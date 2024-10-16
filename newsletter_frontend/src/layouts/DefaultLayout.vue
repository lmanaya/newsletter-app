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
                    <p class="layout__title">¡Newsletters!</p>
                </router-link>
            </template>
        </HeaderComponent>
        <router-view></router-view>
    </div>
</template>

<style lang="scss" scoped>
@import "@/styles/variables.scss";

.layout__title {
    font-size: $size-lg;
    font-weight: 600;
}
</style>