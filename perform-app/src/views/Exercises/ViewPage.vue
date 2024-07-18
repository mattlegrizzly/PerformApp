<template>
  <ion-page data-page="ExerciseView" style="background-color: white">
    <ion-content id="view_page">
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton url="/exercises" text="Retour" />
          <ion-icon
            @click="setFav"
            :icon="is_fav ? heart : heartOutline"
            size="large"
            color="danger"
          ></ion-icon>
        </div>
        <h1
          style="
            color: black;
            margin-top: 5px;
            margin-bottom: 10px;
            font-size: 20px;
          "
        >
          {{ exercises.name }}
        </h1>
        <div class="info_wrapper">
          <div class="info_exercise">
            <ion-modal class="static-modal" ref="modalMaterial">
              <ion-content>
                <div style="padding: 10px">
                  <div
                    style="
                      display: flex;
                      justify-content: space-between;
                      align-items: center;
                      margin-bottom: 10px;
                    "
                  >
                    <h1 style="margin: 0px">Liste des matériels</h1>
                    <ion-icon
                      class="close-icon"
                      @click="modalMaterial ? modalMaterial.$el.dismiss() : ''"
                      :icon="close"
                    />
                  </div>
                  <div
                    style="width: 90%; padding-bottom: 5px"
                    v-for="element of exercises.material_exercise"
                  >
                    <ion-chip
                      style="
                        width: 100%;
                        padding-left: 10px;
                        padding-right: 10px;
                      "
                      color="primary"
                      >{{ element.material.name }}</ion-chip
                    >
                  </div>
                </div>
              </ion-content>
            </ion-modal>
            <h2 style="font-size: 14px">Matériels :</h2>
            <div style="display: flex">
              <ion-chip
                v-for="element of limitExerciseSport(
                  exercises.material_exercise
                )"
                color="primary"
                >{{ element.material.name }}</ion-chip
              >
              <div
                id="moreText"
                class="more-text"
                :style="
                  exercises.sports_exercise.length < 2
                    ? 'display:none;'
                    : 'display:block'
                "
                style="
                  font-size: 10px;
                  display: flex;
                  align-items: center;
                  margin-left: 5px;
                "
                @click="showModal(modalMaterial)"
              >
                Voir plus...
              </div>
            </div>
          </div>
          <div class="info_exercise">
            <h2 style="font-size: 14px">Sports :</h2>
            <div style="display: flex">
              <ion-modal class="static-modal" ref="modalSports">
                <ion-content>
                  <div style="padding: 10px">
                    <div
                      style="
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        margin-bottom: 10px;
                      "
                    >
                      <h1 style="margin: 0px">Liste des sports</h1>
                      <ion-icon
                        class="close-icon"
                        @click="modalSports ? modalSports.$el.dismiss() : ''"
                        :icon="close"
                      />
                    </div>
                    <div
                      style="width: 90%; padding-bottom: 5px"
                      v-for="element of exercises.sports_exercise"
                    >
                      <ion-chip
                        style="
                          width: 100%;
                          padding-left: 10px;
                          padding-right: 10px;
                        "
                        color="primary"
                        >{{ element.sport.name }}</ion-chip
                      >
                    </div>
                  </div>
                </ion-content>
              </ion-modal>
              <ion-chip
                v-for="element of limitExerciseSport(exercises.sports_exercise)"
                color="primary"
                >{{ element.sport.name }}</ion-chip
              >
              <div
                id="moreText"
                class="more-text"
                :style="
                  exercises.sports_exercise.length < 2
                    ? 'display:none;'
                    : 'display:block'
                "
                style="
                  font-size: 10px;
                  display: flex;
                  align-items: center;
                  margin-left: 5px;
                "
                @click="showModal(modalSports)"
              >
                Voir plus...
              </div>
            </div>
          </div>
        </div>
      </div>
      <transition mode="out-in" name="fade">
        <div
        :style="spinnerStyle"
          style="
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
          "
          key="spinner"
          v-if="loadVideo"
        >
          <v-progress-circular
            color="primary"
            indeterminate
          ></v-progress-circular>
        </div>
        <div v-else key="video" class="video-container" :style="spinnerStyle">
          <video
            ref="videoController"
            id="player"
            playsinline
            data-poster="/path/to/poster.jpg"
            width="100%"
            autoplay
            hideControl
            loop
            clickToPlay
            muted
          >
            <source :src="api_url + exercises.video" type="video/mp4" />
            <source :src="api_url + exercises.video" type="video/webm" />
          </video>
        </div>
      </transition>
      <v-tabs id="tabs-exercise" v-model="tab">
        <v-tab value="one">Instructions</v-tab>
        <v-tab value="two">Muscles</v-tab>
      </v-tabs>
      <div
        style="padding-top: 10px !important ; flex: 1; overflow: scroll"
        class="instructions"
      >
        <v-card-text>
          <v-tabs-window v-model="tab">
            <v-tabs-window-item value="one">
              <ion-list
                v-if="showExercises"
                class="list-item"
                style="
                  height: 45px;
                  margin-left: 0px !important;
                  margin-right: 0px !important;
                  display: flex;
                  flex-wrap: wrap;
                  height: auto;
                  margin-bottom: 20px;
                "
                :inset="true"
              >
                <ion-item
                  class="step_info"
                  v-for="(step, index) in exercises.steps_exercise"
                  :key="step.id"
                >
                  <div class="num_step">
                    {{ index + 1 }}
                  </div>
                  <ion-label>{{ step.text }}</ion-label>
                </ion-item>
              </ion-list>
            </v-tabs-window-item>
            <v-tabs-window-item
              value="two"
              style="display: flex; min-height: 250px"
            >
              <div
                style="
                  display: flex;
                  width: 50%;
                  justify-content: space-between;
                  align-items: center;
                "
              >
                <BodyComponent
                  :height="'200'"
                  :width="'100'"
                  :viewOnly="'show'"
                  :muscleSelected="exercises.zone_exercises"
                />
              </div>
              <div
                style="
                  width: 50%;
                  padding-left: 10px;
                  display: flex;
                  align-items: center;
                "
              >
                <ion-list style="width: 100%" class="muscles_list">
                  <ion-item
                    style="background-color: transparent"
                    v-for="muscle of exercises.zone_exercises"
                  >
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
  onIonViewWillEnter,
  onIonViewWillLeave,
  IonModal,
} from "@ionic/vue";
import { heartOutline, heart, close } from "ionicons/icons";
import NavButton from "../../components/NavButton/NavButton.vue";
//@ts-expect-error
import { BodyComponent } from "perform-body-component-lib";
import type { Step, Muscle } from "../../types/allTypes";

import { useRoute } from "vue-router";
import { ref , computed} from "vue";
import { get, post, del } from "../../lib/callApi";
import { store } from "../../store/store";

import "@/assets/base.css";
import "@/assets/main.css";
import "perform-body-component-lib/style.css";
import "./index.css";

import { useErrorHandler } from "../../lib/useErrorHandler";

const modalSports = ref(null) as any;
const modalMaterial = ref(null) as any;
const videoController = ref(null) as any;

const { triggerError } = useErrorHandler() as any;

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

const showVideo = ref(true);
const loadVideo = ref(true);
const id = ref(0);
const user_id = ref(0);
const is_fav = ref(false);
const fav_id = ref(0);

const showExercises = ref(true);

const limitExerciseSport = (elem: any) => {
  return elem.slice(0, 2);
};

const showModal = async (modal: any) => {
  modal.$el.present();
};

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
        triggerError("Erreur lors de l'ajout au favoris");
      } else {
        is_fav.value = true;
        fav_id.value = res.id;
      }
    });
  }
};

onIonViewWillLeave(() => {
  showVideo.value = false;
  loadVideo.value = false;
});

onIonViewWillEnter(() => {
  loadVideo.value = true;
  showVideo.value = true;
  is_fav.value = false;
  exercises.value.zone_exercises = [];
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
      if (res.status != undefined && res.status > 300) {
        triggerError("Erreur lors de la récupération des favoris");
        is_fav.value = false;
      } else if (res.length > 0) {
        fav_id.value = res[0].id;
        is_fav.value = true;
      }
    });
  });
  get("/exercises/" + id.value + "/", { body: {} }, false).then((res: any) => {
    if (res.status > 300) {
      triggerError("Erreur lors de l'ajout au favoris");
    } else {
      exercises.value = res;
      setTimeout(() => {
        loadVideo.value = false;
      }, 700);
    }
  });
});

const aspectRatio = 1080 / 1920; // Rapport d'aspect 16:9

const spinnerStyle = computed(() => {
  const width = videoController.value ? videoController.value.clientWidth : window.innerWidth;
  const height = width * aspectRatio;
  return {
    height: `${height}px`
  };
});
</script>

<style scoped>
ion-modal {
  --width: 80%;
  --height: 30%;
  --border-radius: 16px;
  --box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
}

.spinner-container, .video-container {
  width: 100%;
  position: relative;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
.fade-enter-to, .fade-leave-from {
  opacity: 1;
}
</style>
