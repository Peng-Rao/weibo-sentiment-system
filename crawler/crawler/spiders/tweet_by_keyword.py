import datetime
import json
import re

from scrapy import Request, Spider

from .common import parse_long_tweet, parse_tweet_info


class TweetSpiderByKeyword(Spider):
    """
    关键词搜索采集
    """
    name = "tweet_by_keyword"
    base_url = "https://s.weibo.com/"

    def __init__(self, keyword=None, start_time=None, end_time=None, is_split_by_hour=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keyword = keyword if keyword else 'python'
        # 爬取时间为过去一个月
        now_time = datetime.datetime.now()
        self.start_time = now_time - datetime.timedelta(days=30)
        self.end_time = now_time
        self.is_split_by_hour = is_split_by_hour

    def start_requests(self):
        """
        爬虫入口
        """
        # 爬取时间为过去一个月
        # 是否按照小时进行切分，数据量更大; 对于非热门关键词**不需要**按照小时切分
        if not self.is_split_by_hour:
            _start_time = self.start_time.strftime("%Y-%m-%d-%H")
            _end_time = self.end_time.strftime("%Y-%m-%d-%H")
            url = f"https://s.weibo.com/weibo?q={self.keyword}&timescope=custom%3A{_start_time}%3A{_end_time}&page=1"
            yield Request(url, callback=self.parse, meta={'keyword': self.keyword})
        else:
            time_cur = self.start_time
            while time_cur < self.end_time:
                _start_time = time_cur.strftime("%Y-%m-%d-%H")
                _end_time = (time_cur + datetime.timedelta(hours=1)).strftime("%Y-%m-%d-%H")
                url = f"https://s.weibo.com/weibo?q={self.keyword}&timescope=custom%3A{_start_time}%3A{_end_time}&page=1"
                yield Request(url, callback=self.parse, meta={'keyword': self.keyword})
                time_cur = time_cur + datetime.timedelta(hours=1)

    def parse(self, response, **kwargs):
        """
        网页解析
        """
        html = response.text
        if '<p>抱歉，未找到相关结果。</p>' in html:
            self.logger.info(f'no search result. url: {response.url}')
            return
        tweets_infos = re.findall('<div class="from"\s+>(.*?)</div>', html, re.DOTALL)
        for tweets_info in tweets_infos:
            tweet_ids = re.findall(r'weibo\.com/\d+/(.+?)\?refer_flag=1001030103_" ', tweets_info)
            for tweet_id in tweet_ids:
                url = f"https://weibo.com/ajax/statuses/show?id={tweet_id}"
                yield Request(url, callback=self.parse_tweet, meta=response.meta, priority=10)
        next_page = re.search('<a href="(.*?)" class="next">下一页</a>', html)
        if next_page:
            url = "https://s.weibo.com" + next_page.group(1)
            yield Request(url, callback=self.parse, meta=response.meta)

    @staticmethod
    def parse_tweet(response):
        """
        解析推文
        """
        data = json.loads(response.text)
        item = parse_tweet_info(data)
        item['keyword'] = response.meta['keyword']
        if item['isLongText']:
            url = "https://weibo.com/ajax/statuses/longtext?id=" + item['mblogid']
            yield Request(url, callback=parse_long_tweet, meta={'item': item}, priority=20)
        else:
            yield item
