from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import os


app = FastAPI()


@app.get("/")
def read_root():
    return HTMLResponse(content="<h1>Hello world</h1>")


if __name__ == "__main__":
    os.system('uvicorn main:app --reload')
