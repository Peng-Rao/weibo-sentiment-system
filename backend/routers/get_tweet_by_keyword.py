from typing import List

from fastapi import APIRouter, Depends

from classifier.model import LstmClassifier, get_classifier
from models import TweetItem
from motor.motor_asyncio import AsyncIOMotorClient
from db import DataBase, get_database

router = APIRouter()


@router.get("/get_tweet_by_keyword", response_model=List[TweetItem])
async def get_tweet_by_keyword(keyword: str, db: DataBase = Depends(get_database)):
    collection = db.client["weibo-sentiment-system"]["tweet_by_keyword"]
    # projection = {field: True for field in TweetItem.__fields__}
    tweets = []
    async for tweet in collection.find({"keyword": keyword}):
        # 只取模型需要的字段
        tweets.append(tweet)
    return tweets
