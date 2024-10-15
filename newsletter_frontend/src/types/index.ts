export interface ApiUser {
    id: number;
    email: string;
    first_name: string;
    last_lame: string;
}

export interface User {
    id: number;
    email: string;
    firstName: string;
    lastName: string;
}

export interface State {
    isAuthenticated: boolean;
    user: User | null;
}
