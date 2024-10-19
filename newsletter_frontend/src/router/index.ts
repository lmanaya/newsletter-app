// src/router.ts
import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

import DefaultLayout from '../layouts/DefaultLayout.vue';
import AdminLayout from '../layouts/AdminLayout.vue';
import store from '../store';

const routes: Array<RouteRecordRaw> = [
    {
        path: '/',
        component: DefaultLayout,
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
                path: 'ingresar',
                name: 'Login',
                component: () => import('../views/LoginView.vue'),
            },
            {
                path: 'registro',
                name: 'Register',
                component: () => import('../views/RegisterView.vue'),
            },
        ],
    },
    {
        path: '/admin',
        component: AdminLayout,
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
                name: 'NewsletterList',
                component: () => import('../views/Newsletter/NewsletterListView.vue'),
            },
            {
                path: 'emails/envios',
                name: 'EmailList',
                component: () => import('../views/SendEmail/SendEmailListView.vue'),
            },
            {
                path: 'emails/creacion/:id',
                name: 'EmailCreation',
                component: () => import('../views/SendEmail/SendEmailCreationView.vue'),
            },
            {
                path: 'emails/envios/:id',
                name: 'EmailDetail',
                component: () => import('../views/SendEmail/SendEmailDetailView.vue'),
            }
        ],
    },
    {
        path: '/unsubscribe',
        name: 'Unsubscribe',
        component: () => import('../views/Newsletter/NewsletterUnsubscribeView.vue'),
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
