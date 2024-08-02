<template lang="">
  <header>
    <div class="navApp">
      <div class="logoWrapper">
        <img class="logo" :src="image" />
      </div>
      <nav>
        <a class="parent-menu" v-on:click.stop.prevent="routerMove('/')">Accueil</a>
        <a class="parent-menu"  v-on:click.stop.prevent="routerMove('/users')">Utilisateurs</a>
        <a class="parent-menu no-overflow" >Bibliothèque
        </a>
        <a class="sub-menu" v-on:click.stop.prevent="routerMove('/exercises')">Exercices</a>
        <a class="sub-menu" v-on:click.stop.prevent="routerMove('/materials')">Matériels</a>
        <a class="sub-menu" v-on:click.stop.prevent="routerMove('/sports')">Sports</a>
        <a class="parent-menu  no-overflow"> Records
        </a>
        <a class="sub-menu" v-on:click.stop.prevent="routerMove('/records_theme')">Générales</a>
        <a class="sub-menu" v-on:click.stop.prevent="routerMove('/records_sports')">Sports</a>
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

<style>
.sub-menu {
  padding-left: 40px !important;
  font-style: italic;
}

.parent-menu {
  font-weight: 600;
}

.no-overflow:hover{
  background-color: transparent !important
}
</style>
