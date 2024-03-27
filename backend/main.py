from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from starlette.websockets import WebSocketDisconnect

from scrapy_project.spiders.tweet_by_keyword import TweetSpiderByKeyword
from scrapy_project.spiders.tweet_spider_by_user_id import TweetSpiderByUserID
from scrapy_project.spiders.user import UserSpider
from scrapy_project.spiders.comment import CommentSpider
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '.', 'scrapy_project'))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    process = CrawlerProcess(get_project_settings())
    await process.crawl(TweetSpiderByKeyword, keyword='python')
    process.start()
    return {"message": "Hello World"}


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
