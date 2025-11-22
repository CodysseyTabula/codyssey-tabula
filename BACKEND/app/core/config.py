"""애플리케이션 설정 모듈

환경 변수를 통해 설정을 관리합니다.
pydantic-settings v2를 사용하여 타입 안전성을 보장합니다.
"""
from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """애플리케이션 설정 클래스
    
    환경 변수 또는 .env 파일에서 설정을 로드합니다.
    """
    
    # 애플리케이션 설정
    app_env: str = Field(default="local", description="실행 환경 (local, docker, production)")
    app_debug: bool = Field(default=True, description="디버그 모드 활성화 여부")
    app_port: int = Field(default=8000, description="서버 포트")
    
    # 데이터베이스 설정
    db_host: str = Field(default="localhost", alias="DB_HOST", description="데이터베이스 호스트")
    db_port: int = Field(default=5432, alias="DB_PORT", description="데이터베이스 포트")
    db_user: str = Field(default="iep_user", alias="DB_USER", description="데이터베이스 사용자명")
    db_password: str = Field(default="iep_password", alias="DB_PASSWORD", description="데이터베이스 비밀번호")
    db_name: str = Field(default="iep_db", alias="DB_NAME", description="데이터베이스 이름")
    database_url: str | None = Field(default=None, alias="DATABASE_URL", description="직접 데이터베이스 URL 지정 (선택사항)")
    
    @property
    def sqlalchemy_database_uri(self) -> str:
        """SQLAlchemy 데이터베이스 URI 생성
        
        DATABASE_URL이 제공된 경우 그것을 사용하고,
        그렇지 않으면 개별 DB_* 변수들로부터 URI를 구성합니다.
        
        Returns:
            str: PostgreSQL 데이터베이스 연결 URI
        """
        if self.database_url:
            return self.database_url
        return (
            f"postgresql+psycopg2://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )
    
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
    }


# 싱글톤 인스턴스
settings = Settings()

