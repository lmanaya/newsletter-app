<script lang="ts">
import useVuelidate from '@vuelidate/core';
import { email, required } from '@vuelidate/validators';
import { defineComponent, computed, ref } from 'vue';
import { useRequest } from '../composables/useRequest';
import { NewSubscriber } from '../types/newsletter';
import ButtonComponent from './ButtonComponent.vue';
import InputComponent from './InputComponent.vue';
import ErrorComponent from './ErrorComponent.vue';


export default defineComponent({
    name: 'SubscribeComponent',
    props: {
        newsletter: {
            type: Object as () => { id: number, title: String, text: String, call_to_action_text: String},
            required: true,
        }
    },
    emits: [ 'subscribe' ],
    setup(props, { emit }) {
        const colorOptions = ["primary", "secondary", "tertiary"];
        const randomIndex = Math.floor(Math.random() * colorOptions.length);
        const color = colorOptions[randomIndex];

        const showForm = ref<Boolean>(false);
        const form = ref<NewSubscriber>({
            email: '',
            newsletter: props.newsletter.id
        });

        const { loading, formErrors, post } = useRequest(form.value);

        const rules = {
            form: {
                email: { required, email }
            },
        };

        const v$ = useVuelidate(rules, { form });

        const submitForm = async () => {
            if (!v$.value.$invalid) {
                const response = await post("/subscribe/", form.value);
                if (response.status === 200) {
                    emit('subscribe', props.newsletter.id);
                    showForm.value = false;
                }
            }
        };

        const resetForm = async () => {
            form.value = { email: '', newsletter: props.newsletter.id };
            showForm.value = false;
        };

        return {
            color,
            showForm,
            loading,
            v$,
            form,
            formErrors,
            submitForm,
            resetForm
        }
    },
    components: {
        ButtonComponent,
        InputComponent,
        ErrorComponent
    }
});
</script>

<template>
    <div class="card__container">
        <div class="card">
            <div class="card__header">
                <div :class="`card__dot card__dot--${ color }`"></div>
                <p class="card__title">{{ newsletter.name }}</p>
            </div>
            <p class="card__text">{{ newsletter.description }}</p>
            <div class="card__action">
                <ButtonComponent
                    v-if="!showForm"
                    @click="() => (showForm = true)"
                    :color="color"
                >
                    {{ newsletter.call_to_action_text }}
                </ButtonComponent>
                <form v-else @submit.prevent="submitForm">
                    <div class="card__form">
                        <div class="card__input">
                            <InputComponent
                                type="text"
                                name="email"
                                placeholder="Correo Electrónico"
                                v-model="form.email"
                                :errors="[
                                    ...v$.form.email.$errors,
                                    ...(formErrors?.email || [])
                                ]"
                                @blur="v$.form.email.$touch()"
                            />
                        </div>
                        <ButtonComponent
                            :color="color"
                            type="submit"
                            variant="outlined"
                            :disabled="v$.$invalid"
                            :loading="loading"
                        >
                            OK
                        </ButtonComponent>
                        <ButtonComponent
                            :color="color"
                            variant="ghost"
                            @click="resetForm()"
                        >
                            <img src="../assets/icons/cross.svg" alt="" width="10">
                        </ButtonComponent>
                    </div>
                    <ErrorComponent v-if="formErrors" :errors="formErrors"/>
                </form>
            </div>
        </div>
    </div>
</template>


<style lang="scss" scoped>
@import "@/styles/variables.scss";
@import "@/styles/mixins.scss";

.card__container {
    margin: $size-sm;
    max-width: 40%;
    display: block;
    min-width: 300px;

    @include responsive(mobile) {
        width: 100%;
        max-width: 100%;
    }
}

.card {
    background-color: $color-grey-50;
    box-shadow: $box-shadow-card;
    border-radius: $size-lg;
    padding: $size-md $size-lg;

    & .card__header {
        display: flex;
        align-items: start;
        justify-content: flex-start;
        margin-bottom: $size-sm;

        & .card__title {
            font-weight: bold;
            font-size: $text-lg;
        }

        & .card__dot {
            margin: $size-sm;
            width: $size-md;
            height: $size-md;
            border-radius: 50%;

            &.card__dot--primary {
                background-color: $color-primary-100;
            }
            &.card__dot--secondary {
                background-color: $color-secondary-100;
            }
            &.card__dot--tertiary {
                background-color: $color-tertiary-100;
            }
        }
    }

    & .card__text {
        font-size: $text-base;
        margin-bottom: $size-sm;
    }

    & .card__action {
        width: 100%;
        display: flex;
        justify-content: flex-end;

        & form {
            width: 100%;

            & .card__form {
                display: flex;
                gap: $size-xs;

                & .card__input {
                    flex-grow: 1;
                }
            }
        }
    }
}
</style>