<script lang="ts">
import { defineComponent } from 'vue';
import { useFetch } from '../composables/useFetch';

export default defineComponent({
    name: 'HomeView',
    setup() {
        const { data, error, loading } = useFetch('/newsletters/');
        return { data, error, loading };
    }
});
</script>

<template>
    <div class="container">
        <p>Home view</p>
        <p v-if="loading">Cargando..</p>
        <div v-if="data">
            <p>{{ data }}</p>
        </div>
    </div>
</template>

<style></style>