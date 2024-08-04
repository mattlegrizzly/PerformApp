<style scoped>
.time-input {
  display: flex;
  align-items: center;
  gap: 5px;
  justify-content: center;
  width: 100%;
  padding-bottom: 10px;
}

.time-input::v-deep .input-wrapper.sc-ion-input-ios {
  padding-inline-start: 0px !important;
  -webkit-padding-start: 0px !important;
  -webkit-padding-end: 0px !important;
  padding-inline-end: 0px !important;
}

.center-input {
  text-align: center;
}

.time-input ion-input {
  width: 3.5em;
  height: 4.5em;
}

.time-input span {
  font-size: 1.5em;
  line-height: 2;
}

.record-unit::part(native) {
  padding-left: 0 !important;
  padding-right: 0 !important;
}

#list-records::part(scroll) {
  overflow-y: hidden !important;
}

.time_input {
  border: solid 1px rgb(194, 194, 194);
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.range_inner {
  margin: 0px 20px 0px 20px;
  padding: 0 10px;
}

.range-labels {
  display: flex;
  justify-content: space-between;
  padding: 0 10px;
}

.range-label {
  font-size: 14px;
  text-align: center;
  width: 10%;
}

.difficulty-slider {
  --bar-background-active: transparent; /* Pour éviter le remplissage noir lors du drag */
  --bar-background: linear-gradient(
    to right,
    green,
    yellow,
    red
  ); /* Dégradé du slider */
  --knob-background: white; /* Couleur du bouton du slider */
  --knob-background-pressed: white; /* Couleur du bouton quand il est pressé */
  --knob-size: 16px; /* Taille du bouton */

  --ticks-background: rgba(0, 0, 0, 0.5); /* Garde les ticks visibles */
  --ticks-background-active: rgba(
    0,
    0,
    0,
    0.5
  ); /* Assure que les ticks restent visibles lorsqu'ils sont actifs */
  --ticks-width: 2px;
}
</style>

<template>
  <ion-page data-page="EditWorkout">
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton url="profile" text="Retour" back="back" />
        </div>
        <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
          Créer votre séance pour le <br />{{ toFrenchDate() }}
        </h1>
        <div class="input_injurie">
          <ion-label
            position="stacked"
            :class="errorAdd && workout.name == '' ? 'required_text' : ''"
            >Nom de la séance</ion-label
          >
          <ion-input
            :class="errorAdd && workout.name == '' ? 'required_class' : ''"
            type="text"
            label-placement="stacked"
            fill="outline"
            placeholder="Séance VMA"
            :value="workout.name"
            @ion-change="handleInput('name', $event.detail.value)"
          ></ion-input>
        </div>
        <div class="input_injurie">
          <ion-label position="stacked">Description de la séance</ion-label>

          <ion-textarea
          :value="workout.workout_description"
            variant="outlined"
            placeholder="Décrivez votre séance"
            @ion-change="handleInput('description', $event.detail.value)"
            :rows="4"
          >
          </ion-textarea>
        </div>
        <div class="input_injurie">
          <ion-label
            position="stacked"
            :class="errorAdd && workout.date == '' ? 'required_text' : ''"
            >Date</ion-label
          >
          <ion-input
            :class="errorAdd && workout.date == '' ? 'required_class' : ''"
            type="date"
            :value="workout.date"
            label-placement="stacked"
            fill="outline"
            :default="actualDate"
            placeholder="12/03/2023"
            @ion-change="handleInput('date', $event.detail.value)"
          ></ion-input>
        </div>
        <div>
          <ion-label
            position="stacked"
            :class="errorAdd && !isTimeIsEmpty() ? 'required_text' : ''"
            >Temps (en hh:mm:ss)</ion-label
          >

          <div class="time-input">
            <ion-input
              v-model="hours"
              aria-label="hours"
              type="number"
              :labelPlacement="undefined"
              placeholder="HH"
              maxLength="2"
              class="time_input"
              :max="23"
              :min="0"
              style="padding-inline-start: 0px; --padding-end: 0px"
              :class="errorAdd && !isTimeIsEmpty() ? 'required_class' : ''"
            >
            </ion-input
            >:
            <ion-input
              v-model="minutes"
              type="number"
              placeholder="MM"
              aria-label="minutes"
              :labelPlacement="undefined"
              maxLength="2"
              class="time_input"
              :max="59"
              :min="0"
              :class="errorAdd && !isTimeIsEmpty() ? 'required_class' : ''"
            ></ion-input
            >:
            <ion-input
              v-model="seconds"
              type="number"
              placeholder="SS"
              aria-label="secondes"
              :labelPlacement="undefined"
              maxLength="2"
              class="time_input"
              :max="59"
              :min="0"
              :class="errorAdd && !isTimeIsEmpty() ? 'required_class' : ''"
            ></ion-input>
          </div>
        </div>
        <div>
          <div class="input_injurie">
            <ion-label position="stacked">RPE Cognitif</ion-label>
            <!-- Labels des crans -->
            <div class="range-labels">
              <div v-for="num in 10" :key="num" class="range-label">
                {{ num }}
              </div>
            </div>

            <!-- Slider pour la difficulté de 1 à 10 -->
            <div class="range_inner">
              <ion-range
                v-model="workout.cognitive_rpe"
                aria-label="Difficulté"
                :ticks="true"
                :snaps="true"
                :min="1"
                :max="10"
                class="difficulty-slider"
                @ion-change="handleRange"
                id="cognitive"
              ></ion-range>
            </div>
          </div>
          <div class="input_injurie">
            <ion-label position="stacked">RPE Physique</ion-label>
            <!-- Labels des crans -->
            <div class="range-labels">
              <div v-for="num in 10" :key="num" class="range-label">
                {{ num }}
              </div>
            </div>

            <!-- Slider pour la difficulté de 1 à 10 -->
            <div class="range_inner">
              <ion-range
                v-model="workout.physical_rpe"
                aria-label="Difficulté"
                id="phsyical"
                :ticks="true"
                :snaps="true"
                :min="1"
                :max="10"
                @ion-change="handleRange"
                class="difficulty-slider"
              ></ion-range>
            </div>
          </div>
        </div>
        <div>
          <NavButton
            style="width: 100%; height: 40px; margin-top: 20px"
            @click="addWorkout"
            :disabled="adding"
            :text="adding ? 'Ajout en cours' : 'Modifier la séance'"
            :noIcon="true"
          />
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonContent,
  IonPage,
  IonInput,
  IonLabel,
  IonRange,
  IonTextarea,
  onIonViewWillEnter,
} from "@ionic/vue";
import "@/assets/base.css";
import "@/assets/main.css";
import NavButton from "../../components/NavButton/NavButton.vue";
import { ref, computed } from "vue";
import "../Profile/index.css";
import { store } from "../../store/store";
import { useRoute } from "vue-router";
import { useErrorHandler } from "../../lib/useErrorHandler";
import { useRouter } from 'vue-router';
import { get, patch } from "../../lib/callApi";

const { triggerError } = useErrorHandler() as any;
const router = useRoute();
const navRouter = useRouter();

const cognitive_rpe = ref(5); // Valeur initiale du slider
const physical_rpe = ref(5); // Valeur initiale du slider

const errorAdd = ref(false);

const hours = ref("");
const minutes = ref("");
const seconds = ref("");

const userLoggin = ref({
  user: {
    id: 0,
  },
}) as any;
const actualDate = ref('')
const workout = ref({
  id: 0,
  name: "",
  date: actualDate.value as any,
  workout_description: "",
  cognitive_rpe: cognitive_rpe.value,
  physical_rpe: physical_rpe.value,
  time_value: "",
  user: 0,
});


const adding = ref(false);

const addWorkout = () => {
  workout.value.user = userLoggin.value.user.id;
  workout.value.date = new Date(actualDate.value);
  const formattedTimeValue = formatDuration(timeValue.value);
  workout.value.time_value = formattedTimeValue;
  patch("/workout/" + workout.value.id + '/', { body: workout.value }, true).then((res) => {
    if(res.status > 300){
      triggerError(res.data)
    } else {
      navRouter.push('/workout_show/' + workout.value.id)
    }
  });
};

const isTimeIsEmpty = () => {
  return hours.value !== "" || minutes.value != "" || seconds.value != "";
};

const formatDuration = (time : any) => {
  console.log(time)
  const [hours, minutes, seconds] = time
    .split(":")
    .map((part : any) => part.padStart(2, "0"));

  // Format to HH:MM:SS
  const formattedDuration = `00 ${hours}:${minutes}:${seconds}`;
  return formattedDuration;
};

const timeValue = computed(() => {
  return `${hours.value}:${minutes.value}:${seconds.value}`;
});


const handleRange = (e: any) => {
  console.log(e.target.id);
  if (e.target.id === "cognitive") {
    cognitive_rpe.value = e.detail.value;
    workout.value.cognitive_rpe = e.detail.value;
  } else {
    physical_rpe.value = e.detail.value;
    workout.value.physical_rpe = e.detail.value;
  }
};

const handleInput = (
  name: string,
  valuePass: string | undefined | number | null
) => {
  console.log("oui");
  let value = valuePass as any;
  switch (name) {
    case "name":
      if (value[0])
        workout.value.name = value[0].toUpperCase() + value.slice(1);
      else workout.value.name = value;
      break;
    case "description":
      workout.value.workout_description = value;
      break;
    case "date":
      console.log(value);
      actualDate.value = value;
      break;
    case "cogntive":
      workout.value.cognitive_rpe = value;
      break;
    case "physical":
      workout.value.physical_rpe = value;
      break;
    case "time":
      console.log(value)
      workout.value.time_value = value;
      break;
    case undefined:
      break;
  }
};

const toFrenchDate = () => {
  const date = new Date(workout.value.date);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  const formattedDate = `${day}-${month}-${year}`;
  return formattedDate;
};

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
      const paramsDate = workout.value.date;
      const date = new Date(paramsDate);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, "0");
      const day = String(date.getDate()).padStart(2, "0");
      const formattedDate = `${year}-${month}-${day}`;
      actualDate.value = formattedDate;
      workout.value.date = formattedDate;
      hours.value = workout.value.time_value.split(':')[0]
      minutes.value = workout.value.time_value.split(':')[1]
      seconds.value = workout.value.time_value.split(':')[2]
    }
  });
}

onIonViewWillEnter(async () => {
  workout.value.name = '';
  workout.value.workout_description = '';
  cognitive_rpe.value = 5;
  physical_rpe.value = 5;
  hours.value = '';
  minutes.value = '';
  seconds.value = '';
  const user = await store.get("user");
  userLoggin.value = JSON.parse(user);
  adding.value = false;
  loadWorkoutForDay();
});
</script>
