<style scoped></style>

<template>
  <ion-page>
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton url="profile" text="Retour" back="back" />
          <NavButton @click="addInjurie" text="Enregistrer" :noIcon="true" />
        </div>
        <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
          Ajouter une blessure
        </h1>
        <div class="input_injurie">
          <ion-label>Nom de la blessure</ion-label>
          <ion-input label-placement="stacked" fill="outline" @ion-change="handleInput('name', $event.detail.value)"
            placeholder="Déchirure du quadriceps"></ion-input>
        </div>
        <div class="input_injurie">
          <ion-label>Description de la blessure</ion-label>

          <ion-textarea variant="outlined" placeholder="Décrivez votre blessure"
            @ion-change="handleInput('description', $event.detail.value)">
          </ion-textarea>
        </div>

        <div class="input_injurie">
          <ion-label>Zone de la blessure</ion-label>

          <ion-list class="filter-item">
            <ion-item>
              <ion-select interface="popover" placeholder="Zone de la blessure" class="custom-ion-select"
                :toggle-icon="chevronDownOutline" justify="space-between"
                @ion-change="handleInput('zone', $event.detail.value)">
                <ion-select-option v-for="elem in muscles" :key="elem.code" :value="elem.code">{{
                  elem.name }}</ion-select-option>
              </ion-select>
            </ion-item>
          </ion-list>
        </div>
        <div class="input_injurie">
          <ion-label>Date de la blessure</ion-label>
          <ion-input type="date" label-placement="stacked" fill="outline" placeholder="2021-09-01"
            @ion-change="handleInput('date', $event.detail.value)"></ion-input>
        </div>
        <div class="input_injurie">
          <ion-label>Etat de la blessure</ion-label>
          <ion-list class="filter-item">
            <ion-item>
              <ion-select interface="popover" placeholder="Etat de la blessure" class="custom-ion-select"
                :toggle-icon="chevronDownOutline" justify="space-between"
                @ion-change="handleInput('state', $event.detail.value)">
                <ion-select-option v-for="elem in injuries_state" :key="elem.code" :value="elem.code">{{ elem.name
                  }}</ion-select-option>
              </ion-select>
            </ion-item>
          </ion-list>
        </div>
        <div style="
            display: flex;
            width: 100%;
            margin-top: 16px;
            justify-content: center;
            align-items: center;
          ">
          <BodyComponent :muscleSelected="[{ zone: zone }]" :height="'200'" :width="'100'" :viewOnly="'show'" />
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonContent,
  IonPage,
  IonList,
  IonItem,
  IonSelect,
  IonSelectOption,
  IonInput,
  IonTextarea,
  onIonViewWillEnter
} from "@ionic/vue";
import "@/assets/base.css";
import "@/assets/main.css";
import { chevronDownOutline } from "ionicons/icons";
import NavButton from "../../components/NavButton/NavButton.vue";
import { onMounted, ref } from "vue";
import { get, post } from "../../lib/callApi";
import type { Muscle } from "../../types/allTypes";
import "./index.css";
//@ts-expect-error
import { BodyComponent } from "perform-body-component-lib";
import { store } from "../../store/store";
import router from "../../router";

const nameInjury = ref("");
const description = ref("");
const zone = ref("");
const date = ref("");
const state = ref("");

const handleInput = (name: string, valuePass: string | undefined | null) => {
  let value = valuePass as string;
  console.log(value)
  switch (name) {
    case "name":
      nameInjury.value = value;
      break;
    case "description":
      description.value = value;
      break;
    case "zone":
      zone.value = value;
      break;
    case "date":
      date.value = value;
      break;
    case "state":
      state.value = value;
      break;
    case undefined:
      state.value = "";
  }
  console.log('zone ', zone.value)
};

const user = ref({} as any);

const addInjurie = () => {
  post(
    "/injuries/",
    {
      body: {
        name: nameInjury.value,
        description: description.value,
        zone: zone.value,
        date: date.value,
        state: state.value,
        user: user.value.id,
      },
    },
    true
  ).then((res) => {
    if (res.status > 300) {
    } else {
      router.push("/list_injuries");
    }
  });
};

const injuries_state = ref([
  {
    code: "TR",
    name: "Soignée",
  },
  {
    code: "NT",
    name: "Pas soignée",
  },
  {
    code: "IP",
    name: "En cours",
  },
]);

const muscles = ref([] as Muscle[]);

onIonViewWillEnter(async () => {
  let storeUser = await store.get("user");
  if (storeUser !== "") {
    user.value = JSON.parse(storeUser).user;
  }
  const ionSelect = document.querySelectorAll(".custom-ion-select");
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
  get("/workzones/all", { body: {} }, false).then((res) => {
    console.log(res);
    muscles.value = res;
  });
});
</script>
