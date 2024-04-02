# 微博情感分析系统

这个项目构建了微博情感分析系统，前端使用 `Vue3 + Vite + Tailwindcss`，后端使用 `Fastapi`，机器学习模型使用 `sklearn` 和 `pytorch`， 爬虫使用 `scrapy`。

## 内容列表
- [前端](https://github.com/Raopend/weibo-sentiment-system/blob/release/frontend/README.md)
- [后端](https://github.com/Raopend/weibo-sentiment-system/blob/release/backend/README.md)
- [爬虫](https://github.com/Raopend/weibo-sentiment-system/blob/release/crawler/README.md)
- [项目结构](#项目结构)
- [启动](#启动)

## 项目结构
```
├── README.md
├── backend # 后端
├── crawler # 爬虫
├── frontend # 前端
└── notebooks # 模型训练
```

## 启动
先启动爬虫采集数据，然后启动后端，最后启动前端。
