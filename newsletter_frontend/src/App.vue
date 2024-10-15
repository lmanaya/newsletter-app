<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'App',
    setup() {}
});
</script>

<template>
  <div id="app">
    <nav class="navbar">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/login">Login</a></li>
      </ul>
    </nav>
    <router-view />
  </div>
</template>