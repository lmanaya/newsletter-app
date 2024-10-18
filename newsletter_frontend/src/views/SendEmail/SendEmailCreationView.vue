<script lang="ts">
import { computed, defineComponent, onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import SendEmailForm from '../../components/SendEmail/SendEmailForm.vue';
import { useApiService } from '../../composables/useApiService';
import { getNewsletter as getNewsletterApi } from '../../services/newsletterService';
import { Newsletter } from '../../types/newsletter';

export default defineComponent({
    name: 'SendEmailCreationView',
    setup() {
        const route = useRoute();
        const router = useRouter();
        const newsletterId = computed(() => route.params.id);
        const newsletter = ref<Newsletter | null>(null);

        const {
            data: dataNewsletter,
            execute: getNewsletter
        } = useApiService(() => getNewsletterApi(newsletterId.value as string));

        const redirectToEmail = async (id: number) => {
            router.push({ name: 'EmailDetail', params: { id } });
        };

        const redirectToEmailList = async () => {
            router.push({ name: 'EmailList' });
        };

        onMounted(async () => {
            await getNewsletter();

            if (!dataNewsletter.value) {
                router.push({ name: 'NewsletterList' });
            }

            newsletter.value = dataNewsletter.value;
        });

        return {
            newsletter,
            redirectToEmail,
            redirectToEmailList
        }
    },
    components: {
        SendEmailForm
    }
});
</script>

<template>
    <div v-if="newsletter">
        <h1>{{ newsletter.name }}</h1>
        <p>{{ newsletter.description }}</p>

        <div class="card">
            <h2>Crear correo</h2>
            <SendEmailForm
                action="create"
                :newsletter="newsletter.id"
                @created="redirectToEmailList"
                @sended="(id) => redirectToEmail(id)"
            />
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import "@/styles/variables.scss";

.card {
    box-shadow: $box-shadow-card;
    padding: $size-lg;
    margin: $size-md 0;
}
</style>