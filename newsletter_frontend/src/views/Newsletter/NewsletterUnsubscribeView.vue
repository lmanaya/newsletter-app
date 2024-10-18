<script lang="ts">
import { computed, defineComponent, onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { UnsubscribePayload } from '../../types/newsletter';
import { useApiService } from '../../composables/useApiService';
import { getNewsletter, unsubscribe } from '../../services/newsletterService';
import ButtonComponent from '../../components/ButtonComponent.vue';
import FatalComponent from '../../components/FatalComponent.vue';

export default defineComponent({
    name: 'NewsletterUnsubscribeView',
    setup() {
        const route = useRoute();
        const router = useRouter();

        const queryToken = computed(() => route.query.token);
        const queryNewsletter = computed(() => route.query.newsletter);

        const newsletter = ref<number | null>(null);
        const successForm = ref<Boolean>(false);
        const errorForm = ref<Boolean>(false);

        const form = computed<UnsubscribePayload>(() => {
            const payload: UnsubscribePayload = { unsubscribe_token: queryToken.value as string };
            if (newsletter.value) {
                payload.newsletter = newsletter.value;
            }
            return payload;
        });

        const {
            loading: validating,
            data,
            formErrors: validateErrors,
            execute: validateNesletter
        } = useApiService(() => getNewsletter(queryNewsletter.value as string));

        const {
            loading,
            formErrors,
            execute: unsubscribeNewsletter
        } = useApiService(() => unsubscribe(form.value));

        const abcdc = async (allNewsletters: Boolean = false) => {
            newsletter.value = allNewsletters ? null : parseInt(queryNewsletter.value as string);
            await unsubscribeNewsletter();
            successForm.value = !formErrors.value;
            errorForm.value = !!formErrors.value;
        };

        onMounted(async () => {
            if (!queryToken.value || !queryNewsletter.value) {
                return router.push({ name: 'Home' });
            }
            await validateNesletter();
            errorForm.value = !!validateErrors.value;
        });

        return {
            validating,
            validateErrors,
            loading,
            formErrors,
            newsletter,
            data,
            successForm,
            errorForm,
            abcdc
        }
    },
    components: {
        ButtonComponent,
        FatalComponent
    }
})
</script>

<template>
    <div v-if="data" class="container">
        <div v-if="!successForm" class="unsubscribe">
            <h1>¿Estas seguro de desuscribirte?</h1>
            <div class="unsubscribe__buttons">
                <ButtonComponent
                    :loading="loading && newsletter"
                    color="grey"
                    @onclick="() => (abcdc())"
                >
                    Sí, desuscribirme de <strong>"{{ data.name }}"</strong>
                </ButtonComponent>
                <ButtonComponent
                    :loading="loading && !newsletter"
                    color="grey"
                    variant="ghost"
                    size="small"
                    @onclick="() => (abcdc(true))"
                >
                    Desuscribirme de todos los newsletters
                </ButtonComponent>
                <ButtonComponent
                    color="primary"
                    variant="ghost"
                    size="small"
                    :to="{ name: 'Home' }"
                >
                    Mejor no, sigo como estoy
                </ButtonComponent>
            </div>
        </div>
        <div v-else class="unsubscribe__completed">
            <img src="../../assets/images/unsubscribe.svg" alt="">
            <div class="unsubscribe__text">
                <p>Lo sentimos por verte partir. ¡Cuídate y hasta la próxima! 🌟</p>
                <br>
                <ButtonComponent color="secondary" :to="{ name: 'Home' }">Ir al inicio</ButtonComponent>
            </div>
        </div>

        <FatalComponent v-if="errorForm" @close="() => (errorForm = false)" />
    </div>
</template>

<style lang="scss" scoped>
@import "@/styles/variables.scss";

.unsubscribe {
    text-align: center;
    max-width: 400px;
    margin: auto;

    & .unsubscribe__buttons {
        display: flex;
        flex-direction: column;
        gap: $size-sm;
        align-items: center;
        padding: $size-lg 0;
    }
}

.unsubscribe__completed {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    gap: $size-md;

    & img {
        max-width: 200px;
    }

    & .unsubscribe__text {
        display: flex;
        flex-direction: column;
        & p {
            max-width: 300px;
        }
    }
}
</style>