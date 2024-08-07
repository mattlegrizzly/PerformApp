<template>
  <ion-page data-page="Coaching">
    <ion-content :fullscreen="true">
      <div style="box-shadow: 0px 4px 8px #d4d4d4">
        <div class="perform-page">
          <div>
            <div style="display: flex; justify-content: space-between">
              <h1
                style="
                  margin-top: 0px !important;
                  margin-bottom: 0px !important;
                  height: auto;
                  display: flex;
                  justify-content: center;
                  align-items: center;
                "
              >
                Entrainements
              </h1>
              <div
                style="
                  display: flex;
                  align-items: center;
                  justify-content: space-around;
                "
              >
                <ion-button
                  id="return_today"
                  style="
                    --background: white;
                    border-radius: 15px;
                    margin-right: 5px;
                  "
                  @click="resetToToday"
                >
                  <ion-icon :icon="todayOutline" />
                </ion-button>
                <ion-button @click="openCalendarModal">
                  <ion-icon :icon="calendarOutline" />
                </ion-button>
              </div>
            </div>
            <!-- Slider pour les jours de la semaine -->
            <!-- Affichage du mois en cours -->
            <div style="text-align: center; margin-bottom: 0px">
              <h2
                style="
                  margin-bottom: 0px;
                  margin-top: 10px;
                  font-size: 20px !important;
                  text-transform: capitalize;
                "
              >
                {{ currentMonth }}
              </h2>
            </div>
          </div>
        </div>

        <swiper
          v-if="weeks.length"
          :key="swiperKey"
          :initial-slide="3"
          :slides-per-view="7"
          :slides-per-group="7"
          :space-between="0"
          @slideChangeTransitionStart="beforeSlideChange"
          @slideChangeTransitionEnd="onSlideChange"
          :loop="true"
          class="swiper-container day_swiper"
        >
          <swiper-slide
            v-for="(day, index) in weeks"
            :key="index"
            @click="() => selectDay(day)"
          >
            <div
              class="day-card"
              :class="{ 'selected-day': isSelected(day) }"
              style="position: relative"
            >
              <div>{{ day.shortLabel }}</div>
              <div>{{ day.dayNumber }}</div>
              <div
                v-if="day.isWorkout"
                :style="{
                  color: isSelected(day) ? 'var(--primary-blue)' : 'white',
                }"
                style="position: absolute; top: -26px; font-size: 40px"
              >
                •
              </div>
            </div>
          </swiper-slide>
        </swiper>
      </div>

      <!-- Affichage du texte précis du jour sélectionné -->
      <div v-if="selectedDay" class="perform-page" style="height: calc(100vh - 242px - var(--pd-t))">
          <div v-for="workout of selectedWorkout">
            <div
              @click="router.push('/workout_show/' + workout.id)"
              class="workout_elem"
            >
              <div
                style="
                  display: flex;
                  justify-content: space-between;
                  align-items: center;
                "
              >
                <h5 style="margin: 0px">{{ workout.name }}</h5>
                <p style="margin: 0px">{{ workout.time_value }}</p>
              </div>
              <div style="display: flex; justify-content: space-between">
                <div style="width: 40%">
                  <ion-label position="stacked" style="padding-bottom: 10px">
                    RPE Physique :
                  </ion-label>
                  <Jauge :value="workout.physical_rpe" />
                </div>
                <div style="width: 40%; margin-right: 20px">
                  <ion-label position="stacked" style="padding-bottom: 10px">
                    RPE Cognitif :
                  </ion-label>
                  <Jauge :value="workout.cognitive_rpe" />
                </div>
              </div>
            </div>
          </div>
          <div v-if="selectedWorkout.length == 0" style="display: flex; align-items: center; height: 30%;">
            <h4 style="font-size: 16px; text-align: center; font-style: italic; font-weight: 400; color: gray;">
              Pas d'entraînements aujourd'hui ! <br>
              Saisissez votre premier entrainement de la journée !
            </h4>
        </div>
        <ion-button
          style="
            position: absolute;
            right: var(--pd-r);
            bottom: 80px;
          "
          @click="getUrlDate()"
        >
          <ion-icon :icon="addOutline"></ion-icon>
        </ion-button>
      </div>

      <!-- Modal pour le calendrier -->
      <ion-modal id="calendarModal" ref="calendarModal">
        <ion-content class="calendar-content">
          <vue-cal
            class="vue-cal"
            default-view="month"
            :disable-views="['years', 'year', 'week', 'day']"
            @cell-click="onDateSelected"
            @view-change="onViewChange"
            locale="fr"
            :selected-date="selectedDay ? selectedDay.fullDate : null"
            :start-date="selectedDay ? selectedDay.fullDate : null"
            :events="workoutEvents"
          >
          </vue-cal>
        </ion-content>
      </ion-modal>
    </ion-content>
  </ion-page>
</template>

<script setup>
import { ref, onMounted, nextTick, computed, watch } from "vue";
import {
  IonPage,
  IonLabel,
  IonContent,
  IonIcon,
  IonButton,
  IonModal,
  onIonViewWillEnter,
} from "@ionic/vue";
import {
  close,
  addOutline,
  calendarOutline,
  todayOutline,
} from "ionicons/icons";
import { Swiper, SwiperSlide } from "swiper/vue";
import NavButton from "../../components/NavButton/NavButton.vue";
import "swiper/swiper-bundle.css";
import { get } from "../../lib/callApi";
import { store } from "../../store/store";
import { useErrorHandler } from "../../lib/useErrorHandler";
import Jauge from "../../components/Jauge/Jauge.vue";
import { useRouter } from "vue-router";
import VueCal from "vue-cal";
import "vue-cal/dist/vuecal.css";
import "@/assets/base.css";
import "@/assets/main.css";

const router = useRouter();
const { triggerError } = useErrorHandler();
const isInitializing = ref(true); // Variable pour contrôler l'initialisation
const workoutEvents = ref([]);
const user = ref(null);
const selectedWorkout = ref(null);
const selectedDay = ref(null);
const calendarModal = ref(null);
const swiperKey = ref(0);
const weeks = ref([]);
const currentMonth = ref("");
const initialSelectedDay = ref(null);
const numWeeks = 9; // 3 semaines avant, 3 semaines après + semaine actuelle
const initialBufferWeeks = 3;

// Fonction pour générer les semaines avec un tampon
const generateWeeksWithBuffer = (startDate, numWeeks) => {
  const days = [];
  const current = new Date(startDate);

  // Ajuster la date au début de la semaine (lundi)
  const dayOfWeek = current.getDay();
  const diff = dayOfWeek === 0 ? -6 : 1 - dayOfWeek;

  current.setDate(current.getDate() + diff - initialBufferWeeks * 7); // Ajouter le tampon

  for (let week = 0; week < numWeeks; week++) {
    for (let i = 0; i < 7; i++) {
      const day = new Date(current);
      day.setDate(current.getDate() + week * 7 + i);
      days.push({
        label: day.toLocaleDateString("fr-FR", { weekday: "long" }),
        shortLabel: day
          .toLocaleDateString("fr-FR", { weekday: "short" })
          .slice(0, 3),
        dayNumber: day.getDate(),
        fullDate: new Date(day),
      });
    }
  }

  return days;
};

watch(weeks, () => {
  console.log(weeks.value);
});

const updateCurrentMonth = () => {
  if (weeks.value.length > 0) {
    currentMonth.value = selectedDay.value.fullDate.toLocaleDateString(
      "fr-FR",
      {
        month: "long",
        year: "numeric",
      }
    );
  }
};

const selectToday = () => {
  const today = new Date();
  selectedDay.value = weeks.value.find(
    (day) =>
      day.fullDate.toLocaleDateString("fr-FR", {
        day: "numeric",
        month: "long",
        year: "numeric",
      }) ===
      today.toLocaleDateString("fr-FR", {
        day: "numeric",
        month: "long",
        year: "numeric",
      })
  );
  updateCurrentMonth();
  loadWorkoutForDay();
};

const loadWorkoutForDay = () => {
  if (!selectedDay.value || !user.value) return;
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
};

const updateWorkoutEvents = () => {
  workoutEvents.value = weeks.value
    .filter((day) => day.isWorkout)
    .map((day) => ({
      start: day.fullDate,
      end: day.fullDate,
      title: "Workout",
      class: "workout-event",
    }));
  console.log(workoutEvents);
};

const onViewChange = (view) => {
  console.log("viewChange", view);
  if (view && view.startDate) {
    loadMonthlyWorkouts();
  }
};

const resetToToday = async () => {
  const today = new Date();
  weeks.value = generateWeeksWithBuffer(today, numWeeks);

  // Sélectionner le jour actuel
  const todayIndex = weeks.value.findIndex(
    (day) => day.fullDate.toLocaleDateString() === today.toLocaleDateString()
  );

  if (todayIndex !== -1) {
    selectDay(weeks.value[todayIndex]);

    // Repositionner Swiper sur la semaine actuelle
    nextTick(() => {
      const swiperInstance = document.querySelector(".swiper-container").swiper;
      if (swiperInstance) {
        swiperInstance.slideTo(Math.floor(todayIndex / 7) * 7, 0); // 0 désactive l'animation
      }
    });

    // Mettre à jour le mois affiché
    updateCurrentMonth();

    // Charger les séances pour le mois
    await loadMonthlyWorkouts();
    // Charger les séances pour la semaine
    //await loadWeeklyWorkouts(today);
  }
};

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
  updateCurrentMonth();
};

const beforeSlideChange = () => {
  // Capturer la date initiale avant le changement
  if (selectedDay.value) {
    initialSelectedDay.value = new Date(selectedDay.value.fullDate);
  } else {
    initialSelectedDay.value = null;
  }
};

const onSlideChange = async (swiper) => {
  if (isInitializing.value) return;

  const index = swiper.realIndex;
  const firstDayIndex = Math.floor(index / 7) * 7;
  let selectedDay = weeks.value[firstDayIndex];

  if (
    selectedDay.fullDate.getFullYear() > new Date().getFullYear() &&
    swiper.swipeDirection === "prev"
  ) {
    if (initialSelectedDay.value) {
      initialSelectedDay.value.setDate(initialSelectedDay.value.getDate() - 7);
      weeks.value = generateWeeksWithBuffer(initialSelectedDay.value, numWeeks);

      selectedDay = weeks.value.find(
        (day) =>
          day.fullDate.toLocaleDateString() ===
          initialSelectedDay.value.toLocaleDateString()
      );

      selectDay(selectedDay);
      updateCurrentMonth();

      nextTick(() => {
        swiper.slideTo(Math.floor(index / 7) * 7, 0);
      });

      return;
    }
  }

  // Sélectionner le jour calculé et mettre à jour le mois affiché
  selectDay(selectedDay);
  updateCurrentMonth();

  // Recharger les séances pour la semaine
  //await loadWeeklyWorkouts(selectedDay.fullDate);
  await loadMonthlyWorkouts();
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
  if (day.date) {
    selectedDate = new Date(day.date);
  } else {
    selectedDate = new Date(day);
  }

  // Générer les semaines à partir de la date sélectionnée
  weeks.value = generateWeeksWithBuffer(selectedDate, numWeeks);

  // Sélectionner le jour dans les semaines générées
  const selectedIndex = weeks.value.findIndex(
    (d) => d.fullDate.toLocaleDateString() === selectedDate.toLocaleDateString()
  );

  if (selectedIndex !== -1) {
    selectDay(weeks.value[selectedIndex]);

    // Repositionner manuellement Swiper sur la semaine contenant le jour sélectionné
    nextTick(() => {
      const swiperInstance = document.querySelector(".swiper-container").swiper;
      if (swiperInstance) {
        swiperInstance.slideTo(Math.floor(selectedIndex / 7) * 7, 0); // 0 désactive l'animation
      }
    });

    // Mise à jour du mois affiché
    loadMonthlyWorkouts();
    updateCurrentMonth();
  }

  closeCalendarModal(); // Fermer le modal du calendrier
};

const fetchWorkoutsForWeek = async (dateStr) => {
  try {
    // Assurez-vous que `dateStr` est bien formaté en `YYYY-MM-DD`
    const formattedDateStr = dateStr.replace(/\//g, "-");
    const response = await get(
      `/workout/workouts-for-week/?date_str=${formattedDateStr}`,
      { body: {} },
      true
    );

    return response;
  } catch (error) {
    console.error("Error fetching workouts for week:", error);
    return {};
  }
};

const fetchWorkoutsForMonth = async (year, month) => {
  try {
    const response = await get(
      `/workout/workouts-for-month/?year=${year}&month=${month}`,
      { body: {} },
      true
    );
    return response;
  } catch (error) {
    console.error("Error fetching workouts for month:", error);
    return {};
  }
};

const loadWeeklyWorkouts = async (startDate) => {
  console.log("loadWeek");
  // Assurez-vous que la date est au format YYYY-MM-DD
  const dateStr = startDate.toISOString().split("T")[0]; // Format YYYY-MM-DD
  const weekWorkouts = await fetchWorkoutsForWeek(dateStr);

  weeks.value.forEach((day) => {
    day["isWorkout"] = false;
    const dayStr = day.fullDate
      .toLocaleDateString("fr-FR", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
      })
      .split("/")
      .reverse()
      .join("-");
    day.isWorkout = weekWorkouts[dayStr] || false;
  });
};

const loadMonthlyWorkouts = async () => {
  const year = selectedDay.value.fullDate.getFullYear();
  const month = selectedDay.value.fullDate.getMonth() + 1; // Mois actuel

  const monthWorkouts = await fetchWorkoutsForMonth(year, month);

  // Mise à jour des semaines
  weeks.value.forEach((day) => {
    const dayStr = day.fullDate
      .toLocaleDateString("fr-FR", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
      })
      .split("/")
      .reverse()
      .join("-");
    day.isWorkout = monthWorkouts[dayStr] || false;
  });
  updateWorkoutEvents();
};
const isSwiperInitialized = ref(false); // Drapeau pour contrôler l'initialisation du Swiper

onIonViewWillEnter(async () => {
  if (!isSwiperInitialized.value) {
    const today = new Date();
    weeks.value = generateWeeksWithBuffer(today, numWeeks);

    await store.get("user").then((res) => {
      user.value = JSON.parse(res);
    });

    // Sélectionner le jour actuel ou le jour sélectionné précédemment
    const selectedIndex = weeks.value.findIndex((day) =>
      selectedDay.value
        ? day.fullDate.toLocaleDateString() ===
          selectedDay.value.fullDate.toLocaleDateString()
        : day.fullDate.toLocaleDateString() === today.toLocaleDateString()
    );

    if (selectedIndex !== -1) {
      selectDay(weeks.value[selectedIndex]);

      // Utiliser nextTick pour s'assurer que Swiper est bien monté avant de le repositionner
      nextTick(() => {
        const swiperInstance =
          document.querySelector(".swiper-container").swiper;
        if (swiperInstance) {
          swiperInstance.slideTo(Math.floor(selectedIndex / 7) * 7, 0); // Positionner Swiper sur la bonne semaine
        }
      });
    }

    isSwiperInitialized.value = true; // Marquer le Swiper comme initialisé
  }
  loadMonthlyWorkouts();
  loadWorkoutForDay();
});

onMounted(async () => {
  const today = new Date();
  weeks.value = generateWeeksWithBuffer(today, numWeeks);

  await store.get("user").then((res) => {
    user.value = JSON.parse(res);
  });

  // Charger les séances pour le mois
  await loadMonthlyWorkouts();
  // Charger les séances pour la semaine
  //await loadWeeklyWorkouts(today);

  // Sélectionner le jour actuel
  const todayIndex = weeks.value.findIndex(
    (day) => day.fullDate.toLocaleDateString() === today.toLocaleDateString()
  );

  if (todayIndex !== -1) {
    selectDay(weeks.value[todayIndex]);

    nextTick(() => {
      const swiperInstance = document.querySelector(".swiper-container").swiper;
      if (swiperInstance) {
        swiperInstance.slideTo(Math.floor(todayIndex / 7) * 7, 0);
      }
    });
  }

  isInitializing.value = false;
  loadWorkoutForDay();
});
</script>

<style scoped>
.day-card {
  text-align: center;
  height: 60px; /* Fixe la hauteur de chaque jour */
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  background-color: var(--primary-blue);
  color: white;
  width: calc(100% - 5px); /* Ajuste la largeur pour inclure l'espace */
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

.vue-call {
  padding: 10px;
}

#calendarModal {
  --min-height: 30%;
  --border-radius: 20px;
  --width: 80%;
  --max-height: 50%;
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
  max-height: calc(100%); /* Ajuste la hauteur maximale du calendrier */
}
</style>

<style>
.vuecal .vuecal__cell--selected {
  background-color: var(--primary-blue) !important;
  color: white !important; /* Assurez-vous également que le texte est visible */
  z-index: 2;
}

.vuecal .vuecal__cell--today {
  background-color: var(--primary-blue20) !important;
  color: black !important; /* Assurez-vous également que le texte est visible */
  z-index: 2;
}

.vuecal__cell-events-count {
  background-color: var(--primary-blue);
  border-radius: 50%;
  margin: auto;
}

.vuecal__flex .vuecal__menu {
  display: none;
}
</style>

<style>
#return_today::part(native) {
  color: var(--primary-blue) !important;
  border: 1px solid var(--primary-blue) !important;
}
</style>
