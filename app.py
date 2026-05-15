from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import platform

app = FastAPI()


def page_template(title, content):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>

        <style>
            body {{
                background-color: #0f172a;
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}

            .card {{
                background: #1e293b;
                padding: 40px;
                border-radius: 20px;
                width: 550px;
                box-shadow: 0 0 25px rgba(0,0,0,0.5);
                text-align: center;
            }}

            h1 {{
                color: #38bdf8;
                margin-bottom: 20px;
            }}

            p {{
                font-size: 18px;
                color: #cbd5e1;
            }}

            .green {{
                color: #4ade80;
                font-weight: bold;
            }}

            .info {{
                margin-top: 20px;
                text-align: left;
                background: #0f172a;
                padding: 20px;
                border-radius: 12px;
            }}

            .info p {{
                margin: 10px 0;
            }}

            a {{
                display: inline-block;
                margin-top: 25px;
                color: #38bdf8;
                text-decoration: none;
            }}

            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>

    <body>
        <div class="card">
            {content}
        </div>
    </body>
    </html>
    """


@app.get("/", response_class=HTMLResponse)
def home():

    content = """
    <h1>🚀 Cloud FastAPI DevOps Project</h1>

    <p>
        AI-assisted DevOps deployment using Docker,
        GitHub, Railway, and FastAPI.
    </p>

    <p class="green">
        ✅ Application Running Successfully
    </p>

    <div class="info">
        <p><strong>Tech Stack:</strong> FastAPI, Docker, Railway, GitHub</p>
        <p><strong>Deployment:</strong> Cloud Containerized App</p>
        <p><strong>Status:</strong> Online</p>
    </div>

    <a href="/health">Health Dashboard →</a><br>
    <a href="/system">System Information →</a>
    """

    return page_template("Home", content)


@app.get("/health", response_class=HTMLResponse)
def health():

    content = f"""
    <h1>💚 Health Dashboard</h1>

    <p class="green">
        Application Status: HEALTHY
    </p>

    <div class="info">
        <p><strong>Current Time:</strong> {datetime.now()}</p>
        <p><strong>Server Status:</strong> Running</p>
        <p><strong>API Health:</strong> Operational</p>
    </div>

    <a href="/">← Back Home</a>
    """

    return page_template("Health", content)


@app.get("/system", response_class=HTMLResponse)
def system():

    content = f"""
    <h1>🖥️ System Information</h1>

    <div class="info">
        <p><strong>Python Version:</strong> {platform.python_version()}</p>
        <p><strong>Operating System:</strong> {platform.system()}</p>
        <p><strong>Machine:</strong> {platform.machine()}</p>
    </div>

    <a href="/">← Back Home</a>
    """

    return page_template("System", content)