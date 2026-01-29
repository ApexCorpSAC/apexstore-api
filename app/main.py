from fastapi import FastAPI
from app.api.v1 import router as api_v1_router
from app.core.config import settings

app = FastAPI(
    title="ApexStore API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(
    api_v1_router,
    prefix=settings.API_V1_PREFIX,
)


@app.get("/", tags=["Health"])
async def health_check():
    return {"status": "ok"}
