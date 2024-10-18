<script lang="ts">
import { defineComponent, ref, computed } from 'vue';
import { useFetch } from '../../composables/useFetch';
import ButtonComponent from '../../components/ButtonComponent.vue';
import ModalComponent from '../../components/ModalComponent.vue';
import NewsletterForm from '../../components/Newsletter/NewsletterForm.vue';
import TableComponent from '../../components/TableComponent.vue';

export default defineComponent({
    name: 'NewsletterListView',
    setup() {
        const { results, error, loading, fetchData } = useFetch('/newsletters/');
        const showModal = ref<boolean>(false);

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

        const links = computed(() => results.value.map((value) => {
            return {
                path: { name: 'EmailCreation', params: { id: value["id"] }},
                label: "Crear email"
            }
        }))

        return {
            results,
            dataColumns,
            links,
            error,
            loading,
            showModal,
            onCompleteForm
        };
    },
    components: {
        ButtonComponent,
        ModalComponent,
        NewsletterForm,
        TableComponent
    }
});
</script>

<template>
    <div class="newsletters">
        <div class="section">
            <ButtonComponent @onclick="() => (showModal = true)">Registrar newsletter</ButtonComponent>
        </div>

        <div class="section">
            <p v-if="results.length == 0">No hay newsletters por el momento.</p>
            <div v-else class="newsletters__resuls">
                <h1 class="">Resultados</h1>
                <TableComponent
                    :columns="dataColumns"
                    :data="results"
                    :links="links"
                ></TableComponent>
            </div>
        </div>

        <ModalComponent :show="showModal" @close="() => (showModal = false)">
            <template #header>
                <h2>Nuevo newsletter</h2>
            </template>
            <template #body>
                <NewsletterForm @complete="() => onCompleteForm()" ></NewsletterForm>
            </template>
        </ModalComponent>
    </div>
</template>

<style lang="scss" scoped>
@import "@/styles/variables.scss";
.newsletters {
    & .newsletters__resuls h1 {
        margin-bottom: $size-md;
        font-size: $text-lg;
    }
}
</style>