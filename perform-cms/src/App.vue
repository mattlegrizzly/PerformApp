<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import '@/assets/main.css'

import { onMounted } from 'vue';
onMounted(() => {
  console.log('Get me')
})
</script>

<template>

  <RouterView />
</template>

<style>

</style>
