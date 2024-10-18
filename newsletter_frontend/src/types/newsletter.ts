export interface NewNewsletter {
    name: string;
}

export interface NewSubscriber {
    email: string;
    newsletter: number;
}

export interface UnsubscribePayload {
    unsubscribe_token: string;
    newsletter?: number | null;
}
