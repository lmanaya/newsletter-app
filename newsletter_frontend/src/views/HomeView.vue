<script lang="ts">
import { computed, defineComponent, onMounted, ref } from 'vue';
import { useFetch } from '../composables/useFetch';
import NewsletterSubscription from '../components/Newsletter/NewsletterSubscription.vue';
import ButtonComponent from '../components/ButtonComponent.vue';

export default defineComponent({
    name: 'HomeView',
    setup() {
        const { loading, error, next, results, fetchData } = useFetch('/newsletters/');
        const prevResults = ref<[]>([]);
        const totalResults = computed<[]>(() => [
            ...prevResults.value,
            ...results.value
        ]);

        const loadMore = async () => {
            const prevData = results.value;
            await fetchData(next.value);
            prevResults.value = prevData;
        };

        const subscribedNewsletter = ref<number[]>([]);

        const onSubscribe = (newId: number) => {
            subscribedNewsletter.value = [ ...subscribedNewsletter.value, newId ];
        }

        return {
            next,
            totalResults,
            error,
            loading,
            subscribedNewsletter,
            onSubscribe,
            loadMore
        };
    },
    components: {
        NewsletterSubscription,
        ButtonComponent
    }
});
</script>

<template>
    <div class="container">
        <div class="home">
            <div class="home__header">
                <div>
                    <h1 class="home__title">¡No te pierdas nuestras novedades!</h1>
                    <p class="home__subtitle">Sé el primero en recibir contenido exclusivo,
                        noticias, y consejos directamente en tu bandeja de entrada.
                        📩 ¡Suscríbete ahora mismo!</p>
                </div>
                <img src="../assets/images/subscribe.svg" alt="">
            </div>

            <div v-if="totalResults" class="home__content">
                <NewsletterSubscription
                    v-for="newsletter in totalResults" :key="newsletter.id"
                    :newsletter="newsletter"
                    @subscribe="(value) => onSubscribe(value)"
                />
            </div>

            <div v-if="loading || next" class="home__footer">
                <p v-if="loading">Cargando..</p>
                <ButtonComponent
                    variant="ghost"
                    color="grey"
                    @click="loadMore()"
                >
                    Cargar más.
                </ButtonComponent>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import "@/styles/variables.scss";
@import "@/styles/mixins.scss";

.home {
    padding-bottom: $size-xl;

    & .home__header {
        padding: $size-xl 0;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: $size-lg;
        flex-direction: column;

        @include responsive(desktop) {
            flex-direction: row;
        }

        & div {
            max-width: 900px;
            width: 100%;
            flex-grow: 1;
        }

        & img {
            height: 100%;
            max-width: 300px;
            object-fit: contain;
            @include responsive(desktop) {
                max-width: 400px;
            }
        }
    }
    & .home__title {
        font-size: $text-xl;
        @include responsive(tablet) {
            font-size: $text-xxl;
        }
        @include responsive(desktop) {
            font-size: $text-xxxl;
        }
    }
    & .home__subtitle {
        font-size: $text-md;
        @include responsive(tablet) {
            font-size: $text-md;
        }
        @include responsive(desktop) {
            font-size: $text-md;
        }
    }

    & .home__footer {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: $size-md;
    }
}

.home__content {
    display: flex;
    flex-wrap: wrap;
    width: 100%
}
</style>