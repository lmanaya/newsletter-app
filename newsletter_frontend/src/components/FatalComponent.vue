<script lang="ts">
import { defineComponent } from 'vue'
import ButtonComponent from './ButtonComponent.vue';
import ModalComponent from './ModalComponent.vue';

export default defineComponent({
    name: 'FatalComponent',
    emits: ['close'],
    setup() {
        const reload = () => {
            window.location.reload();
        };

        return {
            reload
        }
    },
    components: {
        ButtonComponent,
        ModalComponent
    }
})
</script>

<template>
    <ModalComponent :show="true" @close="() => ($emit('close'))">
        <template #header>
            <h2>Ups! algo salió mal</h2>
        </template>
        <template #body>
            <img src="../assets/images/error.svg" alt="">
        </template>
        <template #footer>
            <ButtonComponent color="alarm" @onclick="reload">Recargar la página</ButtonComponent>
        </template>
    </ModalComponent>
</template>

<style lang="scss" scoped>
@import "@/styles/variables.scss";

.title {
    font-size: $text-lg;
}

img {
    width: 100%;
    max-height: 200px;
    margin: auto;
}

button {
    width: 100%;
}
</style>