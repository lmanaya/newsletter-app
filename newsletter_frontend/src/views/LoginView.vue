<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useAuth } from '../composables/useAuth';
import useVuelidate from '@vuelidate/core';
import { required, email } from '@vuelidate/validators';
import ButtonComponent from '../components/ButtonComponent.vue';
import ErrorComponent from '../components/ErrorComponent.vue';
import InputComponent from '../components/InputComponent.vue';
import { useForm } from '../composables/useForm';

export default defineComponent({
    name: 'LoginView',
    setup() {
        const { loading, login } = useAuth();

        const form = ref({
            email: '',
            password: '',
        });

        const { formErrors, setFormErrors } = useForm(form.value);

        const rules = {
            form: {
                email: { required, email },
                password: { required },
            },
        };

        const v$ = useVuelidate(rules, { form });

        const submitForm = async () => {
            if (!v$.value.$invalid) {
                const response = await login({
                    email: form.value.email,
                    password: form.value.password
                });
                if (response.status != 200) {
                    setFormErrors(response.data);
                }
            } else {
                console.log('Formulario error:', form.value);
            }
        };

        return {
            form,
            formErrors,
            v$,
            loading,
            submitForm,
        }
    },
    components: {
        InputComponent,
        ButtonComponent,
        ErrorComponent
    }
});
</script>

<template>
    <div class="login container">
        <div class="login__container">
            <div class="login__title">
                <h1>Iniciar sesión</h1>
            </div>
            <div class="login__form">
                <form @submit.prevent="submitForm">
                    <InputComponent
                        type="text"
                        name="email"
                        label="Correo Electrónico:"
                        v-model="form.email"
                        :errors="v$.form.email.$errors"
                        @blur="v$.form.email.$touch()"
                    />
                    <InputComponent
                        type="password"
                        name="password"
                        label="Contraseña:"
                        v-model="form.password"
                        :errors="v$.form.password.$errors"
                        @blur="v$.form.password.$touch()"
                    />

                    <ErrorComponent v-if="formErrors" :errors="formErrors"/>

                    <ButtonComponent
                        type="submit"
                        :disabled="v$.$invalid"
                        :loading="loading"
                        :preventDefault="false"
                    >
                        Ingresar
                    </ButtonComponent>
                    <ButtonComponent
                        variant="link"
                        size="small"
                        :to="{ name: 'Register' }"
                    >
                        Crear cuenta
                    </ButtonComponent>
                </form>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import "@/styles/variables.scss";

.login {
    padding-left: $size-md;
    padding-right: $size-md;

    & .login__container {
        box-shadow: $box-shadow-regular;
        padding: $size-xl $size-xl;
        margin: $size-lg auto;
        max-width: $breakpoint-mobile;
        background-color: $color-white;
        border-radius: 8px;
    }
    & .login__title {
        text-align: center;
    }
    & .login__form form {
        display: flex;
        flex-direction: column;
        justify-content: stretch;
        max-width: 400px;
        margin: auto;
        padding: $size-sm 0;
    }
}
</style>