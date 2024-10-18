<script lang="ts">
import { defineComponent, ref } from 'vue';
import ButtonComponent from './ButtonComponent.vue';

export default defineComponent({
    name: 'TabMenuComponent',
    props: {
        tabs: {
            type: Array as () => { name: String, label: any}[],
            required: true
        },
        defaultTab: {
            type: String,
            default: null
        },
        color: {
            type: String,
            default: "primary"
        }
    },
    emits: ['selectTab'],
    setup(props, { emit }) {
        const activeTab = ref(props.defaultTab ? props.defaultTab : props.tabs[0].name);

        const selectTab = (tabName: String) => {
            emit('selectTab', tabName);
            activeTab.value = tabName;
        };

        const isActive = (tabName: String) => {
            return activeTab.value === tabName;
        };

        return {
            activeTab,
            selectTab,
            isActive,
        }
    },
    components: {
        ButtonComponent
    }
});
</script>

<template>
    <div>
        <div class="tabs">
            <ButtonComponent
                v-for="(tab, index) in tabs"
                :key="index"
                type="tab"
                :color=" isActive(tab.name) ? color : 'grey'"
                :variant=" isActive(tab.name) ? 'filled' : 'ghost'"
                @onclick="selectTab(tab.name)"
            >
                {{ tab.label }}
            </ButtonComponent>
        </div>
        <div class="tab-content">
            <slot :name="activeTab"></slot>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import "@/styles/variables.scss";
.tabs {
    display: flex;
}

.tab-content {
    padding: $size-md;
    border: $color-background;
    box-shadow: $box-shadow-card;
}
</style>