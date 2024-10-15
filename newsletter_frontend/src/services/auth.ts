import api from './api';
import { LoginCredentials, RegisterPayload } from '@/types/auth';

export const login = async (credentials: LoginCredentials) => {
    return await api.post('/users/login/', credentials);
};

export const logout = async () => {
    const refreshToken = localStorage.getItem('refreshToken');
    return await api.post('/users/logout/', {
        refresh_token: refreshToken
    });
};

export const register = async (data: RegisterPayload) => {
    return await api.post('/users/register/', data);
};
