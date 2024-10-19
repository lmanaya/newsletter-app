<script lang="ts">
import { computed, defineComponent, onMounted, ref } from 'vue';
import { useApiService } from '../../composables/useApiService';
import {
    createImage as createImageApi,
    createDocument as createDocumentApi,
    updateImage as updateImageApi,
    updateDocument as updateDocumentApi,
    getImage as getImageApi,
    getDocument as getDocumentApi
} from '../../services/sendEmailService';
import ButtonComponent from '../ButtonComponent.vue';
import InputComponent from '../InputComponent.vue';
import ModalComponent from '../ModalComponent.vue';
import FatalComponent from '../FatalComponent.vue';

export default defineComponent({
    name: 'SendEmailFiles',
    props: {
        attached_documents: {
            type: Array as () => number[],
            required: true
        },
        attached_images: {
            type: Array as () => number[],
            required: true
        }
    },
    emits: ['update:attached_documents', 'update:attached_images'],
    setup(props, { emit }) {
        const selectedFile = ref<File | null>(null);
        const selectedFormData = ref<FormData | null>(null);

        const id = ref<number>();
        const name = ref<string>();
        const loading = ref<boolean>(false);
        const error = ref<boolean>(false);

        const isPdf = computed<boolean>(
            () => selectedFile.value?.type === 'application/pdf' || props.attached_documents.length > 0
        );
        const isFile = computed<boolean>(
            () => selectedFile.value !== null || props.attached_documents.length > 0 || props.attached_images.length > 0
        );

        const {
            data: createdDoc,
            execute: createDocument
        } = useApiService(() => createDocumentApi(selectedFormData.value));
        const {
            data: createdImg,
            execute: createImage
        } = useApiService(() => createImageApi(selectedFormData.value));

        const {
            execute: updateDocument
        } = useApiService(() => updateDocumentApi(id.value, selectedFormData.value));
        const {
            execute: updateImage
        } = useApiService(() => updateImageApi(id.value, selectedFormData.value));

        const {
            data: document,
            execute: getDocument
        } = useApiService(() => getDocumentApi(id.value));
        const {
            data: image,
            execute: getImage
        } = useApiService(() => getImageApi(id.value));

        const handleFileUpload = async (event: Event) => {
            loading.value = true;

            const target = event.target as HTMLInputElement;
            if (target.files && target.files[0]) {
                selectedFile.value = target.files[0];
                name.value = selectedFile.value.name;

                const formData = new FormData();
                formData.append('file', selectedFile.value);
                formData.append('name', name.value);

                selectedFormData.value = formData;
                if (selectedFile.value.type === 'application/pdf') {
                    if (props.attached_documents.length === 0) {
                        error.value = !(await createDocument());
                        emit('update:attached_documents', createdDoc.value.id);
                    } else {
                        id.value = props.attached_documents[0];
                        error.value = !(await updateDocument());
                        emit('update:attached_documents', id.value);
                    }
                }

                if (selectedFile.value.type === 'image/png') {
                    if (props.attached_images.length === 0) {
                        error.value = !(await createImage());
                        emit('update:attached_images', createdImg.value.id);
                    } else {
                        id.value = props.attached_images[0];
                        error.value = !(await updateImage());
                        emit('update:attached_images', id.value);
                    }
                }
            }

            loading.value = false;
        };

        onMounted(async () => {
            for (let i = 0; i < props.attached_documents.length; i++) {
                id.value = props.attached_documents[i];
                error.value = !(await getDocument());
                name.value = document.value.name;
            }
            for (let i = 0; i < props.attached_images.length; i++) {
                id.value = props.attached_documents[i];
                error.value = !(await getImage());
                name.value = image.value.name;
            }
        });

        return {
            loading,
            name,
            isPdf,
            isFile,
            error,
            handleFileUpload
        }
    },
    components: {
        ModalComponent,
        InputComponent,
        ButtonComponent,
        FatalComponent
    }
});
</script>

<template>
    <div :class="`input-file${isFile ? ' input-file--with-file': ''}`">
        <input
            id="attached_file"
            type="file"
            @change="handleFileUpload"
            accept=".png, .pdf"
            :disabled="loading"
        >
        <label for="attached_file">
            <div v-if="!isFile" class="input-file__box">
                <img src="../../assets/icons/clip.svg" alt="upload file">
                <p>Adjuntar un archivo .Pdf o .png</p>
            </div>
            <div v-else-if="!loading" class="input-file__box">
                <img v-if="isPdf" src="../../assets/icons/pdf-file.svg" alt="uploaded file">
                <img v-else src="../../assets/icons/png-file.svg" alt="uploaded file">
                <p>{{ name }}</p>
            </div>
            <div v-else class="input-file__box">
                <div class="input-file__box--loading"></div>
                <div>Subiendo archivo...</div>
            </div>
        </label>

        <FatalComponent v-if="error"></FatalComponent>
    </div>
</template>


<style lang="scss" scoped>
@import "@/styles/variables.scss";

.input-file {
    background-color: $color-grey-50;
    box-shadow: $box-shadow-regular;
    border-radius: $button-border-radius;
    border: solid 1px $color-grey-200;
    padding: 0 24px;
    height: $button-height-large;
    margin-bottom: $size-sm;

    &:hover {
        border-color: $color-grey-300;
    }

    &.input-file--with-file {
        background-color: $color-secondary-50;
        border-color: $color-secondary-100;

        &:hover {
            border-color: $color-secondary-200;
        }
    }

    & label {
        display: block;
        height: 100%;
        &:hover {
            cursor: pointer;
        }
    }

    & input {
        position: absolute;
        z-index: -1;
        opacity: 0;
    }

    & img {
        width: 30px;
        height: 30px;
    }

    & .input-file__box {
        display: flex;
        height: 100%;
        align-items: center;
        gap: $size-md;

        &.input-file__box--loading {
            margin-left: 10px;
            border: 2px solid rgba(0, 0, 0, 0.1);
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
    }
}

@keyframes spin {
    to {
        transform: rotate(360deg); /* Gira el círculo completamente */
    }
}
</style>