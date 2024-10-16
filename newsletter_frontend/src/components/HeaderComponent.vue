<script lang="ts">
import { defineComponent } from 'vue';
import { useAuth } from '../composables/useAuth';
import ButtonComponent from './ButtonComponent.vue';

export interface Link {
    path: string;
    name: string;
}

export default defineComponent({
    name: 'HeaderComponent',
    props: {
        links: {
            type: Array as () => Link[],
            required: true
        }
    },
    setup() {
        const {
            isAuthenticated,
            logout
        } = useAuth();

        return {
            isAuthenticated,
            logout
        }
    },
    components: {
        ButtonComponent
    }
});
</script>

<template>
    <div class="header">
        <div class="header__container">
            <slot name="main"></slot>
            <div>
                <nav class="navbar">
                    <router-link v-for="link in links" :key="link.path" :to="link.path">{{ link.name }}</router-link>
                </nav>

                <ButtonComponent v-if="isAuthenticated" color="alarm" @click="logout">
                    Cerrar sesión
                </ButtonComponent>
                <router-link :to="{ name: 'Login' }" v-else >
                    <ButtonComponent color="secondary">
                        Ingresar
                    </ButtonComponent>
                </router-link>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import "@/styles/variables.scss";

.header {
    display: flex;
    background-color: $color-background;
}

.header__container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: nowrap;
    max-width: $breakpoint-desktop;
    margin: auto;
    width: 100%;
    padding: 0px $size-md;
}
</style>