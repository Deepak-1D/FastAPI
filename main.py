from fastapi import FastAPI, Request
from pydantic import BaseModel
import request

app = FastAPI()

class Msg(BaseModel):
    msg: str


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


@app.post("/payment/webhook")
async def demo_post(inp: Request):
    req = await inp.json()
    request.post("https://874d-103-130-91-189.in.ngrok.io/webhook", json=req)
    


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}
