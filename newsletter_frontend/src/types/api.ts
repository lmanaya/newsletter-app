export interface ApiUser {
    id: number;
    email: string;
    first_name: string;
    last_lame: string;
}

export interface PaginatedResponse {
    count: number;
    next: String | null;
    previous: String | null;
    results: [];
}

export interface ErrorResponse {
    status: number;
    data: object;
}