from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import reports, exports, health
from .config import settings
import uvicorn

app = FastAPI(title='Figest Relatório Service', version='1.0.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(reports.router, prefix="/reports", tags=["Reports"])
app.include_router(exports.router, prefix="/exports", tags=["Exports"])
app.include_router(health.router, prefix="/health", tags=["Health"])

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.port, reload=True)
