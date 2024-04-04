<script setup lang="ts">
import { ref } from 'vue'
import router from '@/router'
import image from '@/assets/logo_perform.png'
import '@/assets/base.css'

const email = ref('')
const password = ref('')

const alert = ref(false)
const error_message = ref('error')

const sendData = () => {
  console.log(password.value, ' ', email.value)
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
      console.log(data)
      localStorage.setItem('user', JSON.stringify(data))
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
  width: 100%;
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
  border-radius: 20px;
  padding: 10px;
  background-color: #00000008;
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
        <input v-model="email" placeholder="entre-votre email" />
      </div>
      <div class="inputFormDiv">
        <span>Mot de passe</span>
        <input v-model="password" type="password" placeholder="*****" />
      </div>
      <div class="buttonWrapper">
        <button @click="sendData">Se connecter</button>
      </div>
    </form>
  </div>
  <RouterView v-show="false" />
</template>
