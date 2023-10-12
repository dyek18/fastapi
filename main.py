from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/", StaticFiles(directory="public", html=True), name="static")

@app.get("/")
def read_root():
    custom_message = "내가 하고 싶은 말을 여기에 추가하세요."
    return HTMLResponse(content=f"<html><body><h1>Hello, World</h1><p>{custom_message}</p></body></html>")
