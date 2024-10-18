<script lang="ts">
import { computed, defineComponent, onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import { useApiService } from '../../composables/useApiService';
import { NewsletterEmail } from '../../types/sendEmails';
import { getNewsletterEmail } from '../../services/sendEmailService';
import SendEmailForm from '../../components/SendEmail/SendEmailForm.vue';

export default defineComponent({
    name: 'SendEmailDetailView',
    setup() {
        const route = useRoute();
        const router = useRouter();
        const newsletterEmailId = computed(() => route.params.id);
        const newsletterEmail = ref<NewsletterEmail | null>(null);

        const {
            data,
            execute
        } = useApiService(() => getNewsletterEmail(newsletterEmailId.value as string));

        const redirectToEmailList = () => {
            router.push({ name: 'EmailList' });
        };

        onMounted(async () => {
            await execute();

            if (!data.value) {
                router.push({ name: 'EmailList' });
            }

            newsletterEmail.value = data.value;
        });

        return {
            newsletterEmail,
            redirectToEmailList
        }
    },
    components: {
        SendEmailForm
    }
})
</script>

<template>
    <div v-if="newsletterEmail">
        <div class="section">
            <h1>Correo electrónico</h1>
            <h2 v-if="typeof newsletterEmail.newsletter === 'object'" >
                {{ newsletterEmail.newsletter.name }}
            </h2>
        </div>

        <div v-if="newsletterEmail.status === 'sended' ">
            <p>Email enviado</p>
        </div>
        <div>
            <SendEmailForm
                action="update"
                :newsletter="newsletterEmail.newsletter"
                :newsletterEmail="newsletterEmail"
                @updated="redirectToEmailList"
                @sended="redirectToEmailList"
            />
        </div>
    </div>
</template>

<style lang="scss" scoped>

</style>