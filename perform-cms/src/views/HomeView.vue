<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref, onMounted } from 'vue'
import NavMenu from '@/components/NavMenu.vue'
import type IEUser from '@/types/types'
import { get, refresh } from '@/lib/callApi'

const user = ref({
  user : {
    email : ''
  }
} as IEUser);
const alert = ref(false)
const error_message = ref('error')
const loadObjectFromLocalStorage = () => {
  const storedObject = localStorage.getItem('user') // Remplacez 'yourObjectName' par la clé utilisée pour stocker votre objet
  if (storedObject) {
    user.value = JSON.parse(storedObject)
  }
}

const getUsers = async () => {
  console.log('Bearer ' + user.value.access)
  const response = await get('/admin/users_all/latest');
  console.log('la reponse ' , response)
}

onMounted(() => {
  loadObjectFromLocalStorage() // Appel de la fonction lors du montage du composant
  getUsers();
})

const closePopup = () => {
  alert.value = false
}
</script>

<template>
  <NavMenu />
    <div class="mainWrapper">
      <h1>Bienvenue {{ user?.user?.email === '' ? '' : user.user.last_name + ' ' + user.user.first_name }}</h1>
    </div>
  
  <RouterView />
</template>
