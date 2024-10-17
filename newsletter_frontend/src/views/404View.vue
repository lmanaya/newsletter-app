<script lang="ts">
import { defineComponent } from 'vue';
import HeaderComponent from '../components/HeaderComponent.vue';
import ButtonComponent from '../components/ButtonComponent.vue';

export default defineComponent({
    name: '404View',
    setup() {},
    components: {
        HeaderComponent,
        ButtonComponent
    }
});
</script>

<template>
    <div>
        <HeaderComponent></HeaderComponent>
        <div class="container not-found">
            <img src="../assets/images/not-found.svg" alt="">
            <ButtonComponent :to="{ name: 'Home' }">Ir al inicio</ButtonComponent>
        </div>
    </div>
</template>


<style lang="scss" scoped>
@import "@/styles/variables.scss";
@import "@/styles/mixins.scss";

.not-found {
    @include display-flex;
    flex-direction: column;

    & img {
        max-width: 500px;
        margin: $size-lg;
    }
}
</style>