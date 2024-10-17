<script lang="ts">
import { computed, defineComponent } from 'vue';
import { PaginatedResponse } from '../types/api';

export default defineComponent({
    name: 'TableComponent',
    props: {
        columns: {
            type: Array,
            required: true,
        },
        data: {
            type: Array,
            required: true
        }
    },
    emits: ["page"],
    setup(props, { emit }) {
        return { emit }
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
                </tr>
            </thead>
            <tbody>
                <tr v-for="(row, rowIndex) in data" :key="rowIndex">
                    <td v-for="(column, colIndex) in columns" :key="colIndex">
                        {{ row[column.field] }}
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