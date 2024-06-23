import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import './scripts/mouse-handler.js'

import { createMemoryHistory, createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import('./components/Home.vue')
    },
    {
        path: '/craft',
        name: 'Craft',
        component: () => import('./components/Craft.vue')
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

createApp(App)
    .use(router)
    .mount('#app')
