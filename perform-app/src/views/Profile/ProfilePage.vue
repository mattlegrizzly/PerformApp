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
      <img :src="'https://api.grizzlyperform.app/' + user.profile_picture">
      <ion-button size="small" @click="disconnect">
        Connexion
      </ion-button>
    </ion-content>
  </ion-page>
</template>

<script lang="ts" setup>
import { IonHeader, IonToolbar, IonTitle, IonContent, IonPage, IonButton } from '@ionic/vue';
import { store } from '../../store/store';
import router from '../../router';
import { onMounted, ref } from 'vue';
import { get } from '../../lib/callApi';

const user = ref({
  user: {
    age: 0,
    email: "",
    first_name: "",
    gender: "",
    id: 1,
    last_name: "",
    profile_picture: null,
    size: null,
    sports_user: [],
    user_injuries: [],
    users_wellness: []
  }
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
    user.value = json;
    console.log(user.value);
    get('/admin/users_all/' + user.value.user.id, {}, true)
  })
}

</script>