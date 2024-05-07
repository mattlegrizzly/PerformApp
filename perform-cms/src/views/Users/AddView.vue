<script setup lang="ts">
import NavMenu from '../../components/NavMenu/NavMenu.vue'
import { ref, onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import '@/assets/base.css'
import { post } from '@/lib/callApi'
import type IERequestOptions from '@/types/request'
import router from '@/router'
import NavButton from '@/components/NavButton/NavButton.vue'

const user = ref({})

const alertErr = ref(false)
const alertSuc = ref(false)
const error_message = ref('')
const success_message = ref('error')

const gender = ref([
  {id : 'male', value : "Homme"},
  {id : 'female', value : "Femme"},
  {id : 'other', value : "Autre"}
])
const image_url = ref('')
const image_src = ref('')

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

function genererTexteAleatoire() {
  var caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+='
  var longueur = 15
  var texteAleatoire = ''

  for (var i = 0; i < longueur; i++) {
    var caractereAleatoire = caracteres.charAt(Math.floor(Math.random() * caracteres.length))
    texteAleatoire += caractereAleatoire
  }

  return texteAleatoire
}

const sendData = (quitForm: boolean) => {
  const option = {
    body: {
      email: user.value.email,
      password: user.value.password,
      last_name: user.value.last_name,
      first_name: user.value.first_name,
      gender: user.value.gender,
      age: user.value.age,
      size: user.value.size,
      profile_picture: image_url.value
    }
  } as IERequestOptions

  post('/register/', option, false, true)
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
        if (quitForm) {
          router.push('/users')
        } else {
          success_message.value = 'Vous avez ajoutez : ' + res.first_name + ' ' + res.last_name
          user.value = {}
          image_url.value = ''
          image_src.value = ''
          alertSuc.value = true
        }
      }
    })
    .catch((error) => {
      alertErr.value = true
    })
}

onMounted(() => {
  user.value.password = genererTexteAleatoire()
})
</script>
<style>
.inputFormDiv {
  width: 100% !important;
}
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
    <NavButton class="returnBack" :text="'Retour'" :url="'/users'" prepend-icon="mdi-arrow-left" />
    <h1>Ajouter un Utilisateur</h1>
    <form @submit.prevent="submit">
      <div class="inputFormDiv">
        <v-text-field v-model="user.email" label="Email * " variant="filled"></v-text-field>
      </div>
      <div class="inputFormDiv">
        <v-text-field v-model="user.last_name" label="Nom " variant="filled"></v-text-field>
        <v-text-field v-model="user.first_name" label="Pénom " variant="filled"></v-text-field>
      </div>
      <div class="inputFormDiv">
        <v-text-field v-model="user.size" label="Taille " variant="filled"></v-text-field>
      </div>
      <div class="inputFormDiv">
        <v-text-field label="Poids" v-model="user.weight"></v-text-field>
      </div>
      <div class="inputFormDiv">
        <v-text-field label="Age" v-model="user.age"></v-text-field>
      </div>
      <div class="inputFormDiv">
        <v-select
          label="Select"
          :items="gender"
          v-model="user.gender"
          item-title="value"
          item-value="id"
        ></v-select>
      </div>
      <div class="inputFormDiv">
        <v-text-field label="Mot de passe" v-model="user.password"></v-text-field>
      </div>
      <div class="inputFormDiv">
        <v-file-input
          label="Photo de profil utilisateur"
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
