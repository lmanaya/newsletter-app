export interface LoginCredentials {
    email: string;
    password: string;
}

export interface RegisterPayload {
    email: string;
    password: string;
    first_name: string;
    last_name: string;
}

export interface User {
    id: number;
    email: string;
    firstName: string;
    lastName: string;
}
