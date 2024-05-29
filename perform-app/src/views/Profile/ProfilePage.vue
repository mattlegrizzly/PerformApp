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
      <div class="container_home">
        <div class="profile_picture_div">
          <div class="img_container">
            <img :src="user ? api + user.profile_picture : ''" alt='profile'>
          </div>
        </div>
        <div class="profile_container_div">
          <h1>
            {{ user.first_name + " " + user.last_name }}
          </h1>
        </div>
        <div class="profile_container_div">
          <div class="div_container_info">
            <h2>
              Mes disciplines
            </h2>
            <ion-chip v-for="sport of user.sports_user" color="primary">{{ sport.sport.name
              }}</ion-chip>
          </div>
        </div>
        <div class="profile_container_div">
          <div class="div_container_info">
            <h2>
              Mes infos
            </h2>
            <div class="users_infos">

              <div class=div_user_info>
                <h3>Âge :</h3>
                <p>{{ user.age }}</p>
              </div>

              <div class=div_user_info>
                <h3>Poids :</h3>
                <p>{{ user.weight }} kg</p>
              </div>

              <div class=div_user_info>
                <h3>Taille :</h3>
                <p>{{ user.size }} cm</p>
              </div>
            </div>
          </div>
        </div>
        <div class="profile_container_div">
          <div class="div_container_info">
            <h2>
              Mes blessures
            </h2>
            <ion-list>
              <div class="injurie_div" v-for="injurie of injuries">
                <ion-label>{{ injurie.zone.name
                  }}</ion-label>
                <ion-label>|</ion-label>
                <ion-label> {{ injurie.date.toLocaleDateString("fr") }}</ion-label>
                <ion-label>|</ion-label>
                <ion-label :class="stateSetClass(injurie.state)" class="injurie_state">{{ stateSet(injurie.state) }}


                </ion-label>
                <ion-icon :icon="chevronForwardOutline"></ion-icon>

              </div>
            </ion-list>
          </div>
        </div>
        <ion-button size="small" @click="disconnect">
          Connexion
        </ion-button>
      </div>
    </ion-content>
  </ion-page>
</template>

<script lang="ts" setup>
import { IonContent, IonPage, IonButton, IonChip, IonList, IonIcon, IonItem, IonLabel } from '@ionic/vue';
import { store } from '../../store/store';
import router from '../../router';
import { inject, onMounted, onUpdated, ref } from 'vue';
import { get } from '../../lib/callApi';
import { useRoute } from 'vue-router';
import './index.css'
import type { Sport } from '@/types/types'
import { chevronForwardOutline } from "ionicons/icons";

const api = import.meta.env.VITE_API_URL;
const routes = useRoute();
const user = ref({
  age: 0,
  weight: 0,
  size: 0,
  email: "",
  first_name: "",
  gender: "",
  id: 1,
  last_name: "",
  profile_picture: "",
  sports_user: [
  ] as Sport[],
  user_injuries: [],
  users_wellness: []
})

const stateSet = (state: string) => {
  switch (state) {
    case 'NT':
      return 'Non traité'
    case 'IP':
      return 'En cours'
    case 'TR':
      return 'Traité'
    default:
      return 'Non traité'
  }
}

const stateSetClass = (state: string) => {
  switch (state) {
    case 'NT':
      return 'nt_class'
    case 'IP':
      return 'ip_class'
    case 'TR':
      return 'tr_class'
    default:
      return ''
  }
}

const injuries = ref([
  {
    id: 1,
    name: 'déchirure du biceps',
    state: 'NT',
    date: new Date(Date.now()),
    description: 'arrachement tendon brachial lors d\'un curl',
    zone: {
      code: "biceps",
      name: "Biceps"
    }
  },
  {
    id: 2,
    name: 'déchirure du biceps',
    state: 'TR',
    date: new Date(Date.now()),
    description: 'arrachement tendon brachial lors d\'un curl',
    zone: {
      code: "biceps",
      name: "Biceps"
    }
  }
])

const disconnect = () => {
  store.set('user', '').then(() => {
    router.push('/login')
  })
}

const load = () => {
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
      store.set('user', JSON.stringify(userToSet))
    })
  })
}

onMounted(async () => {
  console.log(injuries)
  let storeUser = await store.get('user')
  user.value = JSON.parse(storeUser).user
  console.log(user.value)
})

onUpdated(() => {
  if (routes.name == "Profile") {
    //load()
  }
})


</script>