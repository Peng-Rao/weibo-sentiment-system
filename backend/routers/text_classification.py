from collections import Counter

from fastapi import APIRouter, Depends

from classifier.model import LstmClassifier, get_classifier
from classifier.utils import load_stopwords
from models import SentimentResponse, SentimentRequest
import jieba
import re

router = APIRouter()

stopwords = load_stopwords()


# 定义一个函数来去除文本中的标点符号
def remove_punctuation(text: str) -> str:
    # 定义中文标点符号的正则表达式
    text_no_punctuation = re.sub("@.+?( |$)", " ", text)  # Remove @xxx (username)
    text_no_punctuation = re.sub("【.+?】", " ", text_no_punctuation)  # Remove 【xx】 (content is usually not written by the user)
    # 去除 特殊字符
    text_no_punctuation = re.sub('[^\u4e00-\u9fa5]+', '', text_no_punctuation)
    text_no_punctuation = re.sub("\u200b", " ", text_no_punctuation)
    return text_no_punctuation


@router.post("/predict", response_model=SentimentResponse)
def predict(request: SentimentRequest, model: LstmClassifier = Depends(get_classifier)):
    # 将文本进行情感分类
    probabilities, sentiment, confidence = model.predict(request.text)
    # 首先去除标点
    text_no_punctuation = remove_punctuation(request.text)
    # 使用 jieba 进行分词
    words = jieba.cut(text_no_punctuation)
    # 过滤掉停用词
    filtered_words = [word for word in words if word not in stopwords and word.strip() != '']
    # 计算词频
    word_freq = Counter(filtered_words)
    # 获取频率最高的前20个词
    most_common_words = word_freq.most_common(20)
    # 转换格式
    formatted_response = [[word, freq] for word, freq in most_common_words]
    return SentimentResponse(
        probabilities=probabilities,
        sentiment=sentiment,
        confidence=confidence,
        word_freq=formatted_response
    )
