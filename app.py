from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import platform

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud DevOps Project</title>
        <style>
            body {
                background-color: #0f172a;
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }

            .card {
                background: #1e293b;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 0 20px rgba(0,0,0,0.4);
                text-align: center;
                width: 500px;
            }

            h1 {
                color: #38bdf8;
            }

            p {
                color: #cbd5e1;
                font-size: 18px;
            }

            .status {
                margin-top: 20px;
                color: #4ade80;
                font-weight: bold;
            }

            .links {
                margin-top: 30px;
            }

            a {
                color: #38bdf8;
                text-decoration: none;
                display: block;
                margin: 10px 0;
            }

            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>🚀 Cloud FastAPI DevOps Project</h1>

            <p>
                AI-assisted DevOps deployment using Docker,
                GitHub, Railway, and FastAPI.
            </p>

            <div class="status">
                ✅ Application Running Successfully
            </div>

            <div class="links">
                <a href="/health">Health Endpoint</a>
                <a href="/system">System Information</a>
            </div>
        </div>
    </body>
    </html>
    """

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