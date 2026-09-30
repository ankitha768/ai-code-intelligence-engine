from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings

app = FastAPI(title=settings.app_name, version="1.0.0", description="AI-assisted code intelligence APIs.")
app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok", "service": settings.app_name, "mode": settings.llm_mode}
