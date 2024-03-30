from typing import Optional, List, Dict
from pydantic import BaseModel, Field, HttpUrl


class ProvinceCount(BaseModel):
    name: str
    value: int


class TweetItem(BaseModel):
    # mblogid: str = Field(...)
    # created_at: str = Field(...)
    ip_location: Optional[str] = Field(None)
    # reposts_count: int = Field(...)
    # comments_count: int = Field(...)
    # attitudes_count: int = Field(...)
    # source: Optional[str] = Field(None)
    content: Optional[str] = Field(None)
    # pic_urls: Optional[List[str]] = Field(None)
    # pic_num: int = Field(...)
    # isLongText: bool = Field(...)
    # is_retweet: bool = Field(...)
    # url: HttpUrl = Field(...)
    keyword: str = Field(...)
