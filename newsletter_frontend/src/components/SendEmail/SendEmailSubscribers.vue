<script lang="ts">
import { computed, defineComponent, onMounted, ref, watch } from 'vue';
import ButtonComponent from '../ButtonComponent.vue';
import ModalComponent from '../ModalComponent.vue';
import TableComponent from '../TableComponent.vue';
import { useFetch } from '../../composables/useFetch';

export default defineComponent({
    name: 'SendEmailSubscribers',
    props: {
        subscribers: {
            type: Array as () => number[],
            required: true
        },
        newsletterId: {
            type: Number,
            required: true
        }
    },
    emits: ['update'],
    setup(props, { emit }) {
        const { loading, error, next, results, fetchData } = useFetch(`/subscribers/?newsletters=${props.newsletterId}`);
        const showModal = ref<boolean>(false);
        const allSelected = ref<boolean>(props.subscribers.length == 0);
        const noneSelected = ref<boolean>(false);

        const dataColumns = [
            { label: 'Id', field: 'id' },
            { label: 'Correo electrónico', field: 'email'}
        ];

        const subscribersProps = computed<number[]>(() => props.subscribers);
        const selection = ref<number[]>(subscribersProps.value);
        const selectionTable = ref<boolean[]>([]);

        watch(() => props.subscribers, (newValue, oldValue) => {
            selection.value = newValue;
        });

        watch(() => selection.value, (newValue, oldValue) => {
            selectionTable.value = results.value.map(({ id }) => selection.value.includes(id));
        });

        watch(() => results.value, (newValue, oldValue) => {
            selectionTable.value = results.value.map(({ id }) => selection.value.includes(id));
        });

        const handleSelection = (index: number, value: boolean) => {
            console.log(index, value);
            console.log(selection.value);
            const id = results.value[index]["id"];
            const newIndex = selection.value.indexOf(id);
            console.log(id);
            allSelected.value = false;
            noneSelected.value = false;

            if (value && !selection.value.includes(id)) {
                selection.value = [...selection.value, id];
            }

            if (!value && selection.value.includes(id)) {
                selection.value.splice(newIndex, 1);
            }
            console.log(selection.value);
        }

        const handleAllSelection = () => {
            allSelected.value = true;
            noneSelected.value = false;
            selection.value = results.value.map(({ id }) => id);
        }

        const handleNoneSelection = () => {
            noneSelected.value = true;
            allSelected.value = false;
            selection.value = [];
        }

        const handleMainSelection = () => {
            if (allSelected.value) {
                handleNoneSelection();
            } else {
                handleAllSelection();
            }
        }

        const emitSelection = () => {
            showModal.value = false;
            emit('update', allSelected.value ? [] : selection.value);
        }

        return {
            results,
            dataColumns,
            selectionTable,
            showModal,
            allSelected,
            noneSelected,
            selection,
            subscribersProps,
            handleSelection,
            handleAllSelection,
            handleNoneSelection,
            emitSelection,
            handleMainSelection
        }
    },
    components: {
        ModalComponent,
        ButtonComponent,
        TableComponent
    }
});
</script>

<template>
    <div class="button-subscribers">
        <div class="subscribers__box" @click="showModal = true">
            <p v-if="subscribers.length === 0">Todos los suscriptores</p>
            <p v-else-if="subscribers.length === 1">{{ subscribers.length }} Suscriptor</p>
            <p v-else>{{ subscribers.length }} suscriptores</p>
        </div>

        <ModalComponent :show="showModal" @close="showModal = false">
            <template #header>
                <h2>Suscriptores</h2>
            </template>
            <template #body>
                <div class="button-subscribers__buttons">
                    <input id="main-checkbox" type="checkbox" :checked="allSelected" @input.prevent="handleMainSelection()">
                    <label for="main-checkbox">
                        <p v-if="!allSelected">Seleccionar todos</p>
                        <p v-if="allSelected">Quitar todos</p>
                    </label>
                </div>
                <TableComponent
                    :columns="dataColumns"
                    :data="results"
                    :checkboxes="selectionTable"
                    @onCheckbox="(index, value) => handleSelection(index, value)"
                ></TableComponent>
            </template>
            <template #footer>
                <ButtonComponent
                    v-if="!noneSelected"
                    color="tertiary"
                    variant="outlined"
                    @click="emitSelection"
                >
                    Guardar cambios
                </ButtonComponent>
            </template>
        </ModalComponent>
    </div>
</template>


<style lang="scss" scoped>
@import "@/styles/variables.scss";

.button-subscribers {
    background-color: $color-tertiary-50;
    box-shadow: $box-shadow-regular;
    border-radius: $button-border-radius;
    border: solid 1px $color-tertiary-100;
    padding: 0 24px;
    height: $button-height-large;
    margin-bottom: $size-sm;
    cursor: pointer;

    &:hover {
        border-color: $color-tertiary-200;
    }

    & .subscribers__box {
        display: flex;
        height: 100%;
        align-items: center;
        gap: $size-md;
    }

    & .button-subscribers__all {
        display: flex;
        gap: $size-sm;
    }

    & .button-subscribers__buttons {
        display: flex;
        flex-wrap: wrap;
        gap: $size-md;
    }
}

@keyframes spin {
    to {
        transform: rotate(360deg);
    }
}
</style>