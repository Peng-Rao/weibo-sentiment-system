import jieba
import re
import csv

stopwords = []
with open("../data/stopwords.txt", "r", encoding="utf8") as f:
    for w in f:
        stopwords.append(w.strip())


def load_corpus(path):
    """
    Load corpus
    """
    data = []
    with open(path, "r", encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header row
        for row in csvreader:
            sentiment, content = row
            content = processing(content)
            data.append((content, int(sentiment)))
    return data


def load_corpus_bert(path):
    """
    Load corpus for BERT
    """
    data = []
    with open(path, "r", encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header row
        for row in csvreader:
            sentiment, content = row
            content = processing_bert(content)
            data.append((content, int(sentiment)))
    return data


def processing(text):
    """
    Data preprocessing
    """
    # Data cleaning part
    text = re.sub("@.+?( |$)", " ", text)  # Remove @xxx (username)
    text = re.sub("【.+?】", " ", text)  # Remove 【xx】 (content is usually not written by the user)
    text = re.sub("\u200b", " ", text)  # '\u200b' is a bad case in this dataset, don't worry about it
    # Word segmentation
    words = [w for w in jieba.lcut(text) if w.isalpha()]
    # Special handling for the negation word `不`: concatenate with the following word
    while "不" in words:
        index = words.index("不")
        if index == len(words) - 1:
            break
        words[index: index + 2] = ["".join(words[index: index + 2])]  # Cool way of slicing assignment for lists
    # Join with spaces to form a string
    result = " ".join(words)
    return result


def processing_bert(text):
    """
    Data preprocessing for BERT
    """
    # Data cleaning part
    text = re.sub("@.+?( |$)", " ", text)  # Remove @xxx (username)
    text = re.sub("【.+?】", " ", text)  # Remove 【xx】 (content is usually not written by the user)
    text = re.sub("\u200b", " ", text)  # '\u200b' is a bad case in this dataset, don't worry about it
    return text

