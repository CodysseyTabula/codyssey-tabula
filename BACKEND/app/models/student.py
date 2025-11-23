from __future__ import annotations

import uuid
from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import String, Date, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from .iep import IEP
    from .student_wechler import StudentWechsler


class Student(Base):
    __tablename__ = "students"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    birth: Mapped[date] = mapped_column(Date, nullable=False)
    grade: Mapped[str] = mapped_column(String, nullable=False)
    guardian_opinion: Mapped[str | None] = mapped_column(String, nullable=True)
    cognitive_level: Mapped[int | None] = mapped_column(Integer, nullable=True)
    social_psych_level: Mapped[int | None] = mapped_column(Integer, nullable=True)
    motor_daily_level: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # Relationships
    wechsler: Mapped["StudentWechsler | None"] = relationship(
        back_populates="student",
        uselist=False,
        cascade="all, delete-orphan",
    )
    ieps: Mapped[list["IEP"]] = relationship(
        back_populates="student",
        cascade="all, delete-orphan",
    )

