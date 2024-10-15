<script lang="ts">
import { defineComponent, computed } from 'vue';
import { login, logout, register } from '../services/auth';
import { useStore } from 'vuex';

export default defineComponent({
    name: 'LoginView',
    setup() {
        const store = useStore();

        const isAuthenticated = computed(() => store.getters.isAuthenticated);
        const user = computed(() => store.getters.getUser);

        const loginUser = () => {
            console.log("login");
            login("admin1@newsletter.com", "p@ssw0rd");
        };

        const logoutUser = () => {
            console.log("logout");
            logout();
        };

        const registerUser = () => {
            console.log("register");
            register("admin2@newsletter.com", "p@ssw0rd", "Admin", "Newsletter");
        };

        return {
            isAuthenticated,
            user,
            loginUser,
            logoutUser,
            registerUser,
        }
    }
});
</script>

<template>
    <div class="container">
        <p>Login view</p>
        <p v-if="isAuthenticated">Está autenticado</p>
        <p v-else>No está autenticado</p>
        <button @click.prevent="loginUser">Iniciar sesión</button>
        <button @click.prevent="logoutUser">Cerrar sesión</button>
        <button @click.prevent="registerUser">Registro</button>
    </div>
</template>

<style>

</style>