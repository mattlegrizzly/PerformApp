<style scoped></style>

<template>
  <ion-page>
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton url="profile" text="Retour" back="back" />
          <NavButton text="Enregistrer" :noIcon="true" />
        </div>
        <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
          Editer mon profil
        </h1>
        <div class="input-div">
          <ion-label>Prénom : </ion-label>
          <ion-input
            class="login-input"
            fill="outline"
            slot="end"
            placeholder="Prénom"
            shape="round"
            @ionInput="handleInput('first_name', $event.detail.value)"
            :value="user.first_name"
          ></ion-input>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
const pwd = ref("");
const email = ref("");

import { IonContent, IonPage, IonInput, IonLabel, IonButton } from "@ionic/vue";
import { ref, onMounted, onUpdated } from "vue";
import "@/assets/base.css";
import "@/assets/main.css";
import { store } from "../../store/store";
import { post } from "../../lib/callApi";
import router from "../../router";
import { Sport } from "../../types/allType";
import { useRoute } from "vue-router";

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

onMounted(async () => {
  let storeUser = await store.get("user");
  if (storeUser !== "") {
    user.value = JSON.parse(storeUser).user;
  }

  const ionSelect = document.querySelectorAll(".custom_nav");
  console.log(ionSelect);
  if (ionSelect === null) return;
  for (const elem of ionSelect) {
    const shadowRoot = elem.shadowRoot;
    if (shadowRoot === null) return;
    console.log(shadowRoot);
    const style = document.createElement("style");
    style.textContent = `
        .button-inner {
        justify-content: flex-start !important;
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
    get("/admin/users_all/" + user.value.id, { body: {} }, true).then((res) => {
      user.value = res;
      res;
      const userToSet = {
        user: res,
        access: json.access,
        refresh: json.refresh,
      };
      store.set("user", JSON.stringify(userToSet));
    });
  });
};

onUpdated(() => {
  if (routes.name == "EditProfile") {
    load();
  }
});
</script>
