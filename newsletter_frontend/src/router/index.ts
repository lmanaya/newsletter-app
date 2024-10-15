// src/router.ts
import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

import BasicLayout from '../layouts/BasicLayout.vue';
import AuthLayout from '../layouts/AuthLayout.vue';
import store from '../store';
const accessToken = localStorage.getItem("accessToken");
const refreshToken = localStorage.getItem("refreshToken");
const user = localStorage.getItem("user");

const routes: Array<RouteRecordRaw> = [
    {
        path: '/',
        component: BasicLayout,
        beforeEnter: (to, from, next) => {
            if (store.state.isAuthenticated) {
                next({ name: 'Admin' });
            } else {
                next();
            }
        },
        children: [
            {
                path: '',
                name: 'Home',
                component: () => import('../views/HomeView.vue'),
            },
            {
                path: 'login',
                name: 'Login',
                component: () => import('../views/LoginView.vue'),
            },
        ],
    },
    {
        path: '/admin',
        component: AuthLayout,
        beforeEnter: (to, from, next) => {
            if (!store.state.isAuthenticated) {
                next({ name: 'Login' });
            } else {
                next();
            }
        },
        children: [
            {
                path: '',
                name: 'Admin',
                component: () => import('../views/AdminView.vue'),
            },
        ],
    },
    {
        path: '/:catchAll(.*)',
        name: 'NotFound',
        component: () => import('../views/404View.vue'),
    },
];

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
});

export default router;
