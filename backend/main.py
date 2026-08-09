from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.organizer import router as organizer_router
from backend.routes.stats import router as stats_router

app = FastAPI(title="SmartFile Organizer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(organizer_router)
app.include_router(stats_router)

@app.get("/status")
def get_status() -> dict:
    return {
        "status": "ok",
        "service": "SmartFile Organizer API",
    }