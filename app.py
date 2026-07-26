from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import json
import os
import socket

app = FastAPI()
templates = Jinja2Templates(directory="templates")

CONFIG_PATH = "config.json"

def load_config():
    if not os.path.exists(CONFIG_PATH):
        return []
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Lekérjük a gép vagy konténer hostname-jét
    hostname = socket.gethostname()
    return templates.TemplateResponse(
        request=request, 
        name="index.html",
        context={"hostname": hostname}
    )

@app.get("/api/services")
async def get_services():
    data = load_config()
    return JSONResponse(content=data)