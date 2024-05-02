<script setup lang="ts">
import NavMenu from '../../components/NavMenu.vue'
import { ref, onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import '@/assets/base.css'
import { post } from '@/lib/callApi'
import type IERequestOptions from '@/types/request'
import router from '@/router'
import NavButton from '@/components/NavButton.vue'
const name = ref('')
const image_url = ref('')
const image_src = ref('')

const alertErr = ref(false)
const alertSuc = ref(false)
const error_message = ref('')
const success_message = ref('error')

const closePopup = () => {
  alertErr.value = false
  alertSuc.value = false
}

const onChangeInput = (e: any) => {
  const file = e.target.files[0]
  if (!file) return

  image_url.value = file
  // Convertir l'image en URL de données
  const reader = new FileReader()
  reader.onload = (e) => {
    image_src.value = e.target?.result as string
  }
  reader.readAsDataURL(file)
}

const sendData = (quitForm: boolean) => {
  const option = {
    body: {
      name: name.value,
      pictures: image_url.value
    }
  } as IERequestOptions
  post('/admin/materials/', option, true, true)
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
        image_url.value = ''
        image_src.value = ''
        if (quitForm) {
          router.back()
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

.returnBack {
  margin-top: 10px;
}
</style>

<template lang="">
  <NavMenu />

  <div class="mainWrapper">
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
      title="Matériel ajouté"
      closable
      @click:close="closePopup"
    >
      {{ success_message }}
    </v-alert>
    <NavButton
      class="returnBack"
      :text="'Retour'"
      :url="'/materials'"
      prepend-icon="mdi-arrow-left"
    />
    <h1>Ajouter un Matériel</h1>
    <form @submit.prevent="submit">
      <div class="inputFormDiv">
        <v-text-field v-model="name" label="Nom du matériel * " variant="filled"></v-text-field>
      </div>
      <div class="inputFormDiv">
        <v-file-input
          label="Photo du matériel"
          prepend-icon="mdi-camera"
          variant="filled"
          v-model="image_url"
          @change="onChangeInput($event)"
        ></v-file-input>
      </div>
      <div class="imageDiv">
        <v-img :height="100" aspect-ratio="16/9" :src="image_src"></v-img>
      </div>

      <div class="buttonWrapper">
        <button @click="sendData(false)">Créer et continuer</button>
        <button class="return_btn" @click="sendData(true)">Créer</button>
      </div>
    </form>
  </div>
  <RouterView />
</template>
