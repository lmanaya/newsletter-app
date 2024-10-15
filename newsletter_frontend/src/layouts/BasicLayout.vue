<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'BasicLayout',
    setup() {}
});
</script>

<template>
    <div class="container">
        <nav class="navbar">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/login">Login</a></li>
            </ul>
        </nav>
        <router-view></router-view>
    </div>
</template>

<style></style>