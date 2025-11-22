# IEP Planning Support Service - Backend API

개별화교육계획(IEP) 설계 지원 서비스의 백엔드 API 서버입니다.

## 📚 프로젝트 소개

특수교사가 학생별 개별화교육계획(IEP)을 효율적으로 작성하고 관리할 수 있도록 지원하는 서비스입니다.
AI 기반 목표 추천, 학습자료 추천, 주차별 학습계획 자동 분배 기능을 제공합니다.

## 🛠 기술 스택

- **언어**: Python 3.11+
- **웹 프레임워크**: FastAPI
- **데이터베이스**: PostgreSQL
- **ORM**: SQLAlchemy 2.x (synchronous)
- **검증/설정**: Pydantic v2, pydantic-settings v2
- **서버**: uvicorn (ASGI)
- **컨테이너**: Docker, docker-compose

## 📋 사전 요구사항

- Python 3.11 이상
- PostgreSQL 16
- (선택) Docker & Docker Compose

## 🚀 로컬 개발 환경 실행

### 1. 가상환경 생성 및 활성화

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate  # Windows
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. 환경변수 설정

`.env.example` 파일을 복사하여 `.env` 파일 생성:

```bash
cp .env.example .env
```

필요한 환경변수 수정 (DB 연결 정보 등)

### 4. 서버 실행

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

서버 실행 후 다음 URL에서 확인:
- API 문서: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

## 🐳 Docker로 실행 (예정)

### docker-compose 사용

```bash
docker-compose up -d
```

### 서비스 중지

```bash
docker-compose down
```

## 📁 프로젝트 구조

```
.
├── app/
│   ├── main.py              # FastAPI 애플리케이션 엔트리포인트
│   ├── api/                 # API 라우터
│   │   └── v1/              # API v1 엔드포인트
│   ├── core/                # 설정 및 유틸리티
│   ├── db/                  # 데이터베이스 세션 관리
│   ├── models/              # SQLAlchemy ORM 모델
│   ├── schemas/             # Pydantic 스키마
│   └── services/            # 비즈니스 로직
├── tests/                   # 테스트 코드
├── docker/                  # Docker 관련 파일
├── requirements.txt         # Python 의존성
├── .env.example             # 환경변수 예시
└── README.md
```

## 🔗 주요 엔드포인트

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | 서버 상태 확인 |
| GET | `/docs` | API 문서 (Swagger UI) |

## 📝 개발 규칙

- Git 커밋 메시지: `<Emoji> <Label> : <Title> #<IssueNumber>`
- 브랜치 네이밍: `<label>/<feature-name>/<developer-name>`
- 코딩 스타일: PEP 8, 타입 힌트 필수

## 📄 라이선스

This project is for educational purposes.

