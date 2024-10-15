<script lang="ts">
import { defineComponent, computed } from 'vue';
import { login, register } from '../services/auth';
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

        const registerUser = () => {
            console.log("register");
            register("admin2@newsletter.com", "p@ssw0rd", "Admin", "Newsletter");
        };

        return {
            isAuthenticated,
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
        <p v-if="isAuthenticated">User is authenticated</p>
        <p v-else>User is not authenticated</p>
        <button @click.prevent="loginUser">Login</button>
        <button @click.prevent="registerUser">Register</button>
    </div>
</template>

<style>

</style>