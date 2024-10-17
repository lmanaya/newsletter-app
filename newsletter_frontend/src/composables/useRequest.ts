import api from '@/services/api';
import { ref } from 'vue';
import { useForm } from './useForm';

export const useRequest = (form: any) => {
    const loading = ref(false);

    const { formErrors, setFormErrors } = useForm(form);

    const post = async (url: string, payload: any) => {
        loading.value = true;
        try {
            const response = await api.post(url, payload);
            return response;
        } catch (error: any) {
            setFormErrors(error.response.data);
            return error.response;
        } finally {
            loading.value = false;
        }
    };

    const get = async (url: string) => {
        loading.value = true;
        try {
            const response = await api.get(url);
            return response;
        } catch (error: any) {
            setFormErrors(error.response.data);
            return error.response;
        } finally {
            loading.value = false;
        }
    };

    return {
        loading,
        formErrors,
        post,
        get
    };
}
