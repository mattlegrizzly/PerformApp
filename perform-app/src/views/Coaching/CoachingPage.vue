<template>
  <ion-page data-page="Coaching">
    <ion-content :fullscreen="true">
      <div class="perform-page">
        <div>
          <div style="display: flex; justify-content: space-between">
            <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
              Mes entrainements
            </h1>
            <div style="display: flex; align-items: center; justify-content: space-around;">
              <ion-button style="margin-right : 5px" @click="getUrlDate()">
                <ion-icon :icon="addOutline"></ion-icon>
              </ion-button>
              <ion-button @click="openCalendarModal">
                <ion-icon :icon="calendarOutline"></ion-icon>
              </ion-button>
            </div>
          </div>
          <!-- Slider pour les jours de la semaine -->
          <!-- Affichage du mois en cours -->
          <div style="text-align: center; margin-bottom: 10px;">
            <h2>{{ currentMonth }}</h2>
          </div>

          <swiper
            v-if="weeks.length"
            :key="swiperKey"
            :initial-slide="0" 
            :slides-per-view="7"
            :slides-per-group="7"
            :space-between="0"
            @slideChangeTransitionEnd="onSlideChange"
            :loop="true"
            class="swiper-container day_swiper"
          >
            <swiper-slide
              v-for="(day, index) in weeks"
              :key="index"
              @click="selectDay(day)"
            >
              <div class="day-card" :class="{ 'selected-day': isSelected(day) }">
                <div>{{ day.shortLabel }}</div>
                <div>{{ day.dayNumber }}</div>
              </div>
            </swiper-slide>
          </swiper>
        </div>

        <!-- Affichage du texte précis du jour sélectionné -->
        <div v-if="selectedDay">
          <div>
            <h2>{{ selectedDay.label }} {{ selectedDay.dayNumber }}</h2>
            <div v-for="workout of selectedWorkout">
              <div class="workout_elem">
                <h5 style="margin: 0px">{{ workout.name }}</h5>
                <p>{{ new Date(workout.date).toLocaleDateString("fr") }}</p>
                <p>{{ workout.workout_description }}</p>
                <div style="display: flex">
                  <div style="width: 40%; margin-right: 20px">
                    <ion-label position="stacked" style="padding-bottom: 10px">
                      RPE Cognitif :
                    </ion-label>
                    <Jauge :value="workout.cognitive_rpe" />
                  </div>
                  <div style="width: 40%">
                    <ion-label position="stacked" style="padding-bottom: 10px">
                      RPE Physique :
                    </ion-label>
                    <Jauge :value="workout.physical_rpe" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Modal pour le calendrier -->
        <ion-modal id="calendarModal" ref="calendarModal">
          <ion-content class="calendar-content">
            <div class="modal-header">
              <ion-button fill="clear" @click="closeCalendarModal">
                <ion-icon :icon="close"></ion-icon>
              </ion-button>
            </div>
            <vue-cal 
              class="vue-cal"
              default-view="month" 
              :disable-views="['years', 'year', 'week', 'day']"
              @cell-click="onDateSelected"
              locale="fr"
            />
          </ion-content>
        </ion-modal>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup>
import { ref, onMounted, nextTick, computed } from "vue";
import {
  IonPage,
  IonLabel,
  IonContent,
  IonIcon, 
  IonButton,
  IonModal, 
  onIonViewWillEnter
} from "@ionic/vue";
import { close, addOutline, calendarOutline } from "ionicons/icons";
import { Swiper, SwiperSlide } from "swiper/vue";
import NavButton from "../../components/NavButton/NavButton.vue";
import "swiper/swiper-bundle.css";
import { get } from "../../lib/callApi";
import { store } from "../../store/store";
import { useErrorHandler } from "../../lib/useErrorHandler";
import Jauge from "../../components/Jauge/Jauge.vue";
import { useRouter } from "vue-router";
import VueCal from 'vue-cal';
import 'vue-cal/dist/vuecal.css';

const router = useRouter()
const { triggerError } = useErrorHandler();

const user = ref(null);
const selectedWorkout = ref(null);
const selectedDay = ref(null);
const calendarModal = ref(null);
const swiperKey = ref(0);
const weeks = ref([]);
const currentMonth = ref("");

// Fonction pour générer les semaines et jours à partir d'une date de départ
const generateWeeksFromDate = (startDate, numWeeks) => {
  const days = [];
  const current = new Date(startDate);

  // Ajuster la date au début de la semaine (lundi)
  const dayOfWeek = current.getDay();
  const diff = dayOfWeek === 0 ? -6 : 1 - dayOfWeek;

  current.setDate(current.getDate() + diff);

  for (let week = 0; week < numWeeks; week++) {
    for (let i = 0; i < 7; i++) {
      const day = new Date(current);
      day.setDate(current.getDate() + week * 7 + i);
      days.push({
        label: day.toLocaleDateString("fr-FR", { weekday: "long" }),
        shortLabel: day.toLocaleDateString("fr-FR", { weekday: "short" }).slice(0, 3),
        dayNumber: day.getDate(),
        fullDate: new Date(day),
      });
    }
  }

  return days;
};

const numWeeks = 52;

const updateCurrentMonth = () => {
  if (weeks.value.length > 0) {
    const firstVisibleDate = weeks.value[0].fullDate;
    currentMonth.value = firstVisibleDate.toLocaleDateString("fr-FR", {
      month: "long",
      year: "numeric",
    });
  }
};

const selectToday = () => {
  const today = new Date();
  selectedDay.value = weeks.value.find(day => 
    day.fullDate.toLocaleDateString("fr-FR", {
      day: "numeric",
      month: "long",
      year: "numeric",
    }) === today.toLocaleDateString("fr-FR", {
      day: "numeric",
      month: "long",
      year: "numeric",
    })
  );
  updateCurrentMonth();
  loadWorkoutForDay();
};

const loadWorkoutForDay = () => {
  if (!selectedDay.value) return;
  get(
    "/workout/by-user-and-date?user_id=" +
      user.value.user.id +
      "&date=" +
      selectedDay.value.fullDate,
    { body: {} },
    true
  ).then((res) => {
    if (res.status > 300) {
      triggerError("Erreur à la récupération de l'entrainement");
    } else {
      selectedWorkout.value = res;
    }
  });
}

const getUrlDate = () => {
  if (selectedDay.value && selectedDay.value.fullDate) {
    router.push("/workout_add/" + selectedDay.value.fullDate);
  } else {
    router.push("/workout_add/null");
  }
};

const selectDay = (day) => {
  selectedDay.value = day;
  nextTick(() => {
    loadWorkoutForDay();
  });
};

const onSlideChange = (swiper) => {
  const index = swiper.realIndex;
  const firstDayIndex = Math.floor(index / 7) * 7;
  selectDay(weeks.value[firstDayIndex]);
  updateCurrentMonth();
};

const isSelected = (day) => {
  return (
    selectedDay.value &&
    day.fullDate.getTime() === selectedDay.value.fullDate.getTime()
  );
};

// Gestion de la modal pour le calendrier
const openCalendarModal = () => {
  calendarModal.value.$el.present();
};

const closeCalendarModal = () => {
  calendarModal.value.$el.dismiss();
};

const onDateSelected = async (day) => {
  let selectedDate;
  if(day.date){
    selectedDate = new Date(day.date);
  } else {
    selectedDate = new Date(day);
  }

  // Générer les semaines à partir de la date sélectionnée
  weeks.value = generateWeeksFromDate(selectedDate, numWeeks);

  // Incrémenter la clé pour recréer le Swiper
  swiperKey.value += 1;

  // Attendre le prochain cycle DOM pour recréer l'instance Swiper
  await nextTick();

  selectDay(weeks.value.find(d => 
    d.fullDate.toLocaleDateString() === selectedDate.toLocaleDateString()));  // Sélectionner le jour du vue-cal

  updateCurrentMonth();  // Mettre à jour le mois affiché

  closeCalendarModal();
};

// Initialisation lors du montage du composant
onMounted(async () => {
  weeks.value = generateWeeksFromDate(new Date(), numWeeks);
  await store.get("user").then((res) => {
    user.value = JSON.parse(res);
    selectToday();
  });
});

onIonViewWillEnter(() => {
  loadWorkoutForDay()
})
</script>

<style scoped>
.day-card {
  text-align: center;
  height: 80px; /* Fixe la hauteur de chaque jour */
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  background-color: var(--primary-blue);
  color: white;
  width: calc(100% - 13px); /* Ajuste la largeur pour inclure l'espace */
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  cursor: pointer;
}

.selected-day {
  background-color: white; /* Couleur grise pour le jour sélectionné */
  color: var(--primary-blue);
  border: solid 1px var(--primary-blue);
}

.day_swiper {
  padding-bottom: 10px;
  padding-top: 10px;
  padding-left: 6px;
}

.workout_elem {
  box-shadow: 0px 0px 5px 0px silver;
  padding: 10px 10px;
  align-items: space-between;
  border-radius: 10px;
  margin-bottom: 20px;
}

.vuecal__cell {
  cursor: pointer;
}

.vue-call{
  padding: 10px;
}

.vuecal__cell.is-selected {
  background-color: var(--ion-color-primary);
  color: white;
}

#calendarModal {
  --min-height: 30%;
  --border-radius: 20px;
  --width: 80%;
  --max-height: 55%;
  height: auto;
  --border-radius: 20px;
}

.calendar-content {
  display: flex;
  flex-direction: column;
  padding: 10px;
  height: 100%;
  box-sizing: border-box;
}

.modal-header {
  display: flex;
  justify-content: flex-end;
}

.vue-cal {
  flex: 1;
  max-height: calc(100% - 55px); /* Ajuste la hauteur maximale du calendrier */
}
</style>
