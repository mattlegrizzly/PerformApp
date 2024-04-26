<template lang="">
  <header>
    <div class="navApp">
      <div class="logoWrapper">
        <img class="logo" :src="image" />
      </div>
      <nav>
        <a href="/">Home</a>
        <a href="/users">Users</a>
        <a href="/exercises">Exercices</a>
        <a href="/materials">Materials</a>
        <a href="/sports">Sports</a>
      </nav>
      <div class="buttonWrapper">
        <button @click="deconnectUser">Disconnect</button>
      </div>
    </div>
  </header>
</template>
<script setup lang="ts">
import image from '@/assets/logo_perform.png'
import router from '@/router'
import {useCookies} from '@vueuse/integrations/useCookies'
import { useUserStore } from '@/stores/store';

const userStore = useUserStore();
const cookies = useCookies(['locale'])

const deconnectUser = () => {
  cookies.remove('access');
  userStore.removeUser();
  router.push('/login');
}
</script>
<style>
.navApp {
  height: 100vh;
    width: 300px;
    padding-top: 10px;
    box-shadow: 0px 0px 10px rgb(219, 219, 219);
    position: absolute;
    left: 0px;
    top: 0px;
}

.navApp nav {
  display: flex;
  flex-direction: column;
  margin-top: 20px;
}

.navApp nav a {
  padding-left: 20px;
  padding-right: 20px;
  color: black;
}

.navApp .logo {
  padding-left: 20px;
  padding-right: 20px;
  margin: 10px;
  width: 200px;
}

.navApp .logoWrapper {
  display: flex;
  width: 100%;
  justify-content: center;
  align-items: center;
}

.navApp .buttonWrapper {
  position: absolute;
  bottom: 10px;
  width: 100%;
  padding: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.buttonWrapper button {
  width: 100%;
  height: 40px;
}
</style>
