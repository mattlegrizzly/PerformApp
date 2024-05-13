<script setup lang="ts">
import NavMenu from '../../components/NavMenu/NavMenu.vue'
import { ref, onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import '@/assets/base.css'
import { post } from '@/lib/callApi'
import type IERequestOptions from '@/types/request'
import router from '@/router'
import NavButton from '@/components/NavButton/NavButton.vue'

const name = ref('')
const description = ref('')

const alertErr = ref(false)
const alertSuc = ref(false)
const error_message = ref('')
const success_message = ref('error')

const closePopup = () => {
  alertErr.value = false
  alertSuc.value = false
}

const sendData = (quitForm: boolean) => {
  const option = {
    body: {
      name: name.value
    }
  } as IERequestOptions
  post('/admin/sports/', option, true)
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
          router.push('/materials')
        } else {
          success_message.value = 'Vous avez ajoutez : ' + res.name
          alertSuc.value = true
        }
      }
    })
    .catch((error) => {
      alertErr.value = true
    })
}
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
    title="Erreur de connexion"
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
    title="Sport ajouté"
    closable
    @click:close="closePopup"
  >
    {{ success_message }}
  </v-alert>
  <div class="mainWrapper">
    <NavButton class="returnBack" :text="'Retour'" :url="'/sports'" prepend-icon="mdi-arrow-left" />
    <h1>Ajouter un Sport</h1>
    <form @submit.prevent="submit">
      <div class="inputFormDiv">
        <v-text-field v-model="name" label="Nom du sport * " variant="filled"></v-text-field>
      </div>
      <div class="buttonWrapper">
        <button @click="sendData(false)">Créer et continuer</button>
        <button class="return_btn" @click="sendData(true)">Créer</button>
      </div>
    </form>
  </div>
</template>
