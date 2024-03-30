import asyncio
import random
from db import connect_to_mongo, close_mongo_connection
from typing import Dict

from fastapi import FastAPI, WebSocket, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.websockets import WebSocketDisconnect

import sys
import os
import requests

from models import CrawlerRequest
from routers import get_tweet_by_keyword, get_datasatas

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()


@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(get_tweet_by_keyword.router)
app.include_router(get_datasatas.router)


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    probabilities: Dict[str, float]
    sentiment: str
    confidence: float


def generate_data():
    def random_data():
        return round(random.uniform(10, 100), 2)

    return {
        "dataset": {
            "dimensions": ["Product", "2015", "2016", "2017"],
            "source": [
                {"Product": "Matcha Latte", "2015": random_data(), "2016": random_data(), "2017": random_data()},
                {"Product": "Milk Tea", "2015": random_data(), "2016": random_data(), "2017": random_data()},
                {"Product": "Cheese Cocoa", "2015": random_data(), "2016": random_data(), "2017": random_data()},
                {"Product": "Walnut Brownie", "2015": random_data(), "2016": random_data(), "2017": random_data()},
            ],
        },
        "xAxis": {"type": "category"},
        "yAxis": {},
        "series": [{"type": "bar"}, {"type": "bar"}, {"type": "bar"}],
    }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        print(f"WebSocket disconnected with close code: {websocket.client_state}")


@app.websocket("/bar")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            await websocket.send_json(generate_data())
            await asyncio.sleep(1)  # Send new data every 0.5 seconds
    except WebSocketDisconnect:
        print(f"WebSocket disconnected with close code: {websocket.client_state}")


# @app.post("/predict", response_model=SentimentResponse)
# def predict(request: SentimentRequest, model: LstmClassifier = Depends(get_classifier)):
#     probabilities, sentiment, confidence = model.predict(request.text)
#     return SentimentResponse(
#         probabilities=probabilities,
#         sentiment=sentiment,
#         confidence=confidence
#     )


@app.post("/start_crawler")
async def start_crawler(request: CrawlerRequest):
    url = 'http://localhost:6800/schedule.json'
    data = {
        'project': 'crawler',
        'spider': 'tweet_by_keyword',
        'keyword': request.keyword  # 使用模型属性
    }
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # 触发HTTP错误
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))
    return response.json()
