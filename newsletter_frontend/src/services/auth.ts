import api from './api';
import store from '../store';
import { transformUser } from '../utils/transform';
import { useRouter } from 'vue-router';

export const login = async (email: string, password: string) => {
    const response = await api.post('/users/login/', {
        email: email,
        password: password
    });

    if (response.status === 200) {
        const user = response.data.user;

        localStorage.setItem('accessToken', response.data.access_token);
        localStorage.setItem('refreshToken', response.data.refresh_token);
        localStorage.setItem('user', user);

        await store.dispatch('login', transformUser(user));

        window.location.reload();
    }
    return response.data;
};

export const logout = async () => {
    const refreshToken = localStorage.getItem('refreshToken');
    const response = await api.post('/users/logout/', {
        refresh_token: refreshToken
    });

    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    localStorage.removeItem('user');

    await store.dispatch('logout');

    window.location.reload();

    return response.data;
};

export const register = async (
    email: string,
    password: string,
    first_name: string,
    last_name: string
) => {
    const response = await api.post('/users/register/', {
        email, password, first_name, last_name
    });
    return response.data;
};
