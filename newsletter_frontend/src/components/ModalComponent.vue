<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'ModalComponent',
    props: {
        show: {
            type: Boolean,
            default: false,
        }
    },
    emits: ['close'],
    setup(props, { emit }) {
        return { emit }
    }
});
</script>

<template>
    <div v-if="show" class="modal__overlay">
        <div class="modal">
            <header class="modal__header">
                <slot name="header"></slot>
                <button class="modal__close-button" @click="() => emit('close')">&times;</button>
            </header>
            <section class="modal__body">
                <slot name="body"></slot>
            </section>
            <footer class="modal__footer">
                <slot name="footer"></slot>
            </footer>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import "@/styles/variables.scss";

.modal {
    background-color: $color-background;
    padding: $size-lg;
    margin: $size-md;
    border-radius: $input-border-radius;
    box-shadow: rgba($color-grey-300, 0.3) 0px 8px 24px;;
    width: 100%;
    max-width: 500px;

    & .modal__header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    & .modal__body {
        margin: $size-md 0;
    }

    & .modal__close-button {
        background: none;
        border: none;
        font-size: 1.5rem;
        cursor: pointer;
    }
}

.modal__overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba($color-grey-300, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}
</style>