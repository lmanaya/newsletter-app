<script lang="ts">
import { defineComponent } from 'vue';
import HeaderComponent, { Link } from '../components/HeaderComponent.vue';

export default defineComponent({
    name: 'BasicLayout',
    setup() {
        const links: Link[] = [];

        return {
            links
        }
    },
    components: {
        HeaderComponent
    }
});
</script>

<template>
    <div class="layout">
        <HeaderComponent :links="links">
            <template #main>
                <router-link to="/">
                    <div class="layout__logo">
                        <img src="../assets/logo/logo.svg" width="20">
                        <p class="layout__title">Newsletters App</p>
                    </div>
                </router-link>
            </template>
        </HeaderComponent>
        <router-view></router-view>
    </div>
</template>

<style lang="scss" scoped></style>