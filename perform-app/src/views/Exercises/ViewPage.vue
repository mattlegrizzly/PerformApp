<style scoped></style>

<template>
  <ion-page style="background-color: white">
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton url='/exercises' text="Retour" />
          <ion-icon @click="setFav" :icon="is_fav ? star : starOutline" size="large"></ion-icon>
        </div>
        <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
          {{ exercises.name }}
        </h1>
        <div class="info_wrapper">
          <div class="info_exercise">
            <h2>Matériels :</h2>
            <ion-chip v-for="element of exercises.material_exercise" color="primary">{{ element.material.name
              }}</ion-chip>

          </div>
          <div class="info_exercise">
            <h2>Sports :</h2>
            <ion-chip v-for="element of exercises.sports_exercise" color="primary">{{ element.sport.name }}</ion-chip>
          </div>
        </div>
      </div>
      <div class="imageDiv">
        <video ref="videoController" id="player" playsinline data-poster="/path/to/poster.jpg" height="250" autoplay
          hideControl loop clickToPlay>
          <source :src="api_url + exercises.video" type="video/mp4" />
          <source :src="api_url + exercises.video" type="video/webm" />
        </video>
      </div>
      <v-tabs id="tabs-exercise" v-model="tab">
        <v-tab value="one">Instructions</v-tab>
        <v-tab value="two">Muscles</v-tab>
      </v-tabs>
      <div style="padding-top: 10px !important" class="instructions">
        <v-card-text>
          <v-tabs-window v-model="tab">
            <v-tabs-window-item value="one">
              <ion-list v-if="showExercises" class="list-item" style="
                  height: 45px;
                  margin-left: 0px !important;
                  margin-right: 0px !important;
                " :inset="true" v-for="(step, index) in exercises.steps_exercise" :key="step.id">
                <ion-item class="step_info">
                  <div class="num_step">
                    {{ index + 1 }}
                  </div>
                  <ion-label>{{ step.text }}</ion-label>
                </ion-item>
              </ion-list>
            </v-tabs-window-item>
            <v-tabs-window-item value="two" style="display: flex; min-height: 300px">
              <div style="
                  display: flex;
                  width: 50%;
                  margin-top: 16px;
                  justify-content: space-between;
                  align-items: center;
                ">
                <BodyComponent :height="'200'" :width="'100'" :viewOnly="'show'"
                  :muscleSelected="exercises.zone_exercises" />
              </div>
              <div style="width: 50%; display: flex; align-items: center">
                <ion-list style="width: 100%" class="muscles_list">
                  <ion-item style="background-color: transparent" v-for="muscle of exercises.zone_exercises">
                    <ion-label style="font-size: 14px">
                      {{ muscle.zone.name }}
                    </ion-label>
                  </ion-item>
                </ion-list>
              </div>
            </v-tabs-window-item>
          </v-tabs-window>
        </v-card-text>
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
  IonList,
  IonLabel,
  IonItem,
} from "@ionic/vue"
import { starOutline, star } from "ionicons/icons";
import NavButton from "../../components/NavButton/NavButton.vue";
//@ts-expect-error
import { BodyComponent } from "perform-body-component-lib";

import type { Step, Muscle } from "../../types/types";

import { useRoute } from "vue-router";
import { ref, onMounted } from "vue";
import { get, post, del } from "../../lib/callApi";
import { store } from "../../store/store";

import "@/assets/base.css";
import "@/assets/main.css";
import "perform-body-component-lib/style.css";
import "./index.css";

const router = useRoute();
const api_url = import.meta.env.VITE_API_URL;
const tab = ref(null);
const exercises = ref({
  name: "",
  zone_exercises: [] as Muscle[],
  video: "",
  steps_exercise: [] as Step[],
  material_exercise: [] as any,
  sports_exercise: [] as any,
});

const id = ref(0);
const user_id = ref(0);
const is_fav = ref(false);
const fav_id = ref(0);

const showExercises = ref(true);

const setFav = () => {
  if (is_fav.value) {
    del("/userfavexercises/" + fav_id.value + "/", true).then(() => {
      is_fav.value = false;
    });
  } else {
    post(
      "/userfavexercises/",
      {
        body: {
          user: Number(user_id.value),
          fav_exercise: Number(id.value),
        },
      },
      true
    ).then((res: any) => {
      if (res.status > 300) {
      } else {
        is_fav.value = true;
        fav_id.value = res.id;
      }
    });
  }
};

onMounted(() => {
  id.value = Number(router.params.id);
  store.get("user").then((res) => {
    user_id.value = JSON.parse(res).user.id;
    get(
      "/userfavexercises/user/" +
      user_id.value +
      "/?exercise_id=" +
      Number(id.value),
      { body: {} },
      true
    ).then((res: any) => {
      if (res.status > 300 || res.length <= 0) {
        is_fav.value = false;
      } else {
        fav_id.value = res[0].id;
        is_fav.value = true;
      }
    });
  });
  get("/exercises/" + id.value + "/", { body: {} }, false).then((res: any) => {
    if (res.status > 300) {
    } else {
      exercises.value = res;
      console.log(exercises.value.zone_exercises)
    }
  });
});
</script>
