from fastapi import WebSocket, Depends, FastAPI, APIRouter

from dependencies import get_database

app = FastAPI()

router = APIRouter()


@router.websocket("/ws/tweet_trend")
async def get_tweet_trend(websocket: WebSocket, db=Depends(get_database)):
    await websocket.accept()
    while True:
        collection = db.client["weibo-sentiment-system"]["tweet_by_keyword"]
