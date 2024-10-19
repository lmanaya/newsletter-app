<script lang="ts">
import { defineComponent, ref, watch } from 'vue';
import { useAuth } from '../composables/useAuth';
import useVuelidate from '@vuelidate/core';
import { required, email } from '@vuelidate/validators';
import ButtonComponent from '../components/ButtonComponent.vue';
import ErrorComponent from '../components/ErrorComponent.vue';
import InputComponent from '../components/InputComponent.vue';
import { RegisterPayload } from '../types/auth';
import { useForm } from '../composables/useForm';

export default defineComponent({
    name: 'RegisterView',
    setup() {
        const successRegister = ref<Boolean>(false);

        const { loading, register } = useAuth();

        const form = ref<RegisterPayload>({
            email: '',
            password: '',
            first_name: '',
            last_name: '',
        });

        const { formErrors, setFormErrors } = useForm(form.value);

        const rules = {
            form: {
                email: { required, email },
                password: { required },
                first_name: { required },
                last_name: { required },
            },
        };

        const v$ = useVuelidate(rules, { form });

        const submitForm = async () => {
            if (!v$.value.$invalid) {
                const response = await register(form.value);
                if (response.status != 201) {
                    setFormErrors(response.data);
                } else {
                    successRegister.value = true;
                }
            } else {
                console.log('Formulario error:', form.value);
            }
        };

        return {
            successRegister,
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
    <div class="register container">
        <div class="register__container">
            <div class="register__title">
                <h1>Crear cuenta</h1>
            </div>
            <div class="register__form">
                <div v-if="successRegister" class="register__success">
                    <p>Registro exitoso para el usuario ({{ form.email }}). Ya puedes iniciar sesión.</p>
                    <ButtonComponent
                        variant="link"
                        size="small"
                        :to="{ name: 'Login' }"
                    >
                        Iniciar sesión
                    </ButtonComponent>
                </div>
                <form @submit.prevent="submitForm" v-else>
                    <InputComponent
                        type="text"
                        name="first_name"
                        label="Nombres:"
                        v-model="form.first_name"
                        :errors="[
                            ...v$.form.first_name.$errors,
                            ...(formErrors?.first_name || [])
                        ]"
                        @blur="v$.form.first_name.$touch()"
                    />
                    <InputComponent
                        type="text"
                        name="last_name"
                        label="Apellidos:"
                        v-model="form.last_name"
                        :errors="[
                            ...v$.form.last_name.$errors,
                            ...(formErrors?.last_name || [])
                        ]"
                        @blur="v$.form.last_name.$touch()"
                    />
                    <InputComponent
                        type="text"
                        name="email"
                        label="Correo Electrónico:"
                        v-model="form.email"
                        :errors="[
                            ...v$.form.email.$errors,
                            ...(formErrors?.email || [])
                        ]"
                        @blur="v$.form.email.$touch()"
                    />
                    <InputComponent
                        type="password"
                        name="password"
                        label="Contraseña:"
                        v-model="form.password"
                        :errors="[
                            ...v$.form.password.$errors,
                            ...(formErrors?.password || [])
                        ]"
                        @blur="v$.form.password.$touch()"
                    />

                    <ErrorComponent v-if="formErrors" :errors="formErrors"/>

                    <ButtonComponent
                        type="submit"
                        :disabled="v$.$invalid"
                        :loading="loading"
                        :preventDefault="false"
                    >
                        Resgistrarme
                    </ButtonComponent>
                    <ButtonComponent
                        variant="link"
                        size="small"
                        :to="{ name: 'Login' }"
                    >
                        Ya tengo cuenta
                    </ButtonComponent>
                </form>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import "@/styles/variables.scss";

.register {
    padding-left: $size-md;
    padding-right: $size-md;

    & .register__container {
        box-shadow: $box-shadow-regular;
        padding: $size-xl $size-xl;
        margin: $size-lg auto;
        max-width: $breakpoint-mobile;
        background-color: $color-white;
        border-radius: 8px;
    }
    & .register__title {
        text-align: center;
    }
    & .register__form {
        & .register__success {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: $size-sm 0;
        }
        & form {
            display: flex;
            flex-direction: column;
            justify-content: stretch;
            max-width: 400px;
            margin: auto;
            padding: $size-sm 0;
        }
    }
}
</style>