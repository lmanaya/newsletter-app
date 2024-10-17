import { NewNewsletter, NewSubscriber } from '@/types/newsletter';
import api from './api';

export const fetchNewsletters = async () => {
    return await api.get('/newsletters/');
};

export const createNewsletter = async (credentials: NewNewsletter) => {
    return await api.post('/newsletters/', credentials);
};

export const subscribe = async (payload: NewSubscriber) => {
    return await api.post('/subscribe/', payload);
};
