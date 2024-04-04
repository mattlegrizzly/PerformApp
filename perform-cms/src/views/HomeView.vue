<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref, onMounted } from 'vue'
import NavMenu from '@/components/NavMenu.vue'
import type IEUser from '@/types/types'

const user = ref({
  user : {
    email : ''
  }
} as IEUser);
const loadObjectFromLocalStorage = () => {
  const storedObject = localStorage.getItem('user') // Remplacez 'yourObjectName' par la clé utilisée pour stocker votre objet
  if (storedObject) {
    user.value = JSON.parse(storedObject)
    console.log(user.value)
  }
}

onMounted(() => {
  loadObjectFromLocalStorage() // Appel de la fonction lors du montage du composant
})
</script>

<template>
  <NavMenu />
  <div class="mainWrapper">
    <h1>Bienvenue {{ user?.user?.email === '' ? '' : user.user.last_name + ' ' + user.user.first_name }}</h1>
  </div>
  <RouterView />
</template>
