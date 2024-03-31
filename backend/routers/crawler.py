import requests
from fastapi import HTTPException, APIRouter

from models import CrawlerRequest

router = APIRouter()


@router.post("/start_crawler", tags=['crawler'])
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
