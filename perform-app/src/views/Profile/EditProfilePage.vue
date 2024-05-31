<style scoped>
.input-div ion-list {
  width: auto;
  height: 40px;
  display: flex;
  align-items: center;
}

.input-div ion-item {
  border-radius: 30px;
  border: 1px solid #d4d4d4;
  min-height: 40px !important;
  width: 100%;
}

ion-chip {
  padding-left: 10px;
  padding-right: 10px;
  color: white;
  background-color: var(--primary-blue);
}
</style>

<template>
  <ion-page>
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton url="profile" text="Retour" back="back" />
        </div>
        <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
          Modifier mes informations
        </h1>
        <div class="edit_profile_div">
          <div class="input-div">
            <ion-label>Nom : </ion-label>
            <ion-input type="text" class="login-input" fill="outline" slot="end" placeholder="Prénom" shape="round"
              @ionInput="handleInput('first_name', $event.detail.value)" :value="user.first_name"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Prénom : </ion-label>
            <ion-input type="text" class="login-input" fill="outline" slot="end" placeholder="Nom" shape="round"
              @ionInput="handleInput('last_name', $event.detail.value)" :value="user.last_name"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Email : </ion-label>
            <ion-input type="email" class="login-input" fill="outline" slot="end" placeholder="email@perform.com"
              shape="round" @ionInput="handleInput('email', $event.detail.value)" :value="user.email"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Âge : </ion-label>
            <ion-input type="number" class="login-input" fill="outline" slot="end" placeholder="20" shape="round"
              @ionInput="handleInput('age', $event.detail.value)" :value="user.age"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Taille : </ion-label>
            <ion-input type="number" class="login-input" fill="outline" slot="end" placeholder="170" shape="round"
              @ionInput="handleInput('size', $event.detail.value)" :value="user.size"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Poids : </ion-label>
            <ion-input type="number" class="login-input" fill="outline" slot="end" placeholder="80" shape="round"
              @ionInput="handleInput('weight', $event.detail.value)" :value="user.weight"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Âge : </ion-label>
            <ion-list>
              <ion-item>

                <ion-select class="custom-ion-select" :value="sports_user_temp" aria-label="Fruit"
                  placeholder="Selectionner vos sports" :multiple="true">
                  <ion-select-option v-for="(sport, index) in sports" :value="sport.id">{{ sport.name
                    }}</ion-select-option>
                </ion-select>
              </ion-item>
            </ion-list>
            <ion-chip :icon="close" v-for="sport of user.sports_user" color="primary">{{
              sport.sport.name
            }}</ion-chip>
          </div>
        </div>

      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">

import { IonContent, IonPage, IonInput, IonLabel, IonList, IonItem, IonSelect, IonSelectOption } from "@ionic/vue";
import { ref, onMounted, onUpdated } from "vue";
import "@/assets/base.css";
import "@/assets/main.css";
import { store } from "../../store/store";
import { post } from "../../lib/callApi";
import router from "../../router";
import { Sport } from "../../types/allType";
import { useRoute } from "vue-router";
import NavButton from "../../components/NavButton/NavButton.vue";
import { get } from "../../lib/callApi";
import './index.css'
const routes = useRoute();

const handleInput = (key: string, value: string) => {
  user.value[key] = value;
};

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
  sports_user: [] as Sport[],
  user_injuries: [],
  users_wellness: [],
});

const sports_user_temp = ref([] as Sport[])
const sports = ref([] as Sport[])

onMounted(async () => {
  let storeUser = await store.get("user");
  if (storeUser !== "") {
    user.value = JSON.parse(storeUser).user;
    user.value.sports_user.map((sport) => {
      sports_user_temp.value.push(sport.sport)
    })
    console.log("sports temp ", sports_user_temp)
  }
  get('/sports', { body: {} }, false).then((res) => {
    if (res.status > 300) {

    } else {
      sports.value = res.results;
    }
  })
  const ionSelect = document.querySelectorAll(".custom-ion-select");
  console.log(ionSelect);
  if (ionSelect === null) return;
  for (const elem of ionSelect) {
    const shadowRoot = elem.shadowRoot;
    if (shadowRoot === null) return;
    const style = document.createElement("style");
    style.textContent = `
        .select-wrapper-inner {
        width: 100%; /* Ajustez cette valeur selon vos besoins */
        justify-content: space-between;
      }
    `;
    shadowRoot.appendChild(style);
  }
});

const load = () => {
  console.log("user ", user.value);
  store.get("user").then((res) => {
    const json = JSON.parse(res);
    user.value = json.user;
  });
  get('/sports', { body: {} }, false).then((res) => {
    if (res.status > 300) {

    } else {
      sports.value = res.results;
    }
  })
};

onUpdated(() => {
  if (routes.name == "EditProfile") {
    load();
  }
});

</script>
