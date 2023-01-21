from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder

import os


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
def read_root():
    return HTMLResponse(content="<h1>Hello world</h1>")


@app.get("/main")
def read_main():
    data = "Hello my beloved man (≧◡≦) ♡"
    return PlainTextResponse(content=data)


@app.get("/api/main")
def main_ai_response():  # hide data processing to json
    return {'text': who_rei,
            'id': 0.01}


@app.get("/api/dream1")
def dream_ai():  # real data processing to json
    data = {"text": dream_rei}
    json_data = jsonable_encoder(data)

    return JSONResponse(content=json_data)


if __name__ == "__main__":
    os.system('uvicorn main:app --reload')
