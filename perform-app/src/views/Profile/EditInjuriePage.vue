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
          Modifier une blessure
        </h1>
        <div class="input_injurie">
          <ion-label>Nom de la blessure</ion-label>
          <ion-input
            label-placement="stacked"
            fill="outline"
            :value="injury.name"
            @ion-change="handleInput('name', $event.detail.value)"
            placeholder="Déchirure du quadriceps"
          ></ion-input>
        </div>
        <div class="input_injurie">
          <ion-label>Description de la blessure</ion-label>

          <ion-textarea
            :value="injury.description"
            variant="outlined"
            placeholder="Décrivez votre blessure"
            @ion-change="handleInput('description', $event.detail.value)"
          >
          </ion-textarea>
        </div>

        <div class="input_injurie">
          <ion-label>Zone de la blessure</ion-label>

          <ion-list class="filter-item">
            <ion-item>
              <ion-select
                interface="popover"
                placeholder="Zone de la blessure"
                class="custom-ion-select"
                :toggle-icon="chevronDownOutline"
                justify="space-between"
                :value="injury.zone.code"
                @ion-change="handleInput('zone', $event.detail.value)"
              >
                <ion-select-option
                  v-for="elem in muscles"
                  :key="elem.code"
                  :value="elem.code"
                  >{{ elem.name }}</ion-select-option
                >
              </ion-select>
            </ion-item>
          </ion-list>
        </div>
        <div class="input_injurie">
          <ion-label>Date de la blessure</ion-label>
          <ion-input
            type="date"
            label-placement="stacked"
            fill="outline"
            placeholder="2021-09-01"
            :value="injury.date"
            @ion-change="handleInput('date', $event.detail.value)"
          ></ion-input>
        </div>
        <div class="input_injurie">
          <ion-label>Etat de la blessure</ion-label>
          <ion-list class="filter-item">
            <ion-item>
              <ion-select
                :value="injury.state"
                interface="popover"
                placeholder="Etat de la blessure"
                class="custom-ion-select"
                :toggle-icon="chevronDownOutline"
                justify="space-between"
                @ion-change="handleInput('state', $event.detail.value)"
              >
                <ion-select-option
                  v-for="elem in injuries_state"
                  :key="elem.code"
                  :value="elem.code"
                  >{{ elem.name }}</ion-select-option
                >
              </ion-select>
            </ion-item>
          </ion-list>
        </div>
        <div
          style="
            display: flex;
            width: 100%;
            margin-top: 16px;
            justify-content: center;
            align-items: center;
          "
        >
          <BodyComponent :height="'200'" :width="'100'" :viewOnly="'show'" />
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
  IonLabel,
} from "@ionic/vue";
import "@/assets/base.css";
import "@/assets/main.css";
import { chevronDownOutline } from "ionicons/icons";
//@ts-expect-error
import NavButton from "../../components/NavButton/NavButton.vue";
import { onMounted, ref } from "vue";
import { get, patch } from "../../lib/callApi";
import type { Muscles } from "../../types/allType";
import "./index.css";
//@ts-expect-error
import { BodyComponent } from "perform-body-component-lib";
import { store } from "../../store/store";
import router from "../../router";
import { useRoute } from "vue-router";
import { onUpdated } from "vue";

const navRoute = useRoute();

const injury = ref({
  name: "",
  description: "",
  zone: "",
  date: "",
  state: "",
});

const handleInput = (name: string, value: string) => {
  switch (name) {
    case "name":
      injury.value.name = value;
      break;
    case "description":
      injury.value.description = value;
      break;
    case "zone":
      injury.value.zone.code = value;
      break;
    case "date":
      injury.value.date = value;
      break;
    case "state":
      injury.value.state = value;
      break;
  }
};

const user = ref({} as any);
const id = ref(0);
const addInjurie = () => {
  patch(
    "/injuries/" + id.value + "/",
    {
      body: {
        name: injury.value.name,
        description: injury.value.description,
        zone: injury.value.zone.code,
        date: injury.value.date,
        state: injury.value.state,
        user: user.value.id,
      },
    },
    true
  ).then((res) => {
    console.log(res);
    if (res.status > 300) {
    } else {
      router.push("/view_injuries/" + id.value + "/?edit=true");
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

const muscles = ref([] as Muscles[]);

const load = () => {
  store.get("user").then((res) => {
    const storeUser = res;
    if (storeUser !== "") {
      user.value = JSON.parse(storeUser).user;
      get("/injuries/" + id.value + "/", { body: {} }, true).then((res) => {
        if (res.status > 300) {
        } else {
          injury.value = res;
        }
      });
    }
  });
};

onUpdated(() => {
  if (navRoute.name == "EditInjurie") {
    load();
  }
});

onMounted(async () => {
  id.value = Number(navRoute.params.id);
  store.get("user").then((res) => {
    const storeUser = res;
    if (storeUser !== "") {
      user.value = JSON.parse(storeUser).user;
      get("/injuries/" + id.value + "/", { body: {} }, true).then((res) => {
        if (res.status > 300) {
        } else {
          injury.value = res;
        }
      });
    }
  });
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
  get("/workzones", { body: {} }, false).then((res) => {
    console.log(res);
    muscles.value = res.results;
  });
});
</script>
