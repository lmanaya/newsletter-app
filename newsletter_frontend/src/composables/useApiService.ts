
import { AxiosResponse } from 'axios';
import { ref } from 'vue';
import { useForm } from './useForm';

export const useApiService = (
    apiFunction: () => Promise<AxiosResponse>,
    form: Record<string, any> | undefined = undefined
) => {
    const data = ref(null);
    const loading = ref(false);

    const { formErrors, setFormErrors } = useForm(form);

    const execute = async () => {
        loading.value = true;
        setFormErrors(null);

        try {
            const result = await apiFunction();
            data.value = result.data;
            return true;
        } catch (error: any) {
            setFormErrors(error.response);
            return false;
        } finally {
            loading.value = false;
        }
    };

    return {
        loading,
        data,
        formErrors,
        execute,
    };
};
