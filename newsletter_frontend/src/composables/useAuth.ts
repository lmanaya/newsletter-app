import { computed } from 'vue';
import { useStore } from 'vuex';
import { login as loginApi, logout as logoutApi, register as registerApi } from '@/services/authService';
import { transformUser } from '@/utils/transform';
import { LoginCredentials, RegisterPayload } from '@/types/auth';
import { useRouter } from 'vue-router';

export const useAuth = () => {
    const store = useStore();
    const router = useRouter();

    const loading = computed(() => store.state.loading);
    const isAuthenticated = computed(() => store.state.isAuthenticated);
    const user = computed(() => store.state.user);

    const login = async (credentials: LoginCredentials) => {
        try {
            await store.dispatch('loading', true);

            const response = await loginApi(credentials);

            if (response.status === 200) {
                const user = transformUser(response.data.user);
                const accessToken = response.data.access_token;
                const refreshToken = response.data.refresh_token;
                await store.dispatch('login', {
                    user,
                    accessToken,
                    refreshToken
                });
                router.push({ name: "Admin" });
            }

            return response;
        } catch (error: any) {
            console.error("Error Register request:", error);
            return error.response;
        } finally {
            await store.dispatch('loading', false);
        }
    };

    const logout = async () => {
        try {
            await store.dispatch('loading', true);
            await logoutApi();
        } catch (error) {
            console.error("Error Logout request:", error);
        } finally {
            await store.dispatch('logout');
            await store.dispatch('loading', false);
            router.push({ name: "Login" });
        }
    };

    const register = async (data: RegisterPayload) => {
        try {
            await store.dispatch('loading', true);
            return await registerApi(data);
        } catch (error: any) {
            console.error("Error Register request:", error);
            return error.response;
        } finally {
            await store.dispatch('loading', false);
        }
    };

    return {
        loading,
        isAuthenticated,
        user,
        login,
        logout,
        register
    };
}
