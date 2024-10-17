<script lang="ts">
import { defineComponent, computed } from 'vue';

export default defineComponent({
    name: 'InputComponent',
    props: {
        type: {
            type: String as () => 'text' | 'textarea',
            default: "text"
        },
        disabled: {
            type: Boolean,
            default: false
        },
        name: {
            type: String,
            required: true
        },
        id: {
            type: String,
            required: false
        },
        placeholder: {
            type: String,
            required: false
        },
        modelValue: {
            required: true
        },
        label: {
            type: String,
            required: false
        },
        errors: {
            type: Object,
            default: {}
        },
    },
    emits: ['update:modelValue', 'blur'],
    setup(props, { emit }) {
        const inputErrors = computed(() => props.errors.map((e: any) => e.$message ?? e));
        const updateValue = (e: any) => {
            emit('update:modelValue', e.target.value);
        }

        return {
            emit,
            inputErrors,
            updateValue,
        }
    },
});
</script>

<template>
    <div class="input">
        <div>
            <label
                v-if="label"
                :for="name"
                class="input__label"
            >{{ label }}</label>
        </div>
        <textarea
            v-if="type == 'textarea'"
            :id="id ?? name"
            :placeholder="placeholder"
            :value="modelValue"
            @input="(e) => updateValue(e)"
            @blur="() => emit('blur')"
        ></textarea>
        <input
            v-else
            :type="type"
            :id="id ?? name"
            :placeholder="placeholder"
            :value="modelValue"
            @input="(e) => updateValue(e)"
            @blur="() => emit('blur')"
        />
        <div>
            <span
                v-for="(error, index) in inputErrors"
                :key="`error_${name}_${index}`"
                class="input__error"
            >{{ error }}</span>
        </div>
    </div>
</template>


<style lang="scss" scoped>
@import "@/styles/variables.scss";

.input {
    display: block;
    margin-bottom: $size-sm;
    width: 100%;

    & .input__label {
        font-size: $text-sm;
    }
    & .input__error {
        font-size: $text-xs;
        color: $color-error-text;
    }
    & input, & textarea {
        background-color: transparent;
        height: $input-height;
        width: 100%;
        padding: 0 $size-sm;
        box-sizing: border-box;
        border-radius: $input-border-radius;
        border: none;
        outline: solid 1px $color-grey-200;
        &:hover {
            outline: solid 1px $color-grey-300;
        }
    }
    & textarea {
        height: $input-height * 2;
        padding: $size-sm $size-sm;
        box-sizing: border-box;
    }
}
</style>