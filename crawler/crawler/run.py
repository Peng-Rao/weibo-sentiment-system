import os
import sys

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.comment import CommentSpider
from spiders.tweet_by_keyword import TweetSpiderByKeyword
from spiders.tweet_spider_by_tweet_id import TweetSpiderByTweetID
from spiders.tweet_spider_by_user_id import TweetSpiderByUserID
from spiders.user import UserSpider

if __name__ == '__main__':
    # mode = sys.argv[1]
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'settings'
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    mode_to_spider = {
        'tweet_by_keyword': TweetSpiderByKeyword,
        'tweet_spider_by_user_id': TweetSpiderByUserID,
        'tweet_spider_by_tweet_id': TweetSpiderByTweetID,
        'user': UserSpider,
        'comment': CommentSpider,
    }
    # process.crawl(mode_to_spider['tweet_by_keyword'])
    # process.crawl(mode_to_spider['tweet_spider_by_user_id'])
    # process.crawl(mode_to_spider['tweet_spider_by_tweet_id'])
    process.crawl(mode_to_spider['tweet_by_keyword'])
    # process.crawl(mode_to_spider['user'])
    # the script will block here until the crawling is finished
    process.start()
