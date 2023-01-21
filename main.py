from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse
from fastapi.encoders import jsonable_encoder

import os
import gtext


app = FastAPI()

who_rei = """
I am Ayanami Ray, 
this is a text algorithm that, based on fuzzy logic, 
and also taking into account probability, 
allows you to determine a person's soul by personality."""

dream_rei = """
My dream is to be a pro icon, 
I'm as important to me now as ever, 
as Véronico is for me to be a icon, and I'm a realist
"""


@app.get("/")
async def read_root():
    return HTMLResponse(content="<h1>Hello world</h1>")


@app.get("/index")
async def index():
    return RedirectResponse('/notfound')


@app.get("/notfound", status_code=404)
async def notfound():
    return {"text": "Resource Not Found"}


@app.get("/main")
async def read_main():
    data = "Hello my beloved man (≧◡≦) ♡"
    return PlainTextResponse(content=data)


@app.get("/api/main")
async def main_ai_response():  # hide data processing to json
    return {'text': who_rei,
            'id': 0.01}


@app.get("/api/dream1")
async def dream_ai():  # real data processing to json
    data = {"text": dream_rei}
    json_data = await jsonable_encoder(data)

    return JSONResponse(content=json_data)


@app.get("/api/aitext")
async def get_model(text="I love you"):
    return {"query": text,
            "answer": gtext.gen_rei_text(text)}


if __name__ == "__main__":
    os.system('uvicorn main:app --reload')
