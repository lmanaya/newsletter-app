<script lang="ts">
import { defineComponent, ref } from 'vue'
import TabMenuComponent from '../../components/TabMenuComponent.vue'
import { useApiService } from '../../composables/useApiService';
import { fetchDocuments, fetchImages } from '../../services/sendEmailsServiceService';

export default defineComponent({
    name: 'SendEmailDocumentsView',
    setup() {
        const tabs = [
            { name: 'documents', label: 'Documentos' },
            { name: 'images', label: 'Imágenes' }
        ];

        const query = ref<String | null>(null);

        const { data: documentsData, execute: getDocuments } = useApiService(() => fetchDocuments(query.value));
        const { data: imagesData, execute: getImages } = useApiService(() => fetchImages(query.value));

        const selectTab = async (value: String) => {
            if (value == 'documents') {
                await getDocuments();
            } else {
                await getImages();
            }
        };

        return {
            tabs,
            documentsData,
            imagesData,
            selectTab,
        }
    },
    components: {
        TabMenuComponent
    }
})
</script>

<template>
    <div>
        <div class="section">
            <h1>Archivos</h1>
        </div>
        <TabMenuComponent :tabs="tabs" default-tab="documents" @selectTab="(value) => selectTab(value)">
            <template v-slot:documents>
                {{ documentsData }}
            </template>
            <template v-slot:images>
                {{ imagesData }}
            </template>
        </TabMenuComponent>
    </div>
</template>

<style lang="scss" scoped>

</style>