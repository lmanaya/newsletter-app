import api from './api';

export const login = async (email: string, password: string) => {
    const response = await api.post('/users/login/', {
        email: email,
        password: password
    });

    localStorage.setItem('accessToken', response.data.access_token);
    localStorage.setItem('refreshToken', response.data.refresh_token);
    localStorage.setItem('user', response.data.user);

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

    return response.data;
};

export const register = async () => {
    const response = await api.post('/users/register/');
    return response.data;
};
