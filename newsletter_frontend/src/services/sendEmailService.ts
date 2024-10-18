import { EmailCreate, EmailUpdate, SendNewsletter } from '@/types/sendEmails';
import api from './apiService';
import { cleanPayload } from '@/utils/payload';

export const getImage = async (id: string | null) => {
    return await api.get(`/emails/images/${id}`);
};

export const createImage = async (payload: FormData) => {
    return await api.post("emails/images/", payload, {
        headers: {
            'Content-Type': 'multipart/form-data',
        }
    });
};

export const getDocument = async (id: string | null) => {
    return await api.get(`/emails/documents/${id}`);
};

export const createDocument = async (payload: FormData) => {
    return await api.post("emails/documents/", payload, {
        headers: {
            'Content-Type': 'multipart/form-data',
        }
    });
};

export const getNewsletterEmail = async (id: String | number) => {
    return await api.get(`/emails/newsletters/${id}`);
};

export const createSendEmail = async (payload: EmailCreate) => {
    return await api.post("/emails/newsletters/", cleanPayload(payload));
}

export const updateSendEmail = async (payload: EmailUpdate) => {
    return await api.patch("/emails/newsletters/", cleanPayload(payload));
}

export const sendNewsletterEmail = async (payload: SendNewsletter) => {
    return await api.post("/emails/send-newsletter/", payload);
}
