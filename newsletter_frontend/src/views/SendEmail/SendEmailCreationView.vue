<script lang="ts">
import { required, requiredIf } from '@vuelidate/validators';
import { defineComponent, onMounted, ref } from 'vue';
import { computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useRequest } from '../../composables/useRequest';
import useVuelidate from '@vuelidate/core';
import InputComponent from '../../components/InputComponent.vue';
import ButtonComponent from '../../components/ButtonComponent.vue';
import ErrorComponent from '../../components/ErrorComponent.vue';
import FileComponent from '../../components/FileComponent.vue';

export default defineComponent({
    name: 'SendEmailCreationView',
    setup() {
        const route = useRoute();
        const router = useRouter();
        const newsletterId = computed(() => route.params.id);

        const { loading: initLogin, get } = useRequest({});

        const data = ref({});

        const form = ref({
            newsletter: parseInt(newsletterId.value as string),
            subject: '',
            title: '',
            content: '',
            body: '',
            subscribers: [],
            attached_documents: [],
            attached_images: []
        });

        const { loading, post } = useRequest(form.value);

        const rules = {
            form: {
                newsletter: { required },
                subject: { required },
                title: {
                    requiredIf: requiredIf(function() { return this.form.body === ''; } )
                },
                content: {
                    requiredIf: requiredIf(function() { return this.form.body === ''; } )
                },
                body: {},
                subscribers: { required },
                attached_documents: {},
                attached_images: {}
            },
        };

        const v$ = useVuelidate(rules, { form });

        const submitForm = async () => {
            if (!v$.value.$invalid) {
                const response = await post("/emails/newsletters/", form.value);
                console.log(response);
            }
        };

        onMounted(async () => {
            const response = await get(`/newsletters/${newsletterId.value}/`);
            if (response.status === 200) {
                data.value = response.data;
            } else {
                router.push({ name: 'NewsletterList' });
            }
        })

        return {
            initLogin,
            loading,
            data,
            form,
            v$,
            submitForm,
        };
    },
    components: {
        InputComponent,
        ButtonComponent,
        ErrorComponent,
        FileComponent
    }
});
</script>

<template>
    <div class="create-email">
        <p v-if="initLogin">Cargando...</p>

        <div class="section">
            <h1>Crear correo para "{{ data.name }}"</h1>
        </div>

        <form @submit.prevent="submitForm">
            <InputComponent
                type="text"
                name="subject"
                label="Asunto del correo electrónico:"
                v-model="form.subject"
                :errors="[
                    ...v$.form.subject.$errors,
                    ...(formErrors?.subject || [])
                ]"
                @blur="v$.form.subject.$touch()"
            />

            <InputComponent
                type="text"
                name="title"
                label="Titulo (Opcional):"
                v-model="form.title"
                :errors="[
                    ...v$.form.title.$errors,
                    ...(formErrors?.title || [])
                ]"
                @blur="v$.form.title.$touch()"
            />

            <InputComponent
                type="textarea"
                name="content"
                label="Contenido (Opcional):"
                v-model="form.content"
                :errors="[
                    ...v$.form.content.$errors,
                    ...(formErrors?.content || [])
                ]"
                @blur="v$.form.content.$touch()"
            />

            <FileComponent></FileComponent>
            <ErrorComponent v-if="formErrors" :errors="formErrors"/>

            <ButtonComponent
                type="submit"
                :disabled="v$.$invalid"
                :loading="loading"
            >
                Enviar email
            </ButtonComponent>
        </form>
    </div>
</template>

<style lang="scss" scoped></style>