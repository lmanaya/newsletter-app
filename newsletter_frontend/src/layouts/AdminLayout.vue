<script lang="ts">
import { defineComponent } from 'vue';
import { useAuth } from '../composables/useAuth';
import HeaderComponent, { Link } from '../components/HeaderComponent.vue';

export default defineComponent({
    name: 'AuthLayout',
    setup() {
        const links: Link[] = [];

        const {
            loading,
            logout
        } = useAuth();

        const logoutUser = () => {
            logout();
        };

        return {
            links,
            loading,
            logoutUser
        }
    },
    components: {
        HeaderComponent,
    }
});
</script>

<template>
    <div class="layout">
        <HeaderComponent :links="links">
            <template #main>
                <router-link to="/admin">
                    <p></p>
                    <h1>Admin Newsletters!</h1>
                </router-link>
            </template>
        </HeaderComponent>
        <router-view></router-view>
    </div>
</template>

<style lang="scss" scoped></style>