<script lang="ts">
import { defineComponent, computed, ref } from 'vue';

export default defineComponent({
    name: 'SendEmailBody',
    props: {
        modelValue: {
            required: true
        },
    },
    emits: ['update:modelValue'],
    setup(props, { emit }) {
        const baseHtmlEmail = ref('');

        const newValue = ref('');

        const updateBody = () => {
            emit('update:modelValue', newValue.value);
        }

        return {
            newValue,
            baseHtmlEmail,
            updateBody
        }
    },
});
</script>

<template>
    <div style="font-family: Arial, sans-serif; background-color: white; padding: 30px;">
        <div style=" max-width: 600px; margin: auto; background: white; border-radius: 8px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); padding: 20px;">
            <div class="content" id="content">
                <div v-html="baseHtmlEmail"></div>
                <div class="button-add">+</div>
            </div>
            <div style="padding: 10px; margin-top: 10px; border-top: solid 1px #6c6c6c; text-align: left;">
                <a href="" style="display: inline-block; color: 6c6c6c; text-decoration: none; text-transform: uppercase;">Desuscribirse</a>
            </div>
        </div>
    </div>
</template>


<style lang="scss" scoped>
@import "@/styles/variables.scss";

.button-add {
    padding: 30px;
    display: flex;
    transition: all .4s ease-in-out;
    justify-content: center;
    outline: 1px dashed $color-grey-300;

    &:hover {
        background-color: $color-grey-100;
        cursor: pointer;
    }
}
</style>