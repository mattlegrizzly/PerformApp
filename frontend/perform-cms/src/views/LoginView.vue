<script setup lang="ts">
import { ref } from 'vue'
import router from '@/router'
import image from '@/assets/logo_perform.png'
import AlertComponents from '@/components/AlertComponents/AlertComponents.vue'
import '@/assets/base.css'
import { useCookies } from '@vueuse/integrations/useCookies'
import { useUserStore } from '@/stores/store'
import { post } from '@/lib/callApi'
const cookies = useCookies(['locale'])

const email = ref('')
const password = ref('')
const show2 = ref(false)
const alertErr = ref(false)
const error_message = ref('')
const error_title = ref('')

const userStore = useUserStore()

const sendData = () => {
  const requestOptions = {
    body: { email: email.value, password: password.value }
  }
  post('/login/', requestOptions)
    .then((response) => {
      console.log('response ', response)
      if (response.status > 300) {
        error_message.value = response.data
        alertErr.value = true
        error_title.value = 'Erreur de login'
      } else {
        userStore.setUser(response.user)
        var date = new Date()
        date.setDate(date.getDate() + 7)
        cookies.set('access', response.access, { expires: date })
        router.push('/')
        password.value = ''
        email.value = ''
      }
    })
    .catch((error) => {
      if (error.message) {
        console.log('error ', error)
        error_message.value = error.message
      } else {
        error_title.value = 'Connexion error'
        error_message.value = 'Credential error'
      }
      alertErr.value = true
    })
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
  <AlertComponents
    :message_alert="error_message"
    :type="'error'"
    :title="error_title"
    :alertValue="alertErr"
  />
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
