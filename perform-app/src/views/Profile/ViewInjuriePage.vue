<style scoped></style>

<template>
  <ion-page>
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton :url="urlReturn" text="Retour" :back="back" />
          <NavButton
            @click="router.push('/edit_injurie/' + routerNav.params.id)"
            text="Editer"
            :noIcon="true"
          />
        </div>
        <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
          {{ injury.name }}
        </h1>
        <p>
          {{
            injury.description == "" ? "Rien à signaler" : injury.description
          }}
        </p>
        <div class="injuriy_info">
          <div class="injury_item">
            <p>{{ injury.zone.name }}</p>
          </div>
          <div class="injury_item">
            <p>
              {{ new Date(injury.date).toLocaleString("fr").split(" ")[0] }}
            </p>
          </div>
          <div class="injury_item">
            <ion-label
              :class="stateSetClass(injury.state)"
              class="injurie_state"
              >{{ stateSet(injury.state) }}</ion-label
            >
          </div>
        </div>
        <div
          style="
            display: flex;
            width: 100%;
            margin-top: 40px;
            justify-content: center;
            align-items: center;
          "
        >
          <BodyComponent :height="'300'" :width="'200'" :viewOnly="'show'" />
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonContent, IonPage, IonLabel } from "@ionic/vue";
import NavButton from "../../components/NavButton/NavButton.vue";
import { ref, onMounted, onUpdated } from "vue";
import { useRoute } from "vue-router";
import router from "../../router";

//@ts-expect-error
import { BodyComponent } from "perform-body-component-lib";

import "@/assets/base.css";
import "@/assets/main.css";
import { get } from "../../lib/callApi";
import { Injurie } from "../../types/types";

import "./index.css";

const back = ref("back");
const urlReturn = ref("/list_injuries");

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

const routerNav = useRoute();

const injury = ref({
  name: "",
  description: "",
  state: "",
  date: "",
  zone: "",
});
const id = ref(0);

onMounted(() => {
  id.value = Number(routerNav.params.id);
  if (routerNav.query.edit) {
    back.value = "";
    urlReturn.value += "?edit=true";
  }
  get("/injuries/" + id.value + "/", { body: {} }, true).then((res) => {
    if (res.status > 300) {
    } else {
      injury.value = res;
    }
  });
});

const load = () => {
  id.value = Number(routerNav.params.id);
  get("/injuries/" + id.value + "/", { body: {} }, true).then((res) => {
    if (res.status > 300) {
    } else {
      injury.value = res;
    }
  });
};

onUpdated(() => {
  if (routerNav.name == "ViewInjurie") {
    load();
  }
});
</script>
