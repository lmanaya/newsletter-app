<script lang="ts">
import { defineComponent, ref } from 'vue';
import useVuelidate from '@vuelidate/core';
import { required } from '@vuelidate/validators';
import { Newsletter } from '../../types/newsletter';
import { EmailCreate, EmailUpdate, NewsletterEmail } from '../../types/sendEmails';
import {
    createSendEmail as createSendEmailApi,
    updateSendEmail as updateSendEmailApi,
    sendNewsletterEmail as sendNewsletterEmailApi
} from '../../services/sendEmailService';
import { useApiService } from '../../composables/useApiService';
import InputComponent from '../InputComponent.vue';
import ButtonComponent from '../ButtonComponent.vue';
import ErrorComponent from '../ErrorComponent.vue';
import SendEmailFiles from '../SendEmail/SendEmailFiles.vue';
import SendEmailSubscribers from '../SendEmail/SendEmailSubscribers.vue';

export default defineComponent({
    name: 'SendEmailForm',
    props: {
        action: {
            type: String as () => 'create' | 'update',
            required: true,
        },
        newsletter: {
            type: [Object as () => Newsletter, Number],
            required: true
        },
        newsletterEmail: {
            type: Object as () => NewsletterEmail,
            required: false
        }
    },
    emits: ['created', 'updated', 'sended'],
    setup(props, { emit }) {
        const newsletterEmail = ref<NewsletterEmail | undefined>(props.newsletterEmail);

        const form = ref<EmailCreate | EmailUpdate>({
            subject: newsletterEmail.value?.subject ?? '',
            title: newsletterEmail.value?.title ?? '',
            content: newsletterEmail.value?.content ?? '',
            body: newsletterEmail.value?.body ?? '',
            sent_at: newsletterEmail.value?.sent_at ?? '',
            status: newsletterEmail.value?.status ?? 'pending',
            subscribers: newsletterEmail.value?.subscribers ?? [],
            attached_documents: newsletterEmail.value?.attached_documents ?? [],
            attached_images: newsletterEmail.value?.attached_images ?? []
        });

        const rules = {
            form: {
                subject: { required },
                title: { required },
                content: { required },
                body: {},
                sent_at: { },
                status: { required },
                subscribers: { },
                attached_documents: {},
                attached_images: {}
            },
        };

        const v$ = useVuelidate(rules, { form });

        const {
            loading: loadingCreate,
            data: createData,
            formErrors: createFormErrors,
            execute: createSendEmail
        } = useApiService(() => createSendEmailApi(
            {...form.value, newsletter: props.newsletter as number} as EmailCreate
        ));

        const {
            loading: loadingUpdate,
            data: updateData,
            formErrors: updateFormErrors,
            execute: updateSendEmail
        } = useApiService(() => updateSendEmailApi(newsletterEmail.value?.id as number, form.value as EmailCreate));

        const {
            loading,
            data,
            formErrors,
            execute: sendNewsletterEmail
        } = useApiService(() => sendNewsletterEmailApi({ newsletter_email: newsletterEmail.value!.id}));

        const sendEmail = async () => {
            await sendNewsletterEmail();
            emit('sended', newsletterEmail.value!.id);
        };

        const submitForm = async (sendNow: Boolean = false) => {
            if (!v$.value.$invalid) {
                console.log(props.action);
                if (props.action === 'create') {
                    if (!!createFormErrors) {
                        await createSendEmail();
                        newsletterEmail.value = createData.value! as NewsletterEmail;
                        if (sendNow) {
                            await sendEmail();
                        }
                        else {
                            emit('created', newsletterEmail.value.id);
                        }
                    }
                } else {
                    if (!!updateFormErrors) {
                        await updateSendEmail();
                        newsletterEmail.value = updateData.value! as NewsletterEmail;
                        if (sendNow) await sendEmail();
                        else {
                            emit('updated', newsletterEmail.value.id);
                        }
                    }
                }
            }
        };

        const updateFile = async (type: string, value: number) => {
            if (type === "document") {
                form.value.attached_documents = [value];
                form.value.attached_images = [];
            } else {
                form.value.attached_documents = [];
                form.value.attached_images = [value];
            }

            if (props.action === 'update') {
                await updateSendEmail();
            }
        };

        const handleSelectionSubscribers = async (value: number[]) => {
            form.value.subscribers = value;
            if (props.action === 'update') {
                await updateSendEmail();
            }
        }

        return {
            loadingCreate,
            loadingUpdate,
            loading,
            createData,
            updateData,
            data,
            createFormErrors,
            updateFormErrors,
            formErrors,
            form,
            v$,
            updateFile,
            submitForm,
            handleSelectionSubscribers
        }
    },
    components:{
        InputComponent,
        ButtonComponent,
        ErrorComponent,
        SendEmailFiles,
        SendEmailSubscribers
    }
});
</script>

<template>
    <form class="form">
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
            label="Titulo:"
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
            label="Contenido:"
            v-model="form.content"
            :errors="[
                ...v$.form.content.$errors,
                ...(formErrors?.content || [])
            ]"
            @blur="v$.form.content.$touch()"
        />

        <SendEmailFiles
            :attached_documents="form.attached_documents"
            :attached_images="form.attached_images"
            @update:attached_documents="(value) => updateFile('document', value)"
            @update:attached_images="(value) => updateFile('image', value)"
        />

        <SendEmailSubscribers
            :subscribers="form.subscribers"
            :newsletterId=" typeof newsletter === 'number' ? newsletter : newsletter.id"
            @update="(value) => handleSelectionSubscribers(value)"
        />

        <ErrorComponent v-if="formErrors" :errors="formErrors"/>

        <div class="form__buttons">
            <ButtonComponent
                type="button"
                :disabled="v$.$invalid"
                :loading="loadingCreate"
                @onclick="submitForm(true)"
            >
                Enviar ahora
            </ButtonComponent>

            <ButtonComponent
                type="submit"
                :disabled="v$.$invalid"
                :loading="loadingUpdate"
                @onclick="submitForm()"
            >
                Guardar
            </ButtonComponent>

            <!-- <ButtonComponent
                type="button"
                variant="outlined"
                :disabled="v$.$invalid"
            >
                Programar envío
            </ButtonComponent> -->
        </div>
    </form>
</template>


<style lang="scss" scoped>
@import "@/styles/variables.scss";

.form {
    & .form__buttons {
        display: flex;
        gap: $size-sm;
    }
}
</style>