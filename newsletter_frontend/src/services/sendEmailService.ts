import { EmailCreate, EmailUpdate, SendNewsletter } from '@/types/sendEmails';
import api from './apiService';
import { cleanPayload } from '@/utils/payload';

export const getImage = async (id: string | number) => {
    return await api.get(`/emails/images/${id}/`);
};

export const createImage = async (payload: FormData) => {
    return await api.post("emails/images/", payload, {
        headers: {
            'Content-Type': 'multipart/form-data',
        }
    });
};

export const updateImage = async (id: number | string, payload: FormData) => {
    return await api.patch(`emails/images/${id}/`, payload, {
        headers: {
            'Content-Type': 'multipart/form-data',
        }
    });
};

export const getDocument = async (id: string | number) => {
    return await api.get(`/emails/documents/${id}/`);
};

export const createDocument = async (payload: FormData) => {
    return await api.post("emails/documents/", payload, {
        headers: {
            'Content-Type': 'multipart/form-data',
        }
    });
};

export const updateDocument = async (id: number | string, payload: FormData) => {
    return await api.patch(`emails/documents/${id}/`, payload, {
        headers: {
            'Content-Type': 'multipart/form-data',
        }
    });
};

export const getNewsletterEmail = async (id: String | number) => {
    return await api.get(`/emails/newsletters/${id}/`);
};

export const createSendEmail = async (payload: EmailCreate) => {
    return await api.post("/emails/newsletters/", cleanPayload(payload));
}

export const getSendEmails = async (query: string | null) => {
    return await api.get(`/emails/newsletters/${query ? '?' + query : ''}`);
}

export const getSendEmail = async (id: number) => {
    return await api.get(`/emails/newsletters/${id}/`);
}

export const updateSendEmail = async (id: number, payload: EmailUpdate) => {
    return await api.patch(`/emails/newsletters/${id}/`, cleanPayload(payload));
}

export const sendNewsletterEmail = async (payload: SendNewsletter) => {
    return await api.post("/emails/send-newsletter/", payload);
}
