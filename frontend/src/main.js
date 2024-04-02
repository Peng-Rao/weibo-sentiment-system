import { createApp } from 'vue'
import App from '@/App.vue'
import '@/main.css'
import router from "@/router/index.js";
import { createPinia } from 'pinia'
import '@/assets/css/satoshi.css'
import '@/assets/css/style.css'

const app = createApp(App)
const pinia = createPinia()

app.use(router)
app.use(pinia)
app.mount('#app')
