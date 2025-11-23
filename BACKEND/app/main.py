"""IEP 계획 지원 서비스의 FastAPI 애플리케이션 진입점"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.base import Base
from app.db.session import engine

app = FastAPI(
    title="IEP Planning Support API",
    description="개별화교육계획(IEP) 설계 지원 서비스 백엔드 API",
    version="0.1.0",
)

# React 프런트엔드 개발을 위한 CORS 미들웨어
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    """애플리케이션 시작 시 실행되는 이벤트
    
    데이터베이스 테이블을 자동으로 생성합니다.
    (추후 Alembic 마이그레이션으로 대체 예정)
    """
    Base.metadata.create_all(bind=engine)


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    """
    서버 상태 확인 엔드포인트
    
    Returns:
        dict: 서버 상태 정보
    """
    return {"status": "ok"}

