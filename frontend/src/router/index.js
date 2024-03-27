import {createRouter, createWebHashHistory} from 'vue-router'

const router = createRouter({
    history: createWebHashHistory(), // hash 模式
    routes: [
        {
            path: '/',
            component: () => import('@/views/Index.vue')
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