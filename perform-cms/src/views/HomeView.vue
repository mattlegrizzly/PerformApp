<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref, onMounted } from 'vue';
import axios from 'axios'

const user = ref({
  username: '',
  email: '',
  size: 0,
  age: 0,
  gender: 'male',
  profile_picture: '',
  sports_user: [],
  user_injuries: [],
  users_wellness: []
})
onMounted(() => {
  axios.get('').then((response : any) => (user.value = response))
});
</script>

<template>
  <div class="mainWrapper">
    <h1>Bienvenue {{ user.username === '' ? 'Inconnu': user.username }}</h1>
  </div>
  <RouterView />
</template>
