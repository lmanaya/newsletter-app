<script lang="ts">
import { defineComponent } from 'vue';
import ButtonComponent from './ButtonComponent.vue';

export default defineComponent({
    name: 'TableComponent',
    props: {
        columns: {
            type: Array as () => {field: string, label: string}[],
            required: true,
        },
        data: {
            type: Array as () => Record<string, any>[],
            required: true
        },
        links: {
            type: Array as () => {path: Record<string, any>, label: string}[],
            required: false
        }
    },
    emits: ["page"],
    setup(props, { emit }) {

        const getFieldValue = (obj: Record<string, any>, field: string) => {
            return field.split('.').reduce((o, key) => (o ? o[key] : null), obj);
        }

        return { getFieldValue, emit }
    },
    components: {
        ButtonComponent
    }
});
</script>

<template>
    <div class="table-container">
        <table class="responsive-table">
            <thead>
                <tr>
                    <th v-for="(column, index) in columns" :key="index">
                        {{ column.label }}
                    </th>
                    <th v-if="links"></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(row, rowIndex) in data" :key="rowIndex">
                    <td v-for="(column, colIndex) in columns" :key="colIndex">
                        {{ getFieldValue(row, column.field) }}
                    </td>
                    <td v-if="links">
                        <ButtonComponent :to="links[rowIndex].path" variant="link">
                            {{ links[rowIndex].label }}
                        </ButtonComponent>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped>
.table-container {
    width: 100%;
    overflow-x: auto;
}

.responsive-table {
    width: 100%;
    border-collapse: collapse;
}

.responsive-table th, .responsive-table td {
    border: 1px solid #ddd;
    padding: 8px;
}

.responsive-table th {
    background-color: #f4f4f4;
    text-align: left;
}
</style>