<style scoped></style>

<template>
  <ion-page style="background-color: white">
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton link="exercises" text="retour" back="back" />
          <ion-icon :icon="starOutline" size="large"></ion-icon>
        </div>
        <div class="info_wrapper">
          <div class="info_exercise">
            <h2>Matériels :</h2>
            <ion-chip
              v-for="element of exercises.material_exercise"
              color="primary"
              >{{ element.material.name }}</ion-chip
            >
          </div>
          <div class="info_exercise">
            <h2>Sports :</h2>
            <ion-chip
              v-for="element of exercises.sports_exercise"
              color="primary"
              >{{ element.sport.name }}</ion-chip
            >
          </div>
        </div>

        <h1 style="color: black; margin-top: 0px">{{ exercises.name }}</h1>
      </div>
      <div class="imageDiv">
        <video
          ref="videoController"
          id="player"
          playsinline
          data-poster="/path/to/poster.jpg"
          height="250"
          autoplay
          hideControl
          loop
          clickToPlay
        >
          <source :src="api_url + exercises.video" type="video/mp4" />
          <source :src="api_url + exercises.video" type="video/webm" />
        </video>
      </div>
      <ion-segment @ionChange="handleChange($event)" value="all">
        <ion-segment-button value="all">
          <ion-label>Instructions</ion-label>
        </ion-segment-button>
        <ion-segment-button value="favorites">
          <ion-label>Muscle</ion-label>
        </ion-segment-button>
      </ion-segment>
      <div class="perform-page">
        <div v-if="showExercises">
          <ion-list
            v-if="showExercises"
            class="list-item"
            :inset="true"
            v-for="step in exercises.steps_exercise"
            :key="step.id"
          >
            <ion-item>
              <ion-label>{{ step.text }}</ion-label>
              <ion-icon :icon="chevronForwardOutline"></ion-icon>
            </ion-item>
          </ion-list>
        </div>
        <div v-if="!showExercises" style="display: flex">
          <BodyComponent
            :height="'300'"
            :viewOnly="'show'"
            :muscleSelected="exercises.zone_exercises"
          />
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonPage,
  IonIcon,
  IonChip,
  IonContent,
  IonSegment,
  IonSegmentButton,
} from "@ionic/vue";
import { starOutline } from "ionicons/icons";
import "@/assets/base.css";
import "@/assets/main.css";
import { useRoute } from "vue-router";
import NavButton from "@/components/NavButton/NavButton.vue";
import "perform-body-component-lib/style.css";
import { BodyComponent } from "perform-body-component-lib";

import "./index.css";
const router = useRoute();
const api_url = import.meta.env.VITE_API_URL;

import { ref, onMounted } from "vue";
import { get } from "../../lib/callApi";
const exercises = ref({
  name: "",
  zone_exercises: [],
  video: "",
});
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
onMounted(() => {
  const id = router.params.id;
  get("/exercises/" + id + "/", { body: {} }, false).then((res: any) => {
    if (res.status > 300) {
    } else {
      exercises.value = res;
    }
    console.log(exercises.value);
  });
});
</script>
