import { createStore } from 'vuex';
import { State } from '@/types/store';
import { User } from '@/types/auth';

const store = createStore<State>({
    state: {
        loading: false,
        isAuthenticated: localStorage.getItem('isAuthenticated') === 'true',
        user: null,
    },
    mutations: {
        setLoading(state: State, loading: boolean) {
            state.loading = loading;
        },
        setAuthentication(state: State, isAuthenticated: boolean) {
            state.isAuthenticated = isAuthenticated;
            localStorage.setItem('isAuthenticated', String(isAuthenticated));
        },
        setUser(state: State, user: User | null) {
            state.user = user;
            if (user) { localStorage.setItem('user', JSON.stringify(user)); }
            else { localStorage.removeItem('user')}
        },
    },
    actions: {
        loading({ commit }, loading: boolean) {
            commit('setLoading', loading);
        },
        login({ commit }, data: {user: User, accessToken: string, refreshToken: string}) {
            commit('setAuthentication', true);
            commit('setUser', data.user);
            localStorage.setItem('accessToken', data.accessToken);
            localStorage.setItem('refreshToken', data.refreshToken);
        },
        logout({ commit }) {
            commit('setAuthentication', false);
            commit('setUser', null);
            localStorage.removeItem('accessToken');
            localStorage.removeItem('refreshToken');
        },
    },
    getters: {
        isLoading: (state: State) => state.loading,
        isAuthenticated: (state: State) => state.isAuthenticated,
        getUser: (state: State) => state.user,
    },
});

export default store;
