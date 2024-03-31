import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict

from dependencies import connect_to_mongo, close_mongo_connection
from models import CrawlerRequest
from routers import tweets, datasatas, crawler, tweet_trend

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

app.include_router(tweets.router)
app.include_router(datasatas.router)
app.include_router(crawler.router)
app.include_router(tweet_trend.router)


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    probabilities: Dict[str, float]
    sentiment: str
    confidence: float


# @app.post("/predict", response_model=SentimentResponse)
# def predict(request: SentimentRequest, model: LstmClassifier = Depends(get_classifier)):
#     probabilities, sentiment, confidence = model.predict(request.text)
#     return SentimentResponse(
#         probabilities=probabilities,
#         sentiment=sentiment,
#         confidence=confidence
#     )
