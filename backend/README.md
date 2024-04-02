# 后端

这个项目构建了微博情感分析系统的后端，使用的技术栈有：
- 后端框架： [FastAPI](https://fastapi.tiangolo.com/)
- 数据库： [MongoDB](https://www.mongodb.com/)
- 数据库连接： [motor](https://motor.readthedocs.io/en/stable/)
- websocket 协议：[starlette](https://www.starlette.io/websockets/)
- 依赖构建工具：[poetry](https://python-poetry.org/)

## 内容列表
- [安装](#安装)
- [项目结构](#项目结构)

## 安装
切换到后端目录
```sh
cd backend
```
使用 poetry 安装依赖
```sh
poetry install
```
启动
```sh
uvicorn main:app --reload
```
查看接口文档 127.0.0.1:8000/docs

## 项目结构
```
├── README.md
├── backend.iml
├── classifier # 情感分类模型
│         ├── data
│         ├── helper.py
│         ├── model.py
│         ├── models
│         └── utils.py
├── dependencies.py # 依赖注入
├── main.py # 入口文件
├── models.py # 数据库模型
├── package-lock.json
├── package.json
├── poetry.lock
├── pyproject.toml
├── routers
│         ├── crawler.py # 爬虫调度路由
│         ├── datasatas.py # 数据统计路由
│         ├── text_classification.py # 文本分类路由
│         ├── tweet_trend.py # 周/月统计路由
│         └── tweets.py # 推文数据路由
└── test_main.http
```