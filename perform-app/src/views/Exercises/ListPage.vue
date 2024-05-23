<style scoped></style>

<template>
  <ion-page>
    <div id="header-wrapper">
      <div class="perform-page">
        <h1 style="margin-top: 0px">Liste exercices</h1>
        <ion-label>Rechercher un exercice :</ion-label>
        <ion-input id="search-input" label-placement="floating" fill="outline" placeholder="Cherchez un exercice"
          shape="round"></ion-input>
        <div class="filter-div">
          <ion-button>Filtres</ion-button>
          <ion-list class="filter-item">
            <ion-item>
              <ion-select aria-label="Trier par" interface="popover" placeholder="Trier par">
                <ion-select-option v-for="order in order" :key="order.id" :value="order.id">{{ order.value
                  }}</ion-select-option>
              </ion-select>
            </ion-item>
          </ion-list>
        </div>
      </div>
      <ion-segment @ionChange="handleChange($event)" value="all">
        <ion-segment-button value="all">
          <ion-label>Tous les exercices</ion-label>
        </ion-segment-button>
        <ion-segment-button value="favorites">
          <ion-label>Mes favoris</ion-label>
        </ion-segment-button>
      </ion-segment>
    </div>

    <ion-content color="light">
      <ion-list v-if="showExercises" class="list-item" :inset="true" v-for="exercise in exercises" :key="exercises.id"
        @click="goPage(exercise.id)">
        <ion-item>
          <div class="exercice-img">
            <label>{{ exercise.name[0] }}</label>
          </div>
          <ion-label>{{ exercise.name }}</ion-label>
          <ion-icon :icon="chevronForwardOutline"></ion-icon>
        </ion-item>
      </ion-list>
      <ion-list v-if="!showExercises" class="list-item" :inset="true" v-for="exercise in exercises" :key="exercises.id">
        <ion-item>
          <div class="exercice-img">
            <label>oui</label>
          </div>
          <ion-label>oui</ion-label>
          <ion-icon :icon="chevronForwardOutline"></ion-icon>
        </ion-item>
        <ion-item>
          <div class="exercice-img">
            <label>{{ exercise.name[0] }}</label>
          </div>
          <ion-label>{{ exercise.name }}</ion-label>
          <ion-icon :icon="chevronForwardOutline"></ion-icon>
        </ion-item>
      </ion-list>
    </ion-content>
  </ion-page>
</template>

<script lang="ts" setup>
import {
  IonLabel,
  IonList,
  IonItem,
  IonSegment,
  IonSegmentButton,
  IonIcon,
  IonInput,
  IonContent,
  IonPage,
  IonSelect,
  IonSelectOption,
  IonButton
} from "@ionic/vue";
import { get } from "@/lib/callApi.ts";
import { onMounted, ref } from "vue";
import { chevronForwardOutline } from "ionicons/icons";

const order = [
  { id: "orderByNameAsc", value: "Nom (Croissant)" },
  { id: "orderByNameDesc", value: "Nom (Décroissant)" },
  { id: "orderByIdAsc", value: "Id (Croissant)" },
  { id: "orderByIdDesc", value: "Id (Décroissant)" },
  { id: "orderByDateAsc", value: "Date (Croissant)" },
  { id: "orderByDateDesc", value: "Date (Décroissant)" },
  { id: "default", value: "Par défaut" },
];

const goPage = (id: any) => {
  console.log(id);
  router.push({ name: "ExercisesView", params: { id: id } });
};

const handleChange = (event: any) => {
  console.log("event", event.detail.value);
  if (event.detail.value == "all") {
    showExercises.value = true;
  } else {
    showExercises.value = false;
  }
  console.log("event", showExercises.value);
};
const showExercises = ref(true);
const exercises: any = ref([]);

import "./index.css";
import router from "../../router";

onMounted(() => {
  get("/exercises", { body: {} }, false, false).then((res: any) => {
    if (res.status > 300) {
    } else {
      exercises.value = res.results;
    }
  });
});
</script>
