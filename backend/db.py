from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


def get_database() -> DataBase:
    return db


async def connect_to_mongo():
    db.client = AsyncIOMotorClient("mongodb://localhost:27017")
    # 这里可以添加更多数据库初始化逻辑


async def close_mongo_connection():
    db.client.close()
