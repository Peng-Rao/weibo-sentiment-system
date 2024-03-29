import {createRouter, createWebHashHistory} from 'vue-router'

const router = createRouter({
    history: createWebHashHistory(), // hash 模式
    routes: [
        {
            path: '/keyword',
            component: () => import('@/views/KeywordAnalysis.vue')
        },
        {
            path: '/test',
            component: () => import('@/views/WebSockerDemo.vue')
        },
        {
            path: '/prediction',
            component: () => import('@/views/Prediction.vue')
        }
    ]
})

export default router