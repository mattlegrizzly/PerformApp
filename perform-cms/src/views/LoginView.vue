<script setup lang="ts">
import { ref } from 'vue'
import router from '@/router'
import image from '@/assets/logo_perform.png'
import '@/assets/base.css'
import { useCookies } from '@vueuse/integrations/useCookies'
import { useUserStore } from '@/stores/store'

const cookies = useCookies(['locale'])

const email = ref('')
const password = ref('')
const show2 = ref(false)
const alert = ref(false)
const error_message = ref('error')

const userStore = useUserStore()

const sendData = () => {
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: email.value, password: password.value })
  }
  fetch('http://127.0.0.1:8000/api/login/', requestOptions)
    .then((response) => {
      if (response.status >= 300) {
        throw Error()
      } else {
        return response.json()
      }
    })
    .then((data) => {
      userStore.setUser(data)
      var date = new Date()
      date.setDate(date.getDate() + 7)
      cookies.set('access', data.access, { expires: date })
      router.push('/')
      password.value = ''
      email.value = ''
    })
    .catch(() => {
      error_message.value = 'Credential error'
      alert.value = true
    })
}

const closePopup = () => {
  alert.value = false
}
</script>

<style>
.loginContent {
  display: flex;
  justify-content: center;
  align-content: center;
  flex-wrap: wrap;
  height: 100%;
}

.logoContent {
  width: 100%;
  display: flex;
  justify-content: center;
  align-content: center;
}

.logoContent img {
  width: 200px;
}

h1,
h2 {
  width: 100%;
  text-align: center;
}

h1 {
  margin-bottom: 5px;
  font-weight: 700 !important;
}

h2 {
  margin-top: 0px !important;
  margin-bottom: 20px !important;
}

.inputFormDiv {
  width: 300px;
  display: flex;
  flex-wrap: wrap;
}
.inputFormDiv span,
input {
  width: 100%;
}

.inputFormDiv span {
  margin-bottom: 8px;
  margin-top: 8px;
}

.inputFormDiv input {
  border-bottom: 1px black !important;
  padding: 10px;
}

.buttonWrapper {
  display: flex;
  justify-content: center;
  align-content: center;
  width: 100%;
}

.buttonWrapper button {
  margin-top: 20px;
  background-color: var(--primary-blue);
  border-radius: 20px;
  color: white;
  transition: 0.3s;
}

.buttonWrapper button:hover {
  margin-top: 20px;
  background-color: white;
  border-radius: 20px;
  color: var(--primary-blue);
  border: solid 1px var(--primary-blue);
  transition: 0.3s;
}
</style>
<template lang="">
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
  <div class="loginContent">
    <div class="logoContent">
      <img :src="image" />
    </div>
    <h1>CMS PerformApp</h1>
    <h2>Connectez-vous</h2>
    <form @submit.prevent="submit">
      <div class="inputFormDiv">
        <span>Email </span>
        <v-text-field v-model="email" placeholder="entre-votre email" />
      </div>
      <div class="inputFormDiv">
        <span>Mot de passe</span>
        <v-text-field
          v-model="password"
          placeholder="*****"
          @click:append-inner="show2 = !show2"
          :append-inner-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
          :type="show2 === true ? 'text' : 'password'"
        />
      </div>
      <div class="buttonWrapper">
        <button @click="sendData">Se connecter</button>
      </div>
    </form>
  </div>
  <RouterView v-show="false" />
</template>
