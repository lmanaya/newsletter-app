<script lang="ts">
import { defineComponent } from 'vue';
import { logout } from '../services/auth';

export default defineComponent({
    name: 'AuthLayout',
    setup() {
        const logoutUser = () => {
            console.log("logout");
            logout();
        };

        return {
            logoutUser
        }
    }
});
</script>

<template>
    <div class="container">
        <button @click.prevent="logoutUser">Logout</button>
        <router-view></router-view>
    </div>
</template>

<style></style>