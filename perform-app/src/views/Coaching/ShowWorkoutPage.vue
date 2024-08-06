<style scoped>
ion-modal {
  --width: 80%;
  --height: 120px;
  --border-radius: 16px;
  --box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
}

.input-label-placement-start.sc-ion-input-md-h .input-wrapper.sc-ion-input-md{
    padding-inline-start: 0px !important;
    padding-inline-end: 0px !important;
}

.time-input :deep(.input-wrapper.sc-ion-input-md){
    padding-inline-start: 0px !important;
    padding-inline-end: 0px !important;
}

</style>

<template>
  <ion-page data-page="ShowWorkout">
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton url="/coaching" text="Retour" />
          <NavButton :url="'/workout_edit/' + workout.id" text="Modifier" :noIcon="true"/>
        </div>
        <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
          {{  workout.name }}
        </h1>
        <h5>
          {{ toFrenchDate() }}
        </h5>
        <div style="display:flex; flex-wrap:wrap">
          <ion-label position="stacked" style="width: 100%;">
            {{ workout.time_value }}
          </ion-label>
          <ion-label position="stacked" style="width: 100%;">
            {{workout.workout_description}}
          </ion-label>
        </div>
        <div style="display: flex; justify-content: space-between">
          <div style="width: 40%;">
            <ion-label position="stacked">RPE Cognitif</ion-label>
            <Jauge :value="workout.cognitive_rpe"/>
          </div>
          <div style="width: 40%;">
            <ion-label position="stacked">RPE Physique</ion-label>

            <Jauge :value="workout.physical_rpe"/>
          </div>
        </div>
        <div style="position: absolute; bottom : 10px; width: calc(100% - var(--pd-r) - var(--pd-l)); display: flex; justify-content: center;">
          <ion-button @click="() => deleteModal.$el.present()" color="danger" style="width: 100%">
            Supprimer
          </ion-button>
          <ion-modal ref="deleteModal" id="info_wellness_modal">
            <div>
              <h4 style="font-size : 15px; padding: 0px 20px;">Supprimer cet séance ?</h4>
            </div>
            <div style="position: absolute; bottom : 10px; width: calc(100%); display: flex; justify-content: space-around">
          <ion-button @click="() => deleteModal.$el.dismiss()" color="" style="width: 40%">
            Annuler
          </ion-button>
          <ion-button @click="deleteWorkout" color="danger" style="width: 40%">
            Supprimer
          </ion-button>
        </div>
          </ion-modal>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonContent,
  IonPage,
  IonLabel,
  onIonViewWillEnter,
  IonButton,
  IonModal
} from "@ionic/vue";
import "@/assets/base.css";
import "@/assets/main.css";
import NavButton from "../../components/NavButton/NavButton.vue";
import { ref } from "vue";
import "../Profile/index.css";
import { store } from "../../store/store";
import { useRoute } from "vue-router";
import { useRouter } from "vue-router";
import { useErrorHandler } from "../../lib/useErrorHandler";
import { get, del} from "../../lib/callApi";
import Jauge from "../../components/Jauge/Jauge.vue";

const { triggerError } = useErrorHandler() as any;
const router = useRoute();
const navRouter = useRouter();
const deleteModal = ref(null) as any;
const cognitive_rpe = ref(5); // Valeur initiale du slider
const physical_rpe = ref(5); // Valeur initiale du slider

const userLoggin = ref({
  user: {
    id: 0,
  },
}) as any;
const actualDate = ref('')
const workout = ref({
  id:0,
  name: "",
  date: actualDate.value as any,
  workout_description: "",
  cognitive_rpe: cognitive_rpe.value,
  physical_rpe: physical_rpe.value,
  time_value: "",
  user: 0,
});

const toFrenchDate = () => {
  const date = new Date(workout.value.date);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  const formattedDate = `${day}-${month}-${year}`;
  return formattedDate;
};

const deleteWorkout = () => {
  del(
    "/workout/" + router.params.id,
    true
  ).then((res) => {
    if (res.status && res.status > 300) {
      triggerError("Erreur à la suppression de l'entrainement");
    } else {
      navRouter.push('/coaching')
      deleteModal.value.$el.dismiss();
    }
  });
}

const loadWorkoutForDay = () => {
  get(
    "/workout/" + router.params.id,
    { body: {} },
    true
  ).then((res) => {
    if (res.status > 300) {
      triggerError("Erreur à la récupération de l'entrainement");
    } else {
      workout.value = res;
    }
  });
}

onIonViewWillEnter(async () => {
  const user = await store.get("user");
  userLoggin.value = JSON.parse(user);
  loadWorkoutForDay();
});
</script>
