"""FastAPI application entry point for IEP Planning Support Service"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="IEP Planning Support API",
    description="개별화교육계획(IEP) 설계 지원 서비스 백엔드 API",
    version="0.1.0",
)

# CORS middleware for React frontend development
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


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    """
    서버 상태 확인 엔드포인트
    
    Returns:
        dict: 서버 상태 정보
    """
    return {"status": "ok"}

