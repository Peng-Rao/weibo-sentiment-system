# 爬虫

这个项目构建了微博情感分析系统的爬虫，使用的技术栈有：
- 爬虫框架：[scrapy](https://scrapy.org/)
- 虚拟请求头：[scrapy-fake-useragent](https://pypi.org/project/scrapy-fake-useragent/)
- 数据库：[MongoDB](https://www.mongodb.com/)
- 数据库连接：[pymongo](https://pymongo.readthedocs.io/en/stable/)
- 爬虫部署与调度：[scrapyd](https://scrapyd.readthedocs.io/en/stable/)

## 内容列表
- [安装](#安装)
- [项目结构](#项目结构)

## 安装
切换到后端目录
```sh
cd crawler
```
使用 poetry 安装依赖
```sh
poetry install
```
启动 scrapyd
```sh
scrapyd
```
启动爬虫
```sh
curl http://localhost:6800/schedule.json -d project=crawler -d spider=tweet_by_keyword
```
如果更新了代码，则使用以下命令打包并上传到 scrapyd
```sh
scrapyd-deploy
```

## 项目结构
```
├── README.md
├── classifier # 情感分类模型
│         ├── data
│         ├── helper.py
│         ├── model.py
│         ├── models
│         └── utils.py
├── crawler
│         ├── __init__.py
│         ├── items.py 
│         ├── middlewares.py
│         ├── pipelines.py # 数据处理
│         ├── settings.py # 爬虫配置
│         └── spiders # 爬虫文件
├── crawler.iml
├── poetry.lock
├── pyproject.toml
├── scrapy.cfg
├── setup.py
└── twistd.pid
```