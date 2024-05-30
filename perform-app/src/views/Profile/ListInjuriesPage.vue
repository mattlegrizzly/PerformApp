<style scoped></style>

<template>
  <ion-page>
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton url="profile" text="Retour" back="back" />
          <NavButton url="add_injurie" text="Ajouter" :noIcon="true" />
        </div>
        <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
          Liste de mes blessures
        </h1>
      </div>
      <ion-list
        lines="none"
        style="
          padding-left: var(--pd-l);
          padding-right: var(--pd-r);
          padding-top: 10px;
          padding-bottom: 10px;
        "
      >
        <ion-item
          class="injurie_div_info"
          v-for="injurie of user.user_injuries"
        >
          <div class="injurie_div_parent">
            <div class="injurie_info">
              <ion-label>{{ injurie.name }}</ion-label>
              <ion-label>{{ injurie.date }}</ion-label>
            </div>
            <div class="injurie_info">
              <ion-label>{{ injurie.zone.name }}</ion-label>
              <ion-label
                :class="stateSetClass(injurie.state)"
                class="injurie_state"
                >{{ stateSet(injurie.state) }}
              </ion-label>
            </div>
          </div>
          <div class="injurie_icon">
            <ion-icon :icon="chevronForwardOutline"></ion-icon>
          </div>
        </ion-item>
      </ion-list>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonContent,
  IonPage,
  IonList,
  IonLabel,
  IonIcon,
  IonItem,
} from "@ionic/vue";
import "@/assets/base.css";
import "@/assets/main.css";
import { chevronForwardOutline } from "ionicons/icons";
//@ts-expect-error
import NavButton from "../../components/NavButton/NavButton.vue";
import { onMounted, ref, onUpdated } from "vue";
import { get } from "../../lib/callApi";
//@ts-expect-error
import type { Sport } from "@/types/types";
import { useRoute } from "vue-router";
import { store } from "../../store/store";
import { IEInjury } from "../../types/allType";

import "./index.css";

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
  sports_user: [] as Sport[],
  user_injuries: [] as IEInjury[],
  users_wellness: [],
});

const stateSet = (state: string) => {
  switch (state) {
    case "NT":
      return "Non traité";
    case "IP":
      return "En cours";
    case "TR":
      return "Traité";
    default:
      return "Non traité";
  }
};

const stateSetClass = (state: string) => {
  switch (state) {
    case "NT":
      return "nt_class";
    case "IP":
      return "ip_class";
    case "TR":
      return "tr_class";
    default:
      return "";
  }
};

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

onMounted(async () => {
  let storeUser = await store.get("user");
  if (storeUser !== "") {
    user.value = JSON.parse(storeUser).user;
  }
});

onUpdated(() => {
  if (routes.name == "Profile") {
    load();
  }
});
</script>
