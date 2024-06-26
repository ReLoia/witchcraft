import { createApp } from 'vue'
import { createStore } from 'vuex'
import { createMemoryHistory, createRouter, createWebHistory } from 'vue-router'

import './style.css'
import App from './App.vue'
import './scripts/mouse-handler.js'

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
    },
    {
        path: '/profile',
        name: 'Profile',
        component: () => import('./components/Profile.vue'),
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach((to, from, next) => {

    next();
})

const store = createStore({
    state() {
        return {
            user: {
                username: '',
                sandwitches: []
            }
        }
    },
    mutations: {
        setUser(state, userdata) {
            state.user = userdata
        },
        addSandwitch(state, sandwitch) {
            state.user.sandwitches = [...state.sandwitches, sandwitch]
        }
    },
    actions: {
        setUser(context, userdata) {
            context.commit('setUser', userdata)
        },
        addSandwitch(context, sandwitch) {
            context.commit('addSandwitch', sandwitch)
        },
        async fetchUser(context) {
            const response = await fetch('/api/users/me', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + localStorage.getItem('token')
                }
            });

            if (response.status == 200) {
                const data = await response.json()
                await context.dispatch('setUser', data)
            } else {
                localStorage.removeItem('token')
            }
        }
    }
})

createApp(App)
    .use(router)
    .use(store)
    .mount('#app')
