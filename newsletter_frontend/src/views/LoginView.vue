<script lang="ts">
import { defineComponent } from 'vue';
import { login, logout } from '../services/auth';

export default defineComponent({
    name: 'LoginView',
    setup() {
        const loginUser = () => {
            console.log("login");
            login("admin1@newsletter.com", "p@ssw0rd");
        };

        const logoutUser = () => {
            console.log("logout");
            logout();
        };

        return {
            loginUser,
            logoutUser
        }
    }
});
</script>

<template>
    <div class="container">
        <p>Login view</p>
        <button @click.prevent="loginUser">Iniciar sesión</button>
        <button @click.prevent="logoutUser">Cerrar sesión</button>
    </div>
</template>

<style>

</style>