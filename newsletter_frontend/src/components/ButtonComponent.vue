<script lang="ts">
import { defineComponent, computed } from 'vue';
import { useRouter, RouteLocationRaw } from 'vue-router';

export default defineComponent({
    name: 'Button',
    props: {
        type: {
            type: String as () => "button" | "submit" | "reset" | "tab" | undefined,
            default: "button"
        },
        to: {
            type: Object as () => RouteLocationRaw,
            required: false
        },
        disabled: {
            type: Boolean,
            default: false
        },
        color: {
            type: String as () => "primary" | "secondary" | "tertiary" | "grey" | "alarm",
            default: "primary",
        },
        size: {
            type: String as () => "small" | "regular" | "large",
            default: "regular",
        },
        variant: {
            type: String as () => "filled" | "outlined" | "ghost" | "link",
            default: "filled",
        },
        loading: {
            type: Boolean,
            default: false,
        }
    },
    setup(props, { emit }) {
        const router = useRouter();

        const buttonClasses = computed(() => [
            "button",
            `button--${props.color}`,
            `button--${props.size}`,
            `button--${props.variant}`,
            { "button--loading": props.loading || props.disabled },
            { "button--tab": props.type === "tab" },
        ]);

        const onclick = () => {
            emit("onclick");

            if (props.to) {
                router.push(props.to);
            }
        }

        return {
            buttonClasses,
            onclick
        }
    },
});
</script>

<template>
    <button
        v-if="type !== 'tab'"
        :type="type"
        :class="buttonClasses"
        :disabled="loading || disabled"
        @click="onclick"
    >
        <span class="button__text">
            <slot></slot>
        </span>
        <div v-if="loading" class="button__spinner"></div>
    </button>
    <button
        v-else
        :type="type"
        :class="buttonClasses"
        :disabled="disabled"
        @click="onclick"
    >
        <span class="button__text">
            <slot></slot>
        </span>
    </button>
</template>


<style lang="scss" scoped>
@import "@/styles/variables.scss";

@mixin button-filled-variant ($color, $text-color) {
    background-color: $color;
    color: $text-color;
}

@mixin button-outlined-variant ($color) {
    background-color: transparent;
    outline-style: solid;
    outline-width: 2px;
    outline-color: $color;
    outline-offset: -2px;
    color: $color;
}

@mixin button-ghost-variant ($text-color) {
    background-color: transparent;
    color: $text-color;
}

@mixin button-link-variant ($text-color) {
    background-color: transparent;
    color: $text-color;
    text-decoration: underline;
}

.button__text {
    text-wrap: nowrap;
}

.button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border: none;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.2s;
    border-radius: $button-border-radius;
    margin-bottom: $size-xs;

    &.button--primary {
        &.button--filled {
            @include button-filled-variant($color-primary-100, $color-white);
            &:hover {
                background-color: $color-primary-200;
            }
        }
        &.button--outlined {
            @include button-outlined-variant($color-primary-100);
            &:hover {
                background-color: $color-primary-200;
            }
        }
        &.button--ghost {
            @include button-ghost-variant($color-primary-100);;
            &:hover {
                background-color: $color-primary-50;
            }
        }
        &.button--link {
            @include button-link-variant($color-primary-100);
        }

        &.button--loading {
            & .button__spinner {
                border-top-color: $color-primary-100;
            }
        }
    }
    &.button--secondary {
        &.button--filled {
            @include button-filled-variant($color-secondary-100, $color-white);
            &:hover {
                background-color: $color-secondary-200;
            }
        }
        &.button--outlined {
            @include button-outlined-variant($color-secondary-100);
            &:hover {
                background-color: $color-secondary-50;
            }
        }
        &.button--ghost {
            @include button-ghost-variant($color-secondary-100);
            &:hover {
                background-color: $color-secondary-50;
            }
        }
        &.button--link {
            @include button-link-variant($color-secondary-100);
        }

        &.button--loading {
            & .button__spinner {
                border-top-color: $color-secondary-100;
            }
        }
    }
    &.button--tertiary {
        &.button--filled {
            @include button-filled-variant($color-tertiary-100, $color-white);
            &:hover {
                background-color: $color-tertiary-200;
            }
        }
        &.button--outlined {
            @include button-outlined-variant($color-tertiary-100);
            &:hover {
                background-color: $color-tertiary-50;
            }
        }
        &.button--ghost {
            @include button-ghost-variant($color-tertiary-100);
            &:hover {
                background-color: $color-tertiary-50;
            }
        }
        &.button--link {
            @include button-link-variant($color-tertiary-100);
        }

        &.button--loading {
            & .button__spinner {
                border-top-color: $color-tertiary-100;
            }
        }
    }
    &.button--grey {
        &.button--filled {
            @include button-filled-variant($color-grey-300, $color-white);
            &:hover {
                background-color: $color-grey-400;
            }
        }
        &.button--outlined {
            @include button-outlined-variant($color-grey-300);
            &:hover {
                background-color: $color-grey-100;
            }
        }
        &.button--ghost {
            @include button-ghost-variant($color-grey-300);;
            &:hover {
                background-color: $color-grey-100;
            }
        }
        &.button--link {
            @include button-link-variant($color-grey-300);
        }

        &.button--loading {
            & .button__spinner {
                border-top-color: $color-grey-300;
            }
        }
    }
    &.button--alarm {
        &.button--filled {
            @include button-filled-variant($color-red-100, $color-white);
            &:hover {
                background-color: $color-red-200;
                color: $color-white;
            }
        }
        &.button--outlined {
            @include button-outlined-variant($color-red-100);
            &:hover {
                background-color: $color-red-50;
            }
        }
        &.button--ghost {
            @include button-ghost-variant($color-red-100);;
            &:hover {
                background-color: $color-red-50;
            }
        }
        &.button--link {
            @include button-link-variant($color-red-100);
        }

        &.button--loading {
            & .button__spinner {
                border-top-color: $color-red-200;
            }
        }
    }

    &.button--filled {
        &.button--loading {
            & .button__spinner {
                border-top-color: $color-white;
            }
        }
    }

    &.button--small {
        padding: 0 16px;
        height: $button-height-small;
        font-size: $text-sm;

        &.button--loading {
            & .button__spinner {
                width: 10px;
                height: 10px;
                border-width: 2px;
            }
        }
    }
    &.button--regular {
        padding: 0 18px;
        font-size: $text-base;
        height: $button-height;

        &.button--loading {
            & .button__spinner {
                width: 16px;
                height: 16px;
                border-width: 2px;
            }
        }
    }
    &.button--large {
        padding: 0 24px;
        height: $button-height-large;
        font-size: $text-md;

        &.button--loading {
            & .button__spinner {
                width: 20px;
                height: 20px;
                border-width: 2px;
            }
        }
    }

    &.button--loading {
        pointer-events: none;
        opacity: 0.6;

        & .button__spinner {
            margin-left: 10px;
            border: 2px solid rgba(0, 0, 0, 0.1);
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
    }

    &.button--tab {
        border-radius: 0px;
    }
}

@keyframes spin {
    to {
        transform: rotate(360deg); /* Gira el círculo completamente */
    }
}
</style>