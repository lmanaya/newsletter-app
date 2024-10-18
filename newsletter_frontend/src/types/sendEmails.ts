import { Newsletter } from "./newsletter";

export interface BaseEmail {
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

export interface EmailCreate extends BaseEmail {
    newsletter: number;
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

export interface NewsletterEmail extends BaseEmail {
    id: number;
    newsletter: number | Newsletter
}

export interface SendNewsletter {
    newsletter_email: number;
}
