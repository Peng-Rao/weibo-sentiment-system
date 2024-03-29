from celery import Celery
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_project.scrapy_project.spiders import TweetSpiderByKeyword

app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')


@app.task
def start_crawler():
    process = CrawlerProcess(get_project_settings())
    process.crawl(TweetSpiderByKeyword, keyword='python')
    process.start()
    return 'Crawler started'
