<script setup lang="ts">
import { RouterView } from 'vue-router'
import { ref, onMounted } from 'vue'
import NavMenu from '@/components/NavMenu.vue'
import type { IEUser, IEUserData } from '@/types/types'
import { get } from '@/lib/callApi'
import ListElement from '@/components/ListElement.vue'

const users = ref([{}])

const user = ref({
  user: {} as IEUserData
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
  get('/admin/users_all/latest').then((res) => {
    console.log(res);
  });
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
    <div>
      <ListElement :tableHeader="['email', 'nom', 'prénom']" :tableContent="users.values" />
    </div>
  <RouterView />
</template>
