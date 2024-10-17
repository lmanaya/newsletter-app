<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useFetch } from '../composables/useFetch';
import ButtonComponent from '../components/ButtonComponent.vue';
import ModalComponent from '../components/ModalComponent.vue';
import NewsletterComponent from '../components/NewsletterComponent.vue';
import TableComponent from '../components/TableComponent.vue';

export default defineComponent({
    name: 'NeswlettersView',
    setup() {
        const { results, error, loading, fetchData } = useFetch('/newsletters/');
        const showModal = ref<Boolean>(false);

        const onCompleteForm = () => {
            showModal.value = false;
            fetchData();
        };

        const dataColumns = [
            { label: 'Id', field: 'id' },
            { label: 'Nombre', field: 'name' },
            { label: 'Descripción', field: 'description'},
            { label: 'CTA', field: 'call_to_action_text'}
        ];

        return {
            results,
            dataColumns,
            error,
            loading,
            showModal,
            onCompleteForm
        };
    },
    components: {
        ButtonComponent,
        ModalComponent,
        NewsletterComponent,
        TableComponent
    }
});
</script>

<template>
    <div class="newsletters">
        <div class="section">
            <ButtonComponent @click="() => (showModal = true)">Registrar newsletter</ButtonComponent>
        </div>

        <div class="section">
            <p v-if="results.length == 0">No hay newsletters por el momento.</p>
            <div v-else class="newsletters__resuls">
                <h1 class="">Resultados</h1>
                <TableComponent
                    :columns="dataColumns"
                    :data="results"
                ></TableComponent>
            </div>
        </div>

        <ModalComponent :show="showModal" @close="() => (showModal = false)">
            <template #header>
                <h2>Nuevo newsletter</h2>
            </template>
            <template #body>
                <NewsletterComponent @complete="() => onCompleteForm()" ></NewsletterComponent>
            </template>
        </ModalComponent>
    </div>
</template>

<style lang="scss" scoped>
@import "@/styles/variables.scss";
.newsletters {
    padding-top: $size-lg;

    & .newsletters__resuls h1 {
        margin-bottom: $size-md;
        font-size: $text-lg;
    }
}
</style>