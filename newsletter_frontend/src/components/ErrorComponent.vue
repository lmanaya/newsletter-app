<script lang="ts">
import { defineComponent, computed } from 'vue';

export default defineComponent({
    name: 'ErrorComponent',
    props: {
        errors: {
            type: Object,
            required: true,
        },
    },
    setup(props) {
        const hasErrors = computed(() => Object.keys(props.errors).length > 0);
        const nonFieldErrors = computed<String[]>(() => props.errors["non_field_errors"] ?? []);

        return {
            hasErrors,
            nonFieldErrors
        }
    },
});
</script>

<template>
    <div v-if="hasErrors" class="error">
        <ul v-if="nonFieldErrors.length > 0" class="error__non-fields">
            <li v-for="(error, index) in nonFieldErrors" :key="`non_field_errors_${index}`">{{ error }}</li>
        </ul>
    </div>
</template>


<style lang="scss" scoped>
@import "@/styles/variables.scss";

.error {
    & .error__non-fields {
        background-color: $color-red-50;
        color: $color-red-200;
        font-size: $text-sm;
        padding: $size-sm;

        & li {
            margin-left: $size-md;
        }
    }
}
</style>