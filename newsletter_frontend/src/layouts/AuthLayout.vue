<script lang="ts">
import { defineComponent } from 'vue';
import { useAuth } from '../composables/useAuth';

export default defineComponent({
    name: 'AuthLayout',
    setup() {
        const {
            loading,
            logout
        } = useAuth();

        const logoutUser = () => {
            logout();
        };

        return {
            loading,
            logoutUser
        }
    }
});
</script>

<template>
    <div class="container">
        <p v-if="loading">Cargando...</p>
        <button @click.prevent="logoutUser">Logout</button>
        <router-view></router-view>
    </div>
</template>

<style></style>