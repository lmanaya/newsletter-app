<script lang="ts">
import { defineComponent, computed, ref } from 'vue';

export default defineComponent({
    name: 'UploadFile',
    props: {
        attached_documents: {
            type: Array,
            required: true
        },
        attached_images: {
            type: Array,
            required: true
        },
    },
    emits: ['updateImage', 'updateDocument'],
    setup(props, { emit }) {
        const selectedFile = ref<File | null>(null);

        const handleFileChange = (event: Event) => {
            const target = event.target as HTMLInputElement;
            if (target.files && target.files.length > 0) {
                selectedFile.value = target.files[0]; // Asignar el archivo seleccionado
            }
        };

        const uploadFile = async () => {
            if (!selectedFile.value) {
                uploadMessage.value = 'Por favor selecciona un archivo.';
                return;
            }

            const formData = new FormData();
            formData.append('file', selectedFile.value); // Agregar el archivo al FormData

            try {
                const response = await axios.post('/api/upload/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data', // Cabecera necesaria para subir archivos
                },
                });

                if (response.status === 200) {
                uploadMessage.value = 'Archivo subido con éxito.';
                } else {
                uploadMessage.value = 'Error al subir el archivo.';
                }
            } catch (error) {
                console.error('Error al subir el archivo:', error);
                uploadMessage.value = 'Error al subir el archivo.';
            }
        };

        return {
        }
    },
});
</script>

<template>
    <div>
        <input type="file" accept=".jpg .pdf" />
    </div>
</template>


<style lang="scss" scoped>
@import "@/styles/variables.scss";

</style>