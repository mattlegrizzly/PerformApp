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
const alert = ref(false)
const error_message = ref('error')
const loadObjectFromLocalStorage = () => {
  const storedObject = localStorage.getItem('user') // Remplacez 'yourObjectName' par la clé utilisée pour stocker votre objet
  if (storedObject) {
    user.value = JSON.parse(storedObject)
  }
}

const getUsers = () => {
  console.log('Bearer ' + user.value.access)
  const requestOptions = {
    method: 'GET',
    headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + user.value.access },
  }
  fetch('http://127.0.0.1:8000/api/admin/users_all/', requestOptions)
    .then((response) => {
      if (response.status >= 300) {
        throw Error()
      } else {
        return response.json()
      }
    })
    .then((data) => {
      console.log(data);
      //Stocker le contenu des users dans un tableau
    })
    .catch(() => {
      error_message.value = 'Error while getting users'
      alert.value = true
    })
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
  <v-alert
    :model-value="alert"
    border="start"
    close-label="Close Alert"
    color="error"
    title="Erreur de connexion"
    variant="tonal"
    closable
    @click:close="closePopup"
  >
    {{ error_message }}
  </v-alert>
    <div class="mainWrapper">
      <h1>Bienvenue {{ user?.user?.email === '' ? '' : user.user.last_name + ' ' + user.user.first_name }}</h1>
    </div>
  
  <RouterView />
</template>
