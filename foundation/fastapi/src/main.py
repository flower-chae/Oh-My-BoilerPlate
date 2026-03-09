# ============================================
# FastAPI Boilerplate
# ============================================
# 1. 프로젝트 초기화
#    uv init --python=3.11
#
# 2. 의존성 설치
#    uv add "fastapi[standard]" "loguru"
#
# 3. 서버 실행
#    uv run uvicorn src.main:app --port=8081 --reload --host 0.0.0.0
# ============================================

from fastapi import FastAPI

from src.core.cors import setup_cors
from src.core.exceptions import (
    AppException,
    app_exception_handler,
    global_exception_handler,
)
from src.middleware import LoggingMiddleware
from src.routers import sample_router


app = FastAPI()

# 예외 핸들러 등록
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(AppException, app_exception_handler)

# 미들웨어 등록
setup_cors(app)
app.add_middleware(LoggingMiddleware)

# 라우터 등록
app.include_router(sample_router)
