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
    if (to.name == 'Login' && store.state.user.name != '') {
        next({ name: 'Profile' })
    } else if (to.name == 'Profile' && store.state.user.name == '') {
        next({ name: 'Login' })
    }

    next();
})

const store = createStore({
    state() {
        return {
            user: {
                name: '',
                sandwitches: []
            }
        }
    },
    mutations: {
        setUser(state, userdata) {
            state.user = userdata
        },
        addSandwitch(state, sandwitch) {
            state.user.sandwitches.push(sandwitch)
        }
    },
    actions: {
        setUser(context, userdata) {
            context.commit('setUser', userdata)
        },
        addSandwitch(context, sandwitch) {
            context.commit('addSandwitch', sandwitch)
        }
    }
})

createApp(App)
    .use(router)
    .use(store)
    .mount('#app')
