import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict

from dependencies import connect_to_mongo, close_mongo_connection
from models import CrawlerRequest
from routers import tweets, datasatas, crawler, tweet_trend, text_classification

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
app.include_router(text_classification.router)
