import json

from fastapi import WebSocket, Depends, FastAPI, APIRouter

from dependencies import get_database
from datetime import datetime, timedelta

app = FastAPI()

router = APIRouter()


@router.websocket("/ws/tweet_trend")
async def get_tweet_trend(websocket: WebSocket, db=Depends(get_database)):
    await websocket.accept()
    while True:
        # 接受客户端发送的数据
        receive_data = await websocket.receive_text()
        receive_data = json.loads(receive_data)
        time_range, keyword = receive_data["range"], receive_data["keyword"]
        collection = db.client["weibo-sentiment-system"]["tweet_by_keyword"]

        # 计算一天内的正向情感文档数量
        def count_positive_in_day(query_time: datetime):
            start_of_day = query_time.replace(hour=0, minute=0, second=0, microsecond=0)
            end_of_day = query_time.replace(hour=23, minute=59, second=59, microsecond=999999)
            return collection.count_documents({
                'created_at': {
                    '$gte': start_of_day.isoformat(),
                    '$lt': end_of_day.isoformat()
                },
                'keyword': keyword,
                'sentiment': "positive"
            })

        # 计算一天内的负向情感文档数量
        def count_negative_in_day(query_time: datetime):
            start_of_day = query_time.replace(hour=0, minute=0, second=0, microsecond=0)
            end_of_day = query_time.replace(hour=23, minute=59, second=59, microsecond=999999)
            return collection.count_documents({
                'created_at': {
                    '$gte': start_of_day.isoformat(),
                    '$lt': end_of_day.isoformat()
                },
                'keyword': keyword,
                'sentiment': "negative"
            })
        data = {
            "labels": [],
            "series": [
                {
                    "name": "正向",
                    "data": []
                },
                {
                    "name": "负向",
                    "data": []
                }
            ],
            "start_date": "2021-01-01",
            "end_date": "2021-01-31"
        }

        # 根据时间范围计算正负向情感文档数量
        count = 0
        start_date = None
        end_date = None
        now = datetime.now()
        if time_range == "Week":
            count = 8
            start_date = (now - timedelta(days=7)).replace(hour=0, minute=0, second=0, microsecond=0).strftime("%Y.%m."
                                                                                                               "%d")
            end_date = now.replace(hour=23, minute=59, second=59, microsecond=999999).strftime("%Y.%m.%d")
        else:
            count = 31
            start_date = (now - timedelta(days=30)).replace(hour=0, minute=0, second=0, microsecond=0).strftime("%Y.%m."
                                                                                                                "%d")
            end_date = now.replace(hour=23, minute=59, second=59, microsecond=999999).strftime("%Y.%m.%d")
        for i in range(1, count):
            query_time = now - timedelta(days=count - i)
            data["labels"].append(query_time.strftime("%d"))
            # 计算当天的正负向情感文档数量
            positive_counts_in_day = await count_positive_in_day(query_time)
            negative_counts_in_day = await count_negative_in_day(query_time)
            data["series"][0]["data"].append(positive_counts_in_day)
            data["series"][1]["data"].append(negative_counts_in_day)
        data["start_date"] = start_date
        data["end_date"] = end_date
        await websocket.send_json(data)
