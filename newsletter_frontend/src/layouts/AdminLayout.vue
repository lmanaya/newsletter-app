<script lang="ts">
import { defineComponent } from 'vue';
import { useAuth } from '../composables/useAuth';
import HeaderComponent, { Link } from '../components/HeaderComponent.vue';

export default defineComponent({
    name: 'AuthLayout',
    setup() {
        const links: Link[] = [
            {
                path: { name: 'Create' },
                name: "Crear"
            },
            {
                path: { name: 'Send' },
                name: "Enviar"
            },
        ];

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
                    <div class="layout__logo">
                        <img src="../assets/logo/logo-secondary.svg" width="20">
                        <p class="layout__title">Admin</p>
                    </div>
                </router-link>
            </template>
        </HeaderComponent>
        <router-view></router-view>
    </div>
</template>

<style lang="scss" scoped></style>