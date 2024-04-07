<script setup lang="ts">
import { RouterView } from 'vue-router'
import { ref, onMounted } from 'vue'
import NavMenu from '@/components/NavMenu.vue'
import type { IEUser, IEUserData } from '@/types/types'
import { get } from '@/lib/callApi'
import ListElement from '@/components/ListElement.vue'

const users = ref([{}])
const materials = ref([{}])
const sports = ref([{}])
const exercises = ref([{}])

const user = ref({
  user: {} as IEUserData
} as IEUser);
const alert = ref(false)
const error_message = ref('error')
const loadObjectFromLocalStorage = () => {
  const storedObject = localStorage.getItem('user') // Remplacez 'yourObjectName' par la clé utilisée pour stocker votre objet
  console.log('storedObject ', storedObject)
  if (storedObject) {
    user.value = JSON.parse(storedObject)
  }
}

const getUsers = async () => {
  const res = await get('/admin/users_all/latest');
  users.value = await res;
}

const getMaterials = async () => {
  const res = await get('/admin/materials/latest');
  materials.value = await res;
}

const getExercises = async () => {
  const res = await get('/admin/exercises/latest');
  exercises.value = await res;
}

const getSports = async () => {
  const res = await get('/admin/sports/latest');
  sports.value = await res;
}

onMounted(() => {
  loadObjectFromLocalStorage() // Appel de la fonction lors du montage du composant
  getUsers();
  getExercises();
  getSports();
  getMaterials();
})

const closePopup = () => {
  alert.value = false
}
</script>

<template>
  <NavMenu />
    <div class="mainWrapper">
      <h1>Bienvenue {{ user?.user?.email === '' ? '' : user.user.last_name + ' ' + user.user.first_name }}</h1>
      <div class="home-card">
        <div class="five-recents">
          <h2>
            Les 5 derniers utilisateurs inscrits
          </h2>
          <ListElement :headerTable="['Email', 'Nom', 'Prénom' , 'Taille', 'Age', 'Genre']" :contentTable="users" :limitData="6" />
        </div>
        <div class="five-recents">
          <h2>
            Les 5 derniers matériels inscrits
          </h2>
          <ListElement :headerTable="['Id', 'Nom']" :contentTable="materials" :limitData="2" />
        </div>
        <div class="five-recents">
          <h2>
            Les 5 derniers exercises inscrits
          </h2>
          <ListElement :headerTable="['Nom']" :contentTable="exercises" :limitData="1" />
        </div>
        <div class="five-recents">
          <h2>
            Les 5 derniers sports inscrits
          </h2>
          <ListElement :headerTable="['Id', 'Nom']" :contentTable="sports" :limitData="2" />
        </div>
      </div>
    </div>
  <RouterView />
</template>

<style>
.home-card {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap
}

.five-recents {
  margin : 10px;
  width : 48%;
  border: 1px black solid;
  padding: 10px;
  border-radius: 10px;
}
</style>