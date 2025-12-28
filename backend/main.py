from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

app = FastAPI(
    title="Choose your own adventure Game API",
    description="API for Choose your own adventure Game",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS, #allow all origins
    allow_credentials=True, #allow credentials
    allow_methods=["*"], # "GET", "POST", "PUT", "DELETE", "OPTIONS"
    allow_headers=["*"],
)
def main():
    print("Hello from backend!")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) #reload=True artinya server otomatis reload ketika ada perubahan
