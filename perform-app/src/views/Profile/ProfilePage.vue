<style scoped>
.example-content {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
</style>

<template>
  <ion-page>
    <ion-content>
      <img :src="user ? user.profile_picture : ''" alt='profile'>
      <ion-button size="small" @click="disconnect">
        Connexion
      </ion-button>
    </ion-content>
  </ion-page>
</template>

<script lang="ts" setup>
import { IonContent, IonPage, IonButton } from '@ionic/vue';
import { store } from '../../store/store';
import router from '../../router';
import { onMounted, onUpdated, ref } from 'vue';
import { get } from '../../lib/callApi';
import { useRoute } from 'vue-router';
const routes = useRoute();
const user = ref({
  age: 0,
  email: "",
  first_name: "",
  gender: "",
  id: 1,
  last_name: "",
  profile_picture: "",
  size: null,
  sports_user: [],
  user_injuries: [],
  users_wellness: []
})

const disconnect = () => {
  store.set('user', '').then(() => {
    router.push('/login')
  })
}

const load = () => {
  console.log('oui')
  store.get('user').then((res) => {
    const json = JSON.parse(res)
    user.value = json.user;
    get('/admin/users_all/' + user.value.id, {}, true).then((res) => {
      user.value = res;
      console.log(res)
      const userToSet = {
        user: res,
        access: json.access,
        refresh: json.refresh
      }
      console.log(JSON.stringify(userToSet))
      store.set('user', JSON.stringify(userToSet))
    })
  })
}

onMounted(() => {
  console.log(user.value)
})

onUpdated(() => {
  if (routes.name == "Profile") {
    load()
  }
})


</script>