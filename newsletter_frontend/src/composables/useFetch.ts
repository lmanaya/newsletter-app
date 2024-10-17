import { ref, computed, onMounted } from 'vue';
import { useStore } from 'vuex';
import api from '@/services/api';
import { ErrorResponse, PaginatedResponse } from '@/types/api';

export const useFetch = (url: String) => {
    const data = ref<PaginatedResponse | null>(null);
    const error = ref<ErrorResponse | null>(null);
    const store = useStore();

    const loading = computed(() => store.state.loading);
    const count = computed<number>(() => data.value?.count ?? 0);
    const previous = computed<String | null>(() => data.value?.previous ? data.value?.previous.split("?")[1] : null);
    const next = computed<String | null>(() => data.value?.next ? data.value?.next.split("?")[1] : null);
    const results = computed<[]>(() => data.value?.results ?? []);

    const fetchData = async (query: String | null = null) => {
        store.dispatch('loading', true);
        try {
            const response = await api.get(`${url}${query ? "?" + query : ""}`);
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

    return {
        loading,
        error,
        count,
        next,
        previous,
        results,
        fetchData
    };
}
