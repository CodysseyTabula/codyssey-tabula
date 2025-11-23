from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

if TYPE_CHECKING:
    from .student import Student


class StudentWechsler(Base):
    __tablename__ = "student_wechsler"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    student_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("students.id"), nullable=False)
    vci_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    visual_spatial_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    fri_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    wmi_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    psi_score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    fsiq_score: Mapped[int | None] = mapped_column(Integer, nullable=True)

