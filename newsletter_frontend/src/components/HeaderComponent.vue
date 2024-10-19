<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useAuth } from '../composables/useAuth';
import ButtonComponent from './ButtonComponent.vue';
import { RouteLocationRaw } from 'vue-router';

export interface Link {
    path: RouteLocationRaw;
    name: string;
}

export default defineComponent({
    name: 'HeaderComponent',
    props: {
        links: {
            type: Array as () => Link[],
            default: []
        }
    },
    setup() {
        const {
            isAuthenticated,
            logout
        } = useAuth();

        const showMenu = ref<Boolean>(false);

        return {
            isAuthenticated,
            showMenu,
            logout
        }
    },
    components: {
        ButtonComponent
    }
});
</script>

<template>
    <div class="header">
        <div class="header__container">
            <slot name="main"></slot>
            <div class="header__links">
                <nav class="header__navbar">
                    <router-link v-for="(link, index) in links" :key="index" :to="link.path">{{ link.name }}</router-link>
                </nav>

                <ButtonComponent
                    v-if="isAuthenticated"
                    color="alarm"
                    variant="ghost"
                    @onclick="logout"
                >
                    Cerrar sesión
                </ButtonComponent>
                <router-link :to="{ name: 'Login' }" v-else >
                    <ButtonComponent color="primary" :preventDefault="false">
                        Ingresar
                    </ButtonComponent>
                </router-link>
                <ButtonComponent
                    v-if="links.length > 0"
                    class="header-mobile__menu"
                    color="grey"
                    variant="ghost"
                    @onclick="() => (showMenu = true)"
                >
                    <img src="../assets/icons/menu.svg" alt="" width="20">
                </ButtonComponent>
            </div>
        </div>

        <div v-if="showMenu && links.length > 0" class="header-mobile">
            <div class="header-mobile__close">
                <ButtonComponent color="grey" variant="ghost" @onclick="() => (showMenu = false)">
                    <img src="../assets/icons/cross.svg" alt="" width="20">
                </ButtonComponent>
            </div>
            <div class="header-mobile__navbar">
                <router-link
                    v-for="(link, index) in links"
                    :key="index"
                    :to="link.path"
                    @click="() => (showMenu = false)"
                >{{ link.name }}</router-link>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import "@/styles/variables.scss";
@import "@/styles/mixins.scss";

.header {
    display: flex;
    background-color: $color-background;
    border-bottom: solid 3px $color-grey-100;

    & .header__links {
        flex-grow: 1;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        flex-wrap: nowrap;
        gap: $size-xs;

        @include responsive(desktop) {
            gap: $size-md;
            justify-content: space-between;
        }

        & .header__navbar {
            display: none;

            @include responsive(desktop) {
                display: flex;
                flex-grow: 1;
                justify-content: center;
                align-items: center;
                flex-wrap: nowrap;
                gap: $size-md;
                text-transform: uppercase;
            }

            & a {
                margin-right: $size-md;
                padding: 0 $size-xs;

                &:hover {
                    border-bottom: solid 1px;
                }
            }
        }
    }
}

.header__container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: nowrap;
    max-width: $breakpoint-desktop;
    margin: auto;
    width: 100%;
    padding: 0px $size-md;
}

.header-mobile {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: $color-white;
    z-index: 1000;

    & .header-mobile__navbar {
        padding: $size-xl;
        display: block;
        text-transform: uppercase;
        display: flex;
        flex-direction: column;
        gap: $size-sm;

        & a {
            &:hover {
                border-bottom: solid 1px;
            }
        }
    }

    & .header-mobile__close {
        display: flex;
        justify-content: flex-end;
        padding: $size-sm $size-xl;
    }
}

.header-mobile__menu {
    @include responsive(desktop) {
        display: none;
    }
}
</style>