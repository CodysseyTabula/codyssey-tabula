"""SQLAlchemy 엔진 및 세션 관리

데이터베이스 연결과 세션을 관리합니다.
FastAPI의 의존성 주입을 위한 get_db 함수를 제공합니다.
"""
from __future__ import annotations

from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings

# SQLAlchemy 엔진 생성
# future=True는 SQLAlchemy 2.x 스타일 사용을 명시
engine = create_engine(
    settings.sqlalchemy_database_uri,
    future=True,
)

# 세션 팩토리 생성
# autocommit=False: 명시적으로 commit 호출 필요
# autoflush=False: 명시적으로 flush 호출 필요
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db() -> Generator[Session, None, None]:
    """데이터베이스 세션 의존성
    
    FastAPI 엔드포인트에서 Depends(get_db)로 사용됩니다.
    요청이 끝나면 자동으로 세션을 닫습니다.
    
    Yields:
        Session: SQLAlchemy 데이터베이스 세션
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

