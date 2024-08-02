<script setup lang="ts">
import NavMenu from '../../components/NavMenu/NavMenu.vue'
import { ref, onMounted, watch } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import '@/assets/base.css'
import { post, get } from '@/lib/callApi'
import type IERequestOptions from '@/types/request'
import { useRoute , useRouter} from 'vue-router'
import NavButton from '@/components/NavButton/NavButton.vue'
const route = useRoute()
const router = useRouter()

const unit_selected = ref(
  'time')

watch(() => unit_selected, () => {
  console.log(unit_selected)
})

const name = ref('')
const description = ref('')

const id = ref(0)
const alertErr = ref(false)
const alertSuc = ref(false)
const error_message = ref('')
const error_title = ref('')
const success_message = ref('error')

const sport = ref('')

const closePopup = () => {
  alertErr.value = false
  alertSuc.value = false
}

const sendData = (quitForm: boolean) => {
  const option = {
    body: {
      name: name.value,
      units: unit_selected.value, 
      sport: id.value
    }
  } as IERequestOptions
  post('/admin/records/', option, true)
    .then((res) => {
      error_message.value = ''
      success_message.value = ''
      if (res.status) {
        const keys = Object.keys(res.data)
        for (let i = 0; i < keys.length; i++) {
          error_message.value += keys[i] + ' : ' + res.data[keys[i]] + '\n\n'
        }
        throw Error()
      } else {
        name.value = ''
        description.value = ''
        if (quitForm) {
          router.push('/sports')
        } else {
          success_message.value = 'Vous avez ajoutez : ' + res.name
          alertSuc.value = true
        }
      }
    })
    .catch((error) => {
      alertErr.value = true
    }) 
   console.log(unit_selected.value)
}

const getSport = async () => {
  id.value = Number(route.params.sport_id)
  const res = await get('/admin/sports/' + id.value + '/')
  if (res.status === 404) {
    error_title.value = 'Erreur à la récupération du Sport avec pour id ' + id.value
    error_message.value = res.data.detail
    alertErr.value = true
  } else {
    sport.value = await res
  }
}
const units = [
  {
    name: 'Temps',
    value: 'time',
  }, {
    name: 'Poids',
    value: 'weight',
  },
]

onMounted(() => {
  getSport()
})
</script>
<style>
.return_btn {
  background-color: white !important;
  color: var(--primary-blue) !important;
  border: 1px solid var(--primary-blue);
  transition: 0.3s;
}

.return_btn:hover {
  transition: 0.3s;
  background-color: var(--primary-blue) !important;
  color: white !important;
}
</style>

<template lang="">
  <NavMenu />
  <v-alert
    :model-value="alertErr"
    border="start"
    close-label="Close Alert"
    color="error"
    title="Erreur à l'ajout"
    closable
    @click:close="closePopup"
  >
    {{ error_message }}
  </v-alert>
  <v-alert
    :model-value="alertSuc"
    border="start"
    close-label="Close Alert"
    color="success"
    title="Record ajouté"
    closable
    @click:close="closePopup"
  >
    {{ success_message }}
  </v-alert>
  <div class="mainWrapper">
    <NavButton class="returnBack" :text="'Retour'" :url="'/sports/show/' + id " prepend-icon="mdi-arrow-left" />
    <h1>Ajouter un Record à : {{sport.name}}</h1>
    <form @submit.prevent="submit">
      <div class="inputFormDiv">
        <v-text-field v-model="name" label="Nom du record * " variant="filled"></v-text-field>
      </div>
      <div class="inputFormDiv">
        <v-select
        v-model="unit_selected"
        :items="units"
        hint="Sélectionnez l'unité à utiliser"
        item-title="name"
        item-value="value"
        label="Select"
      />
      </div>
      <div class="buttonWrapper">
        <button @click="sendData(false)">Créer et continuer</button>
        <button class="return_btn" @click="sendData(true)">Créer</button>
      </div>
    </form>
  </div>
</template>
