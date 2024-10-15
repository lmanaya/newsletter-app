import api from './api';

export const fetchNewsletters = async () => {
    return await api.get('/newsletters/');
};
