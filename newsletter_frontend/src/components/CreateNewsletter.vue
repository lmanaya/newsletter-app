<script lang="ts">
import useVuelidate from "@vuelidate/core";
import { required } from "@vuelidate/validators";
import { defineComponent, ref } from "vue"
import { useForm } from "../composables/useForm";
import { createNewsletter as create } from "../services/newsletters";
import InputComponent from "./InputComponent.vue";
import ButtonComponent from "./ButtonComponent.vue";
import ErrorComponent from './ErrorComponent.vue'

export default defineComponent({
    name: 'CreateNewsletter',
    emits: [ 'complete' ],
    setup(props, { emit }) {
        const loading = ref<Boolean>(false);
        const form = ref({
            name: '',
            description: '',
            call_to_action_text: '',
        });

        const { formErrors, setFormErrors } = useForm(form.value);

        const rules = {
            form: {
                name: { required },
                description: { required },
                call_to_action_text: { required },
            },
        };

        const v$ = useVuelidate(rules, { form });

        const submitForm = async () => {
            if (!v$.value.$invalid) {
                loading.value = true;
                const response = await create(form.value);
                loading.value = false;
                if (response.status != 201) {
                    setFormErrors(response.data);
                } else {
                    emit('complete');
                }
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
    <form @submit.prevent="submitForm">
        <InputComponent
            type="text"
            name="name"
            label="Nombre:"
            v-model="form.name"
            :errors="v$.form.name.$errors"
            @blur="v$.form.name.$touch()"
        />
        <InputComponent
            type="textarea"
            name="description"
            label="Descripción:"
            v-model="form.description"
            :errors="v$.form.description.$errors"
            @blur="v$.form.description.$touch()"
        />
        <InputComponent
            type="text"
            name="call_to_action_text"
            label="Mensaje de acción:"
            v-model="form.call_to_action_text"
            :errors="v$.form.call_to_action_text.$errors"
            @blur="v$.form.call_to_action_text.$touch()"
        />

        <ErrorComponent v-if="formErrors" :errors="formErrors"/>

        <ButtonComponent
            type="submit"
            :disabled="v$.$invalid"
            :loading="loading"
        >
            Create
        </ButtonComponent>
    </form>
</template>

<style lang="scss" scoped>

</style>