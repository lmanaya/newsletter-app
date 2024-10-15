export interface ApiUser {
    id: number;
    email: string;
    first_name: string;
    last_lame: string;
}

export interface PaginatedResponse {
    count: number;
    next: number | null;
    previous: number | null;
    results: [];
}

export interface ErrorResponse {
    status: number;
    data: object;
}