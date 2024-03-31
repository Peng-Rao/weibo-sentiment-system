from fastapi import APIRouter, Depends
from starlette.websockets import WebSocket
from typing import List, Dict

from dependencies import DataBase, get_database
from models import TweetItem

router = APIRouter()


@router.get("/get_tweet_by_keyword", response_model=List[TweetItem], tags=["tweets"])
async def get_tweet_by_keyword(keyword: str, db: DataBase = Depends(get_database)):
    collection = db.client["weibo-sentiment-system"]["tweet_by_keyword"]
    tweets = []
    async for tweet in collection.find({"keyword": keyword}):
        # 只取模型需要的字段
        tweets.append(tweet)
    return tweets


@router.websocket("/ws/province-count")
async def websocket_province_count(websocket: WebSocket, db: DataBase = Depends(get_database)):
    await websocket.accept()
    while True:
        # 等待客户端发送关键字
        data = await websocket.receive_text()
        keyword = data  # 假设客户端发送的仅是关键字字符串

        query = {}
        if keyword:
            query["keyword"] = {"$regex": keyword, "$options": "i"}  # 不区分大小写的搜索

        chinese_provinces = [
            "北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江",
            "上海", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南",
            "湖北", "湖南", "广东", "广西", "海南", "重庆", "四川", "贵州",
            "云南", "西藏", "陕西", "甘肃", "青海", "宁夏", "新疆",
            "台湾"
        ]

        collection = db.client["weibo-sentiment-system"]["tweet_by_keyword"]
        cursor = collection.find(query)
        province_counts: Dict[str, int] = {province: 0 for province in chinese_provinces}

        async for document in cursor:
            ip_location = document.get("ip_location", "")
            if ip_location in chinese_provinces:
                province_counts[ip_location] += 1

        result = [
            {"name": province, "value": count}
            for province, count in province_counts.items()
        ]

        # 将结果发送回客户端
        await websocket.send_json(result)
