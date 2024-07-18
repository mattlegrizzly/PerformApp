<template>
  <ion-page style="padding-top: 0px !important" data-page="Home">
    <ion-content>
      <div class="home_div">
        <div class="header_img">
          <img width="200px" src="@/assets/logo_perform.png" alt="logo" />
        </div>
        <div class="block_100">
          <div class="div_info">
            <h1>
              Salut <br />
              {{ user.last_name }} !
            </h1>
            <p>
              {{ new Date(Date.now()).toLocaleString("fr").split(" ")[0] }}
            </p>
          </div>
          <div class="profile_picture">
            <div v-if="!profilePicture" class="profile_placeholder">
              {{ user.first_name[0] }}
            </div>
            <img
              v-else
              :src="profilePicture"
              alt="profile"
              class="profile_img"
            />
          </div>
        </div>
        <div
          :class="
            hideWellness
              ? 'block_100 wellness_100 wellness_100_hidden'
              : 'block_100 wellness_100'
          "
        >
          <div class="display_flex" @click="hideWellness = !hideWellness">
            <h3>Wellness</h3>
            <ion-icon
              :icon="hideWellness ? chevronUpOutline : chevronDownOutline"
            />
          </div>
          <ion-modal ref="modal" id="set_wellness">
            <ion-content>
              <div class="modal-header" style="display: flex">
                <h3 style="width: 90%; font-size: 16px">
                  Saisissez le wellness du jour :
                </h3>
                <ion-icon class="close-icon" @click="dismiss" :icon="close" />
              </div>
              <div class="divs_range">
                <WellnessRange
                  id="sleep_range"
                  title="Sommeil"
                  :value="wellness.sleep"
                  :min="0"
                  :max="10"
                  descriptionStart="Très mauvais"
                  descriptionEnd="Excellent"
                  @change="onIonChange($event, 'sleep')"
                />
                <WellnessRange
                  id="fatigue_range"
                  title="Fatigue"
                  :value="wellness.fatigue"
                  :min="0"
                  :max="10"
                  descriptionStart="Epuisé"
                  descriptionEnd="Je pète la forme"
                  @change="onIonChange($event, 'fatigue')"
                />
                <WellnessRange
                  id="pain_range"
                  title="Douleurs"
                  :value="wellness.pain"
                  :min="0"
                  :max="10"
                  descriptionStart="Aucune"
                  descriptionEnd="Extrême"
                  @change="onIonChange($event, 'pain')"
                />
                <WellnessRange
                  id="stress_range"
                  title="Stress"
                  :value="wellness.stress"
                  :min="0"
                  :max="10"
                  descriptionStart="Aucun"
                  descriptionEnd="Extrême"
                  @change="onIonChange($event, 'stress')"
                />
                <WellnessRange
                  id="hydratation_range"
                  title="Hydratation"
                  :value="wellness.hydratation"
                  :min="0"
                  :max="10"
                  descriptionStart="-1L"
                  descriptionEnd="+3L"
                  @change="onIonChange($event, 'hydratation')"
                />
                <div
                  class="display_flex"
                  style="justify-content: center; margin-top: 10px"
                >
                  <ion-button v-if="wellnessNot" @click="postWellness">
                    Enregistrer
                  </ion-button>
                  <ion-button size="small" v-else @click="patchWellness">
                    Mettre à jour
                  </ion-button>
                </div>
              </div>
            </ion-content>
          </ion-modal>
          <ion-modal class="static-modal" ref="modalStats">
            <ion-content>
              <div class="modal-header">
                <ion-icon
                  class="close-icon"
                  @click="modalStats ? modalStats.$el.dismiss() : ''"
                  :icon="close"
                />
                <div
                  style="
                    width: 100%;
                    display: flex;
                    margin-top: 10px;
                    justify-content: space-between;
                  "
                >
                  <h3>Satistiques :</h3>
                  <ion-list>
                    <ion-item>
                      <ion-select
                        aria-label="Visions"
                        interface="popover"
                        placeholder="Période"
                        :value="period"
                        @ion-change="handleChartChange($event.detail.value)"
                      >
                        <ion-select-option value="week"
                          >Semaines</ion-select-option
                        >
                        <ion-select-option value="month"
                          >Mois</ion-select-option
                        >
                      </ion-select>
                    </ion-item>
                  </ion-list>
                </div>
              </div>
              <div class="modal-body">
                <h4 v-if="period == 'week'">Semaine du {{ weekRange }}</h4>
                <h4 v-else>{{ getMonthAndYear() }}</h4>

                <div>
                  <canvas
                    width="300px"
                    height="200px"
                    min="0"
                    max="10"
                    id="acquisitions"
                  ></canvas>
                </div>
                <div v-if="period == 'week'" class="week-navigation">
                  <ion-button @click="setPreviousWeek" fill="solid">
                    < Semaine précédente</ion-button
                  >
                  <ion-button
                    :disabled="
                      getWeekNumber(new Date(Date.now())) ==
                      getWeekNumber(tempDate)
                    "
                    @click="setNextWeek"
                    fill="solid"
                    >Semaine suivante ></ion-button
                  >
                </div>
                <div v-else class="week-navigation">
                  <ion-button @click="setPreviousMonth" fill="solid">
                    < Mois précédent</ion-button
                  >
                  <ion-button
                    :disabled="isMonthBeforeTempDate()"
                    @click="setNextMonth"
                    fill="solid"
                    >Mois suivant ></ion-button
                  >
                </div>
              </div>
              <div style="display: flex; justify-content: center">
                <ion-button
                  @click="
                    () => {
                      tempDate = new Date(Date.now());
                      if (period === 'week') {
                        updateWeekWellness();
                      } else {
                        updateMonthWellness();
                      }
                    }
                  "
                  fill="outline"
                  size="small"
                  >Revenir
                  {{
                    period == "week"
                      ? "à la semaine actuelle"
                      : "au mois actuel"
                  }}</ion-button
                >
              </div>
            </ion-content>
          </ion-modal>

          <div v-if="wellnessNot">
            <p style="text-align: center; margin-top: 10px; font-size: 16px">
              Saisissez votre wellness du jour !
              <ion-button
                id="open-modal"
                @click="
                  () => {
                    modal.$el.present();
                  }
                "
                expand="block"
                >Saisir le wellness</ion-button
              >
            </p>
          </div>
          <div
            v-else
            class="divs_range show_divs_range"
            :class="hideWellness ? 'show_divs_range_hidden' : ''"
          >
            <WellnessRange
              id="sleep_range"
              title="Sommeil"
              :value="wellness.sleep"
              :min="0"
              :max="10"
              disabled
              descriptionStart="Très mauvais"
              descriptionEnd="Excellent"
            />
            <WellnessRange
              id="fatigue_range"
              title="Fatigue"
              :value="wellness.fatigue"
              :min="0"
              :max="10"
              descriptionStart="Epuisé"
              descriptionEnd="Je pète la forme"
              disabled
            />
            <WellnessRange
              id="pain_range"
              title="Douleurs"
              :value="wellness.pain"
              :min="0"
              :max="10"
              descriptionStart="Aucune"
              descriptionEnd="Extrême"
              disabled
            />
            <WellnessRange
              id="stress_range"
              title="Stress"
              :value="wellness.stress"
              :min="0"
              :max="10"
              descriptionStart="Aucun"
              descriptionEnd="Extrême"
              disabled
            />
            <WellnessRange
              id="hydratation_range"
              title="Hydratation"
              :value="wellness.hydratation"
              :min="0"
              :max="10"
              descriptionStart="-1L"
              descriptionEnd="+3L"
              disabled
            />
            <div class="actions">
              <ion-button size="small" fill="outline" @click="showStats"
                >Statistiques</ion-button
              >
              <ion-button size="small" @click="modal.$el.present()"
                >Editer</ion-button
              >
            </div>
          </div>
        </div>
        <div class="block_100">
          <h3>Postural scoring</h3>
          <h4>Dernier en date : 26/02/2024</h4>
          <div v-if="wellnessNot"></div>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonButton,
  IonIcon,
  IonModal,
  IonContent,
  IonPage,
  onIonViewWillLeave,
  onIonViewWillEnter,
  IonList,
  IonSelect,
  IonSelectOption,
  IonItem,
} from "@ionic/vue";
import "@/assets/base.css";
import "@/assets/main.css";
import "./homepage.css";
import { ref, computed, markRaw } from "vue";
import { store } from "../../store/store";
import { close, chevronDownOutline, chevronUpOutline } from "ionicons/icons";
import { patch, post, get } from "../../lib/callApi";
import WellnessRange from "@/components/WellnessRange/WellnessRange.vue";
import Chart from "chart.js/auto";
import { useErrorHandler } from "../../lib/useErrorHandler";

const { triggerError } = useErrorHandler() as any;
const api = import.meta.env.VITE_API_URL;

const period = ref("week");

//On retrouve ici l'ensemble de nos ref utilisés dans cette page
const hideWellness = ref(false);
const wellnessNot = ref(true);
const weekWellness: any = ref([]);
const weekWellnessTemp: any = ref([]);
const monthWellnessTemp: any = ref([]);
const tempDate: any = ref(new Date(Date.now()));
const wellness = ref({
  sleep: 0,
  stress: 0,
  hydratation: 0,
  pain: 0,
  fatigue: 0,
  id: 0,
} as any);

const chart = ref(null) as any;
const modal = ref(null) as any;
const modalStats = ref(null) as any;

const user = ref({
  age: 0,
  weight: 0,
  size: 0,
  email: "",
  first_name: "",
  gender: "",
  id: 1,
  last_name: "",
  profile_picture: "",
  sports_user: [] as any,
  user_injuries: [],
  users_wellness: [],
});

/**
 * Fonction qui permet d'afficher les dates de début et de fin de la semaine pour le wellness
 */
 const weekRange = computed(() => {
  const start = new Date(weekWellnessTemp.value[0].date);
  const end = new Date(weekWellnessTemp.value[6].date);

  const formatWithLeadingZero = (number : number) => number.toString().padStart(2, '0');

  return `${start.getDate()}/${formatWithLeadingZero(start.getMonth() + 1)} au ${end.getDate()}/${
    formatWithLeadingZero(end.getMonth() + 1)
  }`;
});

/**
 * Fonction qui affiche la modal de définition du wellness
 */
const dismiss = () => {
  if (modal.value) {
    modal.value.$el.dismiss();
  }
};

/**
 * Fonction de conversion d'une date pour la récupérer sans la partie heure
 * @param date
 */
const setLongDate = (date: any) => {
  return date.toISOString().split("T")[0];
};

/**
 * Fonction permettant la création du wellness du jour
 */
const postWellness = async () => {
  const response = await post(
    "/wellness/",
    {
      body: {
        sleep: wellness.value.sleep,
        hydratation: wellness.value.hydratation,
        fatigue: wellness.value.fatigue,
        pain: wellness.value.pain,
        stress: wellness.value.stress,
        user: user.value.id,
        date: setLongDate(new Date()),
      },
    },
    true
  );

  if (!response.status) {
    const userResponse = await get("/users/me/", { body: {} }, true);
    if (userResponse.status > 301) {
      triggerError("Erreur lors de la récupération de l'utilisateur");
    } else {
      await store.set("user", JSON.stringify(userResponse));
      wellness.value = response;
      wellnessNot.value = false;
      modal.value.$el.dismiss();
    }
  } else {
    triggerError("Erreur à l'ajout du wellness");
  }
};

/**
 * Fonction pour mettre à jour les types de graphes
 */
const handleChartChange = (e: any) => {
  console.log(e);
  period.value = e;
  console.log(tempDate);
  if (e == "week") {
    updateWeekWellness();
  } else {
    updateMonthWellness();
  }
};

/**
 * Fonction pour vérifier si le mois et l'année de la date actuelle sont antérieurs à tempDate
 * @param date - La date à vérifier
 * @returns {boolean} - Retourne vrai si le mois et l'année de la date actuelle sont antérieurs à tempDate
 */
const isMonthBeforeTempDate = () => {
  const currentDate = new Date(Date.now());

  const currentYear = currentDate.getFullYear();
  const currentMonth = currentDate.getMonth(); // Mois de 0 à 11

  const tempYear = new Date(tempDate.value).getFullYear();
  const tempMonth = new Date(tempDate.value).getMonth();

  // Vérifier si l'année et le mois de la date actuelle sont antérieurs à ceux de tempDate
  return currentYear <= tempYear && currentMonth == tempMonth;
};

/**
 * Fonction qui permet la mise à jour du wellness du jour
 */
const patchWellness = async () => {
  const response = await patch(
    `/wellness/${wellness.value.id}/`,
    {
      body: {
        sleep: wellness.value.sleep,
        hydratation: wellness.value.hydratation,
        fatigue: wellness.value.fatigue,
        pain: wellness.value.pain,
        stress: wellness.value.stress,
      },
    },
    true
  );
  if (!response.status) {
    modal.value.$el.dismiss();
  } else {
    triggerError("Erreur lors de la modification du wellness");
  }
};

/**
 * Fonction pour afficher les graphiques du wellness
 */
const showStats = async () => {
  modalStats.value.$el.present();
  weekWellnessTemp.value = weekWellness.value;
  await updateWeekWellness();
};

/**
 * Fonction pour afficher et récupérer les informations du wellness de la semaine précédente
 */
const setPreviousWeek = async () => {
  const newDate = new Date(tempDate.value);
  newDate.setDate(newDate.getDate() - 7);
  tempDate.value = newDate;
  await updateWeekWellness();
};

/**
 * Fonction pour afficher et récupérer les informations du wellness de la semaine suivante (sauf si semaine actuelle)
 */
const setNextWeek = async () => {
  const newDate = new Date(tempDate.value);
  newDate.setDate(newDate.getDate() + 7);
  tempDate.value = newDate;
  await updateWeekWellness();
};

/**
 * Fonction pour afficher et récupérer les informations du wellness du mois précédent
 */
const setPreviousMonth = async () => {
  const newDate = new Date(tempDate.value);
  newDate.setMonth(newDate.getMonth() - 1);
  tempDate.value = newDate;
  await updateMonthWellness(); // Supposons que vous avez une fonction updateMonthWellness pour mettre à jour les données mensuelles
};

/**
 * Fonction pour afficher et récupérer les informations du wellness du mois suivant
 */
const setNextMonth = async () => {
  const newDate = new Date(tempDate.value);
  newDate.setMonth(newDate.getMonth() + 1);
  tempDate.value = newDate;
  await updateMonthWellness(); // Supposons que vous avez une fonction updateMonthWellness pour mettre à jour les données mensuelles
};

/**
 * Fonction pour récupérer le nom complet du mois et l'année à partir d'une date
 * @param date - La date à partir de laquelle extraire le mois et l'année
 * @returns {string} - Retourne le nom complet du mois et l'année (ex: "July 2023")
 */
const getMonthAndYear = () => {
  const months = [
    "Janvier",
    "Février",
    "Mars",
    "Avril",
    "Mai",
    "Juin",
    "Juillet",
    "Aout",
    "Septembre",
    "Octobre",
    "Novembre",
    "Décembre",
  ];

  const givenDate = new Date(tempDate.value);
  const monthName = months[givenDate.getMonth()];
  const year = givenDate.getFullYear();

  return `${monthName} ${year}`;
};

/**
 * Fonction pour récupérer et afficher le wellness de la semaine de la date actuelle
 */
const updateWeekWellness = async () => {
  const res = await get(
    `/wellness/user/${user.value.id}/week?date=${setLongDate(
      new Date(tempDate.value)
    )}`,
    { body: {} },
    true
  );
  if (res.status > 301) {
    triggerError("Erreur lors du changement de données");
  } else {
    weekWellnessTemp.value = JSON.parse(JSON.stringify(res));
    if (chart.value) chart.value.destroy();
    createChart(weekWellnessTemp.value);
  }
};

/**
 * Fonction pour récupérer et afficher le wellness du mois de la date actuelle
 */
const updateMonthWellness = async () => {
  const res = await get(
    `/wellness/user/${user.value.id}/month?date=${setLongDate(
      new Date(tempDate.value)
    )}`,
    { body: {} },
    true
  );
  if (res.status > 301) {
    triggerError("Erreur lors du changement de données");
  } else {
    monthWellnessTemp.value = JSON.parse(JSON.stringify(res));
    if (chart.value) chart.value.destroy();
    createChart(monthWellnessTemp.value);
  }
};

/**
 * Fonction de création du graphique du wellness
 * @param data
 */
const createChart = (data: any) => {
  const labels = data.map((elem: { date: string }) => {
    const date = new Date(elem.date);
    const day = date.getDate();
    const weekday = ["dim", "lun", "mar", "mer", "jeu", "ven", "sam"][
      date.getDay()
    ];
    return `${weekday} ${day}`;
  });

  chart.value = markRaw(
    //@ts-expect-error
    new Chart(document.getElementById("acquisitions"), {
      type: "line",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Sommeil",
            data: data.map((elem: { sleep: any }) => elem.sleep),
          },
          {
            label: "Fatigue",
            data: data.map((elem: { fatigue: any }) => elem.fatigue),
          },
          {
            label: "Douleurs",
            data: data.map((elem: { pain: any }) => elem.pain),
          },
          {
            label: "Stress",
            data: data.map((elem: { stress: any }) => elem.stress),
          },
          {
            label: "Hydratation",
            data: data.map((elem: { hydratation: any }) => elem.hydratation),
          },
        ],
      },
      options: {
        spanGaps: true,
        scales: { y: { min: 0, max: 10 } },
        fullSize: true,
        plugins: {
          legend: {
            display: true,
            labels: {
              font: {
                size: 11,
              },
              boxWidth: 20,
              boxHeight: 8,
            },
          },
        },
      },
    })
  );
};

