<script setup lang="ts">
import { ref } from 'vue'
import router from '@/router';
const email = ref('')
const password = ref('')

const sendData = () => {
      console.log(password.value, " " , email.value)
      const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email: email.value, password: password.value })
  };
  fetch("http://127.0.0.1:8000/api/login/", requestOptions)
    .then(response => response.json())
    .then(data => {
      localStorage.setItem('user', JSON.stringify(data));
      router.push('/');
    });
}
</script>

<style lang=""></style>

<template lang="">
  <div>
    <h1>Connectez-vous</h1>
    <form @submit.prevent="submit">
      <span>Email </span>
      <input v-model="email" placeholder="entre-votre email" />
      <span>Mot de passe</span>
      <input v-model="password" type="password" placeholder="*****" />
      <button @click="sendData">Submit</button>
    </form>
  </div>
  <RouterView v-show="false"/>
</template>
