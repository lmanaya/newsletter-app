<script lang="ts">
import { defineComponent, computed } from 'vue';
import { useAuth } from '../composables/useAuth';

export default defineComponent({
    name: 'LoginView',
    setup() {
        const {
            loading,
            user,
            login,
            register
        } = useAuth();

        const loginUser = async () => {
            await login({
                email: "adminx@newsletter.com",
                password: "p@ssw0rd"
            });
        };

        const registerUser = async () => {
            await register({
                email: "admin2@newsletter.com",
                password: "p@ssw0rd",
                first_name: "Admin",
                last_name: "Newsletter"
            });
        };

        return {
            loading,
            user,
            loginUser,
            registerUser,
        }
    }
});
</script>

<template>
    <div class="container">
        <p>Login view</p>
        <p v-if="loading">Cargando...</p>
        <button @click.prevent="loginUser">Login</button>
        <button @click.prevent="registerUser">Register</button>
    </div>
</template>

<style>

</style>