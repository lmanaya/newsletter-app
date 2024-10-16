import { ref, onMounted, watch } from 'vue';

export const useForm = (form: any) => {
    type Error = Partial<typeof form> & { non_field_errors?: string[] };
    const formErrors = ref<Error | null>(null);

    const setFormErrors = (errors: Error | null) => {
        formErrors.value = errors;
    }

    onMounted(() => {
        Object.keys(form).forEach((field) => {
            watch(() => form[field as keyof typeof form], (newValue, oldValue) => {
                if (newValue !== oldValue && formErrors.value) {
                    delete formErrors.value[field];
                    delete formErrors.value.non_field_errors;
                }
            });
        });
    });

    return { formErrors, setFormErrors };
}
