<script setup lang="ts">
import { RouterView } from 'vue-router'
import { ref, onMounted } from 'vue'
import NavMenu from '@/components/NavMenu/NavMenu.vue'
import type { IEUser, IEUserData } from '@/types/types'
import { get, verifyToken } from '@/lib/callApi'
import ListElement from '@/components/ListElement/ListElement.vue'
import AlertComponents from '@/components/AlertComponents/AlertComponents.vue'
import { useUserStore } from '@/stores/store'

const users = ref([{}])
const materials = ref([{}])
const sports = ref([{}])
const exercises = ref([{}])

const alert = ref(false)
const alertMessage = ref('')

const userStore = useUserStore()
const user = ref({
  user: {} as IEUserData
} as IEUser)

const setAlertValue = (type: string) => {
  if (type === "error") {
    alert.value = false
  } else {

  }
}

const getUsers = async () => {
  await get('/admin/users_all/latest')
    .then((res) => {
      users.value = res
    })
    .catch((error: Error) => {
      alert.value = true
      alertMessage.value += error.message + ' users \n'
    })
}

const getMaterials = async () => {
  get('/admin/materials/latest')
    .then((res) => {
      materials.value = res
    })
    .catch((error: Error) => {
      alert.value = true
      alertMessage.value += error.message + ' materials \n'
    })
}

const getExercises = async () => {
  get('/admin/exercises/latest')
    .then((res) => {
      exercises.value = res
    })
    .catch((error: Error) => {
      alert.value = true
      alertMessage.value += error.message + ' exercises \n'
    })
}

const getSports = async () => {
  get('/admin/sports/latest')
    .then((res) => {
      sports.value = res
    })
    .catch((error: Error) => {
      alert.value = true
      alertMessage.value += error.message + ' sports \n'
    })
}

onMounted(() => {
  verifyToken()
    .then((res) => {
      if (res.status > 300) {
        if (res.status == 401) {
          throw Error('Token not valid')
        } else {
          throw Error()
        }
      }
      user.value = userStore.getUser
      getUsers()
      getExercises()
      getSports()
      getMaterials()
    })
    .catch((error: Error) => {
      alert.value = true
      alertMessage.value = error.message
    })
})
</script>

<template>
  <NavMenu />
  <div class="mainWrapper">
    <AlertComponents :title="'Erreur de récupération des données'" :type="'error'" :alertValue="alert"
      :message_alert="alertMessage" :setAlertValue="setAlertValue" />
    <h1>
      Bienvenue
      {{ user?.user?.email === '' ? '' : user.user.last_name + ' ' + user.user.first_name }}
    </h1>
    <div class="home-card">
      <div class="five-recents">
        <h2>Les 5 derniers utilisateurs inscrits</h2>
        <ListElement :headerTable="['Id', 'Email', 'Nom', 'Prénom', 'Taille', 'Age', 'Genre']" :contentTable="users"
          :limitData="6" nav="users" />
      </div>
      <div class="five-recents">
        <h2>Les 5 derniers matériels inscrits</h2>
        <ListElement :headerTable="['Id', 'Nom']" :contentTable="materials" :limitData="2" nav="materials" />
      </div>
      <div class="five-recents">
        <h2>Les 5 derniers exercises inscrits</h2>
        <ListElement :headerTable="['Id', 'Nom']" :contentTable="exercises" :limitData="2" nav="exercises"/>
      </div>
      <div class="five-recents">
        <h2>Les 5 derniers sports inscrits</h2>
        <ListElement :headerTable="['Id', 'Nom']" :contentTable="sports" :limitData="2" nav="sports"/>
      </div>
    </div>
  </div>
</template>

<style>
.home-card {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.five-recents {
  margin: 10px;
  width: 48%;
  border: 1px black solid;
  padding: 10px;
  border-radius: 10px;
}
</style>
