import { ref, computed, onMounted } from 'vue';
import { useStore } from 'vuex';
import api from '@/services/api';
import { ErrorResponse, PaginatedResponse } from '@/types/api';

export const useFetch = (url: string) => {
    const data = ref<PaginatedResponse | null>(null);
    const error = ref<ErrorResponse | null>(null);
    const store = useStore();

    const loading = computed(() => store.state.loading);

    const fetchData = async () => {
        store.dispatch('loading', true);
        try {
            const response = await api.get(url);
            data.value = response.data;
        } catch (error: any) {
            console.error('Error fetching data', error);
            error.value = error.response;
        } finally {
            store.dispatch('loading', false);
        }
    };

    onMounted(() => {
        fetchData();
    });

    return { loading, error, data, fetchData };
}