/**
 * Met à jour la valeur d'un champ de bien-être.
 * @param {Object} detail - Contient la nouvelle valeur du champ.
 * @param {any} name - Le nom du champ de bien-être à mettre à jour.
 */
const onIonChange = ({ detail }: any, name: any) => {
  wellness.value[name] = detail.value;
};

/**
 * Calcule l'URL de l'image de profil de l'utilisateur.
 * @returns {string} - L'URL de l'image de profil, modifiée pour utiliser HTTPS si nécessaire.
 */
const profilePicture = computed(() => {
  if (user.value.profile_picture?.includes(api.split("//")[1])) {
    return user.value.profile_picture.replace("http", "https");
  }
  return user.value.profile_picture ? api + user.value.profile_picture : "";
});

/**
 * Charge les informations de l'utilisateur depuis le stockage et rafraîchit ses données.
 */
const loadUser = async () => {
  const storeUser = await store.get("user");
  if (storeUser) {
    user.value = JSON.parse(storeUser).user;
  }
  await refreshUser();
};

/**
 * Rafraîchit les données de l'utilisateur depuis l'API et les met à jour dans le stockage.
 */
const refreshUser = async () => {
  const response = await get(`/users/me`, { body: {} }, true);
  if (response > 301) {
    triggerError("Erreur lors de la récupération des données utilisateur");
  } else {
    user.value = response.user;
    const userToSet = {
      user: response,
      access: JSON.parse(await store.get("user")).access,
      refresh: JSON.parse(await store.get("user")).refresh,
    };
    store.set("user", JSON.stringify(userToSet));
    checkUserWellness();
  }
};

/**
 * Vérifie le bien-être de l'utilisateur pour la semaine et met à jour l'état de bien-être.
 */
const checkUserWellness = async () => {
  const res = await get(
    `/wellness/user/${user.value.id}/week?date=${setLongDate(new Date())}`,
    { body: {} },
    true
  );
  if (res.status > 301) {
    triggerError("Erreur lors de la récupération du wellness");
  } else {
    res.forEach((WellnessItem: any) => {
      if (
        WellnessItem.date === setLongDate(new Date()) &&
        WellnessItem.sleep != null
      ) {
        wellnessNot.value = false;
        wellness.value = WellnessItem;
      }
    });
  }
};

/**
 * Calcule le numéro de la semaine pour une date donnée.
 * @param {Date} d - La date pour laquelle calculer le numéro de semaine.
 * @returns {number} - Le numéro de la semaine.
 */
function getWeekNumber(d: any) {
  d = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
  d.setUTCDate(d.getUTCDate() + 4 - (d.getUTCDay() || 7));
  let yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1)) as any;
  let weekNo = Math.ceil(((d - yearStart) / 86400000 + 1) / 7);
  return weekNo;
}

/**
 * Exécute les actions nécessaires lors de l'entrée dans la vue.
 */
onIonViewWillEnter(async () => {
  wellnessNot.value = true;
  wellness.value = {
    sleep: 0,
    stress: 0,
    hydratation: 0,
    pain: 0,
    fatigue: 0,
    id: 0,
  };
  await loadUser();
  const res = await get(
    `/wellness/user/${user.value.id}/week?date=${setLongDate(new Date())}`,
    { body: {} },
    true
  );
  if (res.status > 301) {
    triggerError("Erreur lors de la récupération du wellness");
  } else {
    res.forEach((WellnessItem: any) => {
      if (WellnessItem.date === setLongDate(new Date())) {
        if (WellnessItem.sleep !== null) {
          wellnessNot.value = false;
          wellness.value = WellnessItem;
        }
      }
    });
  }

  weekWellness.value = res;
  weekWellnessTemp.value = res;

  document.querySelectorAll(".custom_nav").forEach((elem) => {
    const shadowRoot = elem.shadowRoot;
    if (shadowRoot) {
      const style = document.createElement("style");
      style.textContent = `.button-inner { justify-content: flex-start !important; }`;
      shadowRoot.appendChild(style);
    }
  });
});

/**
 * Exécute les actions nécessaires lors de la sortie de la vue.
 */
onIonViewWillLeave(() => {
  if (chart.value) {
    chart.value.destroy();
  }
});
</script>
