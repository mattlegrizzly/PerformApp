<script setup lang="ts">
import NavMenu from '../../components/NavMenu.vue'
import { ref, onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { post } from '@/lib/callApi'

const exercises = ref({})

</script>
<style lang=""></style>

<template lang="">
  <NavMenu />

  <div class="mainWrapper">
    <h1>Ajouter un Exercise</h1>
  </div>
  <RouterView />
</template>
