<template lang="">
  <header>
    <div class="navApp">
      <div class="logoWrapper">
        <img class="logo" :src="image" />
      </div>
      <nav>
        <a v-on:click.stop.prevent="routerMove('/')">Accueil</a>
        <a v-on:click.stop.prevent="routerMove('/users')">Utilisateurs</a>
        <a v-on:click.stop.prevent="routerMove('/exercises')">Exercices</a>
        <a v-on:click.stop.prevent="routerMove('/materials')">Matériels</a>
        <a v-on:click.stop.prevent="routerMove('/sports')">Sports</a>
      </nav>
      <div class="buttonWrapper">
        <button @click="deconnectUser">Se déconnecter</button>
      </div>
    </div>
  </header>
</template>
<script setup lang="ts">
import image from '@/assets/logo_perform.png'
import router from '@/router'
import { useCookies } from '@vueuse/integrations/useCookies'
import { useUserStore } from '@/stores/store'
import './index.css'

const userStore = useUserStore()
const cookies = useCookies(['locale'])

const routerMove = (route: string) => {
  router.push(route)
}

const deconnectUser = () => {
  cookies.remove('access')
  userStore.removeUser()
  router.push('/login')
}
</script>
