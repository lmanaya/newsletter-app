import { User } from "@/types/auth";

export interface State {
    loading: boolean;
    isAuthenticated: boolean;
    user: User | null;
}
