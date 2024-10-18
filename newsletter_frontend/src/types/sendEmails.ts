export interface EmailCreate {
    newsletter: number;
    subject: string;
    title: string;
    content: string;
    body?: string;
    sent_at?: string;
    status?: string;
    subscribers?: number[];
    attached_documents?: number[];
    attached_images?: number[];
}

export interface EmailUpdate {
    subject?: string;
    title?: string;
    content?: string;
    body?: string;
    sent_at?: string;
    status?: string;
    subscribers?: number[];
    attached_documents?: number[];
    attached_images?: number[];
}

export interface NewsletterEmail extends EmailCreate {
    id: number
}

export interface SendNewsletter {
    newsletter_email: number;
}
