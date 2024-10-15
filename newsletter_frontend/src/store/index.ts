import { createStore } from 'vuex';
import { State, User } from '../types';

const store = createStore<State>({
    state: {
        isAuthenticated: localStorage.getItem('isAuthenticated') === 'true',
        user: null,
    },
    mutations: {
        setAuthentication(state: State, isAuthenticated: boolean) {
            state.isAuthenticated = isAuthenticated;
            localStorage.setItem('isAuthenticated', String(isAuthenticated));
        },
        setUser(state: State, user: User) {
            state.user = user;
        },
    },
    actions: {
        login({ commit }, user: User) {
            commit('setAuthentication', true);
            commit('setUser', user);
        },
        logout({ commit }) {
            commit('setAuthentication', false);
            commit('setUser', null);
        },
    },
    getters: {
        isAuthenticated: (state: State) => state.isAuthenticated,
        getUser: (state: State) => state.user,
    },
});

export default store;
