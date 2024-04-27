# 前端

这个项目构建了微博情感分析系统的前端，使用的技术栈有：

- 前端框架：[`vue3 composition API + vite`](https://v3.cn.vuejs.org/guide/introduction.html)
- 路由管理：[`vue-router`](https://next.router.vuejs.org/)
- 跨组件状态管理：[`pinia`](https://pinia.vuejs.org/)
- `css` 框架：[`tailwindcss`](https://tailwindcss.com/)
- 图表库：[`apexcharts`](https://github.com/apexcharts/apexcharts.js)
- 词云图组件：[`VueWordCloud`](https://github.com/SeregPie/VueWordCloud)
- `http` 请求：[`axios`](https://axios-http.com/)
- `websocket`：[`socket.io`](https://socket.io/)

## 内容列表

- [前端](#前端)
  - [内容列表](#内容列表)
  - [安装](#安装)
  - [项目结构](#项目结构)

## 安装

切换到前端目录

```sh
cd frontend
```

安装依赖

```sh
npm install
```

启动

```sh
npm run dev
```

## 项目结构

```
├── README.md
├── frontend.iml
├── index.html
├── jsconfig.json
├── package-lock.json
├── package.json
├── postcss.config.js
├── public
│         └── favicon.ico
├── src
│         ├── App.vue
│         ├── api # api 请求
│         ├── assets # 静态资源
│         ├── components # 组件
│         ├── layout # 布局组件
│         ├── main.css # 全局样式
│         ├── main.js
│         ├── router # 路由
│         ├── stores # 状态管理
│         ├── utils # 工具函数
│         └── views # 页面
├── tailwind.config.js # tailwindcss 配置
└── vite.config.js
```
