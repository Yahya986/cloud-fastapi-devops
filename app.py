from fastapi import FastAPI
from datetime import datetime
import platform

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "Cloud FastAPI DevOps Project",
        "status": "running",
        "message": "Yahya's AI-assisted DevOps app is live 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": str(datetime.now())
    }

@app.get("/system")
def system():
    return {
        "python_version": platform.python_version(),
        "system": platform.system(),
        "machine": platform.machine()
    }