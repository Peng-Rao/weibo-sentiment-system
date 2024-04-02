import pymongo
from itemadapter import ItemAdapter

from classifier.model import LstmClassifier


class MongoPipeline:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.classifier = LstmClassifier()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE", "items"),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection_name = spider.name

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        probabilities, sentiment, confidence = self.classifier.predict(item["content"])
        item["sentiment"] = sentiment
        self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        return item
