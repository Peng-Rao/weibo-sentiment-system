import asyncio

from starlette.websockets import WebSocket, WebSocketDisconnect
from typing import List, Dict

from fastapi import APIRouter, Depends

from models import TweetItem, ProvinceCount
from motor.motor_asyncio import AsyncIOMotorClient
from db import DataBase, get_database
import pandas as pd

router = APIRouter()


@router.websocket("/ws/datasatas")
async def websocket_datasatas(websocket: WebSocket, db: DataBase = Depends(get_database)):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        keyword = data  # 假设客户端发送的仅是关键字字符串
        query = {"keyword": keyword} if keyword else {}
        collection = db.client["weibo-sentiment-system"]["tweet_by_keyword"]
        # 统计文档数量
        total_counts = await collection.count_documents(query)
        # 统计评论数，使用聚合框架计算 comments_count 字段之和
        pipeline = [
            {"$match": query},  # 添加了这行代码
            {
                "$group": {
                    "_id": None,
                    "total_comments": {"$sum": "$comments_count"}
                }
            }
        ]
        total_comments_count = await collection.aggregate(pipeline).to_list(1)
        # 统计正向情感文档数量
        positive_query = {"sentiment": "positive", **query}  # 修改了这行代码
        positive_counts = await collection.count_documents(positive_query)
        # 统计负向情感文档数量
        negative_query = {"sentiment": "negative", **query}  # 修改了这行代码
        negative_counts = await collection.count_documents(negative_query)
        await websocket.send_json([
            {"title": "总推文数", "total": total_counts},
            {"title": "总评论数", "total": total_comments_count[0]["total_comments"] if total_comments_count else 0},
            {"title": "正向推文数", "total": positive_counts},
            {"title": "负面推文数", "total": negative_counts},
        ])

