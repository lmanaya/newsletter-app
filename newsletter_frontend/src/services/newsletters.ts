import { NewNewsletter, NewSubscriber, UnsubscribePayload } from '@/types/newsletter';
import api from './api';

export const fetchNewsletters = async () => {
    return await api.get('/newsletters/');
};

export const getNewsletter = async (id: string | number) => {
    return await api.get(`/newsletters/${id}`);
};

export const createNewsletter = async (credentials: NewNewsletter) => {
    return await api.post('/newsletters/', credentials);
};

export const subscribe = async (payload: NewSubscriber) => {
    return await api.post('/subscribe/', payload);
};

export const unsubscribe = async (payload: UnsubscribePayload) => {
    console.log(payload);
    return await api.post('/unsubscribe/', payload);
};
