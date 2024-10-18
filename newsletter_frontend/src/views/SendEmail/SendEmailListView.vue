<script lang="ts">
import { defineComponent, ref, computed, onMounted } from 'vue';
import ModalComponent from '../../components/ModalComponent.vue';
import NewsletterForm from '../../components/Newsletter/NewsletterForm.vue';
import TableComponent from '../../components/TableComponent.vue';
import { useApiService } from '../../composables/useApiService';
import { getSendEmails } from '../../services/sendEmailService';
import ErrorComponent from '../../components/ErrorComponent.vue';
import { PaginatedResponse } from '../../types/api';

export default defineComponent({
    name: 'SendEmailListView',
    setup() {
        const query = ref<string | null>(null);

        const { loading, data, formErrors, execute } = useApiService(() => getSendEmails(query?.value));

        const results = computed(() => data.value ? (data.value as PaginatedResponse).results : []);

        const dataColumns = [
            { label: 'Id', field: 'id' },
            { label: 'Asunto', field: 'subject' },
            { label: 'Estado', field: 'status_display' },
            { label: 'Newsletter', field: 'newsletter.name' },
        ];

        const links = computed<{path: Record<string, any>, label: string}[]>(() => results.value.map((value) => {
            return {
                path: { name: 'EmailDetail', params: { id: value["id"] }},
                label: "Ver email"
            }
        }));

        onMounted(async () => {
            await execute();
        });

        return {
            results,
            dataColumns,
            links,
            formErrors,
            loading
        };
    },
    components: {
        ModalComponent,
        NewsletterForm,
        TableComponent,
        ErrorComponent
    }
});
</script>

<template>
    <div class="newsletter-emails">
        <div class="section">
            <h1>Correos electrónicos</h1>
        </div>
        <div class="section">
            <ErrorComponent v-if="formErrors" :errors="formErrors"/>
            <p v-if="results.length == 0">No hay correos electrónicos por el momento.</p>
            <div v-else class="newsletter-emails__resuls">
                <h1 class="">Resultados</h1>
                <TableComponent
                    :columns="dataColumns"
                    :data="results"
                    :links="links"
                ></TableComponent>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import "@/styles/variables.scss";
.newsletter-emails {
    & .newsletter-emails__resuls h1 {
        margin-bottom: $size-md;
        font-size: $text-lg;
    }
}
</style>