"""SQLAlchemy Base 클래스 정의

모든 ORM 모델이 상속받을 기본 클래스입니다.
"""
from __future__ import annotations

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """모든 ORM 모델의 기본 클래스
    
    SQLAlchemy 2.x의 DeclarativeBase를 상속받아 정의합니다.
    모든 데이터베이스 모델은 이 클래스를 상속받아야 합니다.
    """
    pass

