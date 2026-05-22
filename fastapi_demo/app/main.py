import logging
import time
from uuid import uuid4

from fastapi import FastAPI
from fastapi import Request

from .logging_config import setup_logging
from .routers import courses


setup_logging()
logger = logging.getLogger("app.main")

app = FastAPI()


@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", str(uuid4()))
    started_at = time.perf_counter()

    logger.info(
        "request started request_id=%s method=%s path=%s",
        request_id,
        request.method,
        request.url.path,
    )

    try:
        response = await call_next(request)

        duration_ms = (time.perf_counter() - started_at) * 1000
        response.headers["X-Request-ID"] = request_id
        logger.info(
            "request finished request_id=%s method=%s path=%s status_code=%s duration_ms=%.2f",
            request_id,
            request.method,
            request.url.path,
            response.status_code,
            duration_ms,
        )

        return response
    except Exception:
        duration_ms = (time.perf_counter() - started_at) * 1000
        logger.exception(
            "request failed request_id=%s method=%s path=%s duration_ms=%.2f",
            request_id,
            request.method,
            request.url.path,
            duration_ms,
        )
        raise


app.include_router(courses.router)
