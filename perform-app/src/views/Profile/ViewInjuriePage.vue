<style scoped></style>

<template>
  <ion-page data-page="show-injuries">
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton url="/list_injuries" text="Retour" back="" />
          <NavButton :disabled='injury.state == "TR"' @click="router.push('/edit_injurie/' + routerNav.params.id)"
            text="Editer" :noIcon="true" />
        </div>
        <h1 style="color: black; margin-top: 10px; margin-bottom: 5px">
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
            <ion-label :class="stateSetClass(injury.state)" class="injurie_state">{{ stateSet(injury.state)
              }}</ion-label>
          </div>
        </div>
        <div style="
            display: flex;
            width: 100%;
            margin-top: 40px;
            justify-content: center;
            align-items: center;
          ">
          <BodyComponent :muscleSelected="[{ zone: injury.zone }]" :height="'300'" :width="'200'" :viewOnly="'show'" />
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonContent, IonPage, IonLabel, onIonViewWillEnter } from "@ionic/vue";
import NavButton from "../../components/NavButton/NavButton.vue";
import { ref } from "vue";
import { useRoute } from "vue-router";
import router from "../../router";
//@ts-expect-error
import { BodyComponent } from 'perform-body-component-lib'
import "@/assets/base.css";
import "@/assets/main.css";
import "./index.css";
import { get } from "../../lib/callApi";
import { stateSet, stateSetClass } from "../../lib/injurie";
import { useErrorHandler } from '../../lib/useErrorHandler';

const { triggerError } = useErrorHandler() as any;

const routerNav = useRoute();

const injury = ref({
  name: "",
  description: "",
  state: "",
  date: "",
  zone: [{
    zone: {
      name: "",
      code: ""
    }
  }],
}) as any;
const id = ref<number>(0);

const back = ref<string>("back");
const urlReturn = ref<string>("/list_injuries");

/**
 * Exécute les actions nécessaires lors de l'entrée dans la vue.
 */
onIonViewWillEnter(() => {
  id.value = Number(routerNav.params.id);
  injury.value = {
    id: "",
    name: "",
    description: "",
    zone: [{
      zone: {
        name: "",
        code: ""
      }
    }],
    date: "",
    user: '',
    state: "",
  };
  if (routerNav.query.edit) {
    back.value = "";
    urlReturn.value += "?edit=true";
  }
  get("/injuries/" + id.value + "/", { body: {} }, true).then((res) => {
    if (res.status > 300) {
      triggerError('Erreur lors de la récupération des blessures');
    } else {
      injury.value = res;
    }
  });
});


</script>
