<style scoped>
ion-modal {
  --width: 80%;
  --height: 35%;
  --border-radius: 16px;
  --box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
}

.time-input::v-deep .input-wrapper.sc-ion-input-ios {
  padding-inline-start: 0px !important;
  padding-inline-end: 0px !important;
}

.custom-ion-item {
  --padding-start: 0;
}

.time-input {
  display: flex;
  align-items: center;
  gap: 5px;
  justify-content: center;
  width: 100%;
  padding-bottom: 10px;
}

.center-input {
  text-align: center;
}

.time-input ion-input {
  width: 2.5em;
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
</style>

<template>
  <ion-page data-page="ShowRecords">
    <ion-content id="list-records">
      <div class="perform-page" style="display: flex; flex-direction: column">
        <div style="display: flex; justify-content: space-between">
          <NavButton url="records" text="Retour" back="back" />
          <NavButton
            url=""
            text="Ajouter un record"
            @click="showModal(modalRecord)"
            :icon="addOutline"
          />
          <ion-modal class="static-modal" ref="modalRecord">
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
                  <h1 style="margin: 0px">Ajouter un nouveau record</h1>
                  <ion-icon
                    class="close-icon"
                    @click="modalRecord ? modalRecord.$el.dismiss() : ''"
                    :icon="close"
                  />
                </div>
                <div>
                  <template v-if="record.units === 'weight'">
                    <ion-label
                      position="stacked"
                      :class="
                        errorAdd && weightValue == '' ? 'required_text' : ''
                      "
                      >Poids (en kg)</ion-label
                    >
                    <ion-input
                      :class="
                        errorAdd && weightValue == '' ? 'required_class' : ''
                      "
                      v-model="inputValue"
                      type="number"
                      placeholder="Entez le poids en kg"
                      style="padding-left: 10px"
                      @ion-change="handleInput($event.detail.value, 'weight')"
                    ></ion-input>
                  </template>
                  <template v-else-if="record.units === 'time'">
                    <ion-label
                      position="stacked"
                      :class="
                        errorAdd && !isTimeIsEmpty() ? 'required_text' : ''
                      "
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
                        style="padding-inline-start: 0px; --padding-end: 0px"
                        :class="
                          errorAdd && !isTimeIsEmpty() ? 'required_class' : ''
                        "
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
                        :class="
                          errorAdd && !isTimeIsEmpty() ? 'required_class' : ''
                        "
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
                        :class="
                          errorAdd && !isTimeIsEmpty() ? 'required_class' : ''
                        "
                      ></ion-input>
                    </div>
                  </template>
                  <template v-else-if="record.units === 'points'">
                    <ion-label
                      position="stacked"
                      :class="
                        errorAdd && weightValue == '' ? 'required_text' : ''
                      "
                      >Points</ion-label
                    >
                    <ion-input
                      :class="
                        errorAdd && weightValue == '' ? 'required_class' : ''
                      "
                      v-model="inputValue"
                      type="number"
                      placeholder="Entrer les points"
                      style="padding-left: 10px"
                      @ion-change="handleInput($event.detail.value, 'points')"
                    ></ion-input>
                  </template>
                  <template v-else-if="record.units === 'distance_m'">
                    <ion-label
                      position="stacked"
                      :class="
                        errorAdd && weightValue == '' ? 'required_text' : ''
                      "
                      >Distance (en m)</ion-label
                    >
                    <ion-input
                      :class="
                        errorAdd && weightValue == '' ? 'required_class' : ''
                      "
                      v-model="inputValue"
                      type="number"
                      placeholder="Entrer la distance (en m)"
                      style="padding-left: 10px"
                      @ion-change="
                        handleInput($event.detail.value, 'distance_m')
                      "
                    ></ion-input>
                  </template>
                  <template v-else-if="record.units === 'distance_km'">
                    <ion-label
                      position="stacked"
                      :class="
                        errorAdd && weightValue == '' ? 'required_text' : ''
                      "
                      >Distance (en km)</ion-label
                    >
                    <ion-input
                      :class="
                        errorAdd && weightValue == '' ? 'required_class' : ''
                      "
                      v-model="inputValue"
                      type="number"
                      placeholder="Entrer la distance (en km)"
                      style="padding-left: 10px"
                      @ion-change="
                        handleInput($event.detail.value, 'distance_km')
                      "
                    ></ion-input>
                  </template>
                  <template v-else-if="record.units === 'reps'">
                    <ion-label
                      position="stacked"
                      :class="
                        errorAdd && weightValue == '' ? 'required_text' : ''
                      "
                      >Nombre de répétitions</ion-label
                    >
                    <ion-input
                      :class="
                        errorAdd && weightValue == '' ? 'required_class' : ''
                      "
                      v-model="inputValue"
                      type="number"
                      placeholder="Entrer le nombres de répétitions maxs"
                      style="padding-left: 10px"
                      @ion-change="handleInput($event.detail.value, 'reps')"
                    ></ion-input>
                  </template>
                  <template v-else>
                    <ion-label
                      position="stacked"
                      :class="
                        errorAdd && freeValue == '' ? 'required_text' : ''
                      "
                      >Personnalisé</ion-label
                    >
                    <ion-input
                      :class="
                        errorAdd && freeValue == '' ? 'required_class' : ''
                      "
                      v-model="inputValue"
                      type="text"
                      placeholder="Entrer un record personnalisé"
                      style="padding-left: 10px"
                      @ion-change="handleInput($event.detail.value, 'free')"
                    ></ion-input>
                  </template>
                  <div class="input_injurie">
                    <ion-label
                      :class="
                        errorAdd && (dateRecord == '' || dateRecord == null)
                          ? 'required_text'
                          : ''
                      "
                      >Date du record *</ion-label
                    >
                    <ion-input
                      :class="
                        errorAdd && (dateRecord == '' || dateRecord == null)
                          ? 'required_class'
                          : ''
                      "
                      type="date"
                      label-placement="stacked"
                      fill="outline"
                      placeholder="2021-09-01"
                      @ion-change="handleInput($event.detail.value, 'time')"
                    ></ion-input>
                  </div>
                  <div
                    style="display: flex; justify-content: center; width: 100%"
                  >
                    <ion-button @click="submitRecord"> Ajouter </ion-button>
                  </div>
                </div>
              </div>
            </ion-content>
          </ion-modal>
        </div>

        <h1
          style="
            text-align: center;
            color: black;
            margin-top: 35px;
            margin-bottom: 10px;
          "
        >
          {{ record.record_name }}
        </h1>

        <div v-if="record.performances.length <= 0">
          <h2 style="text-align: center">Saisissez votre premier record !</h2>
        </div>
      </div>
      <div
        v-if="record.performances.length > 0"
        style="
          margin: 20px;
          padding: 10px;
          border-radius: 10px;
          border: solid 0.5px #eaeaea;
          position: relative;
          z-index: 1;
          box-shadow: silver 0px 10px 20px 0px;
        "
      >
        <canvas
          v-if="record.units !== 'free'"
          id="chartStats"
          width="300px"
          height="200px"
          min="0"
          max="10"
        ></canvas>
      </div>

      <div
        v-if="record.performances.length > 0"
        style="
          margin: 20px;
          padding: 10px;
          border-radius: 10px;
          border: solid 0.5px #eaeaea;
          z-index: 1000;
          box-shadow: silver 0px 10px 20px 0px;
          flex: 1;
          overflow: scroll;
          height: calc(100vh - 520px);
          display: flex;
          flex-direction: column;
        "
      >
        <h3>Mes records passés</h3>
        <div
          style="
            display: flex;
            justify-content: space-between;
            border-bottom: 1px solid silver;
            padding-bottom: 10px;
            margin-bottom: 5px;
          "
        >
          <p>Records</p>
          <p>Date</p>
        </div>
        <div class="scrollable-container" style="flex: 1; overflow-y: scroll">
          <div
            style="display: flex; justify-content: space-between; width: 100%"
            id="recordListUser"
          ></div>
          <div style="overflow-y: auto; flex: 1">
            <ion-list
              style="height: auto"
              v-for="item in record.performances.slice().reverse()"
              :key="item.id"
              class="records-list"
            >
              <ion-item-sliding>
                <ion-item
                  class="record-unit"
                  style="
                    display: flex;
                    justify-content: space-between;
                    width: 100%;
                  "
                >
                  <p>{{ item.formatted_record }}</p>
                  <p>{{ formattedDate(item.date_record) }}</p>
                </ion-item>

                <!-- Bouton de suppression -->
                <ion-item-options side="end">
                  <ion-item-option
                    color="danger"
                    expandable
                    @click="deleteRecord(item.id)"
                  >
                    Supprimer
                  </ion-item-option>
                </ion-item-options>
              </ion-item-sliding>
            </ion-list>
          </div>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import NavButton from "../../components/NavButton/NavButton.vue";
import { close, addOutline } from "ionicons/icons";
import {
  IonItem,
  IonLabel,
  IonInput,
  IonPage,
  IonIcon,
  IonContent,
  onIonViewWillEnter,
  IonModal,
  IonList,
  IonButton,
  IonItemSliding,
  IonItemOption,
  IonItemOptions,
} from "@ionic/vue";

import "@/assets/base.css";
import "@/assets/main.css";
import "../Profile/index.css";
import { get, post, del } from "../../lib/callApi";
import { useRoute } from "vue-router";
import { store } from "../../store/store";
import { ref, watch, computed, onMounted, onUnmounted, markRaw } from "vue";
import { Chart, registerables } from "chart.js";
import { useErrorHandler } from "../../lib/useErrorHandler";

const { triggerError } = useErrorHandler() as any;
Chart.register(...registerables);
const props = defineProps({
  unit: {
    type: String,
    required: true,
  },
  label: {
    type: String,
    default: "Input",
  },
});

const record = ref({
  record_name: "",
  performances: [],
  units: "",
}) as any;

const recordArray = ref([
  "weight",
  "distance_m",
  "distance_km",
  "points",
  "reps",
]);

const errorAdd = ref(false);

const inputValue = ref("");
const hours = ref("");
const minutes = ref("");
const seconds = ref("");
const user = ref("") as any;
const weightValue = ref("");
const freeValue = ref("");
const dateRecord = ref("") as any;

const modalRecord = ref(null) as any;

const routerNav = useRoute();

const handleInput = (e: any, type: string) => {
  console.log(type, " ", e);
  if (type == "time") {
    dateRecord.value = new Date(e);
  } else if (recordArray.value.includes(type)) {
    weightValue.value = e;
    console.log(" weight ", weightValue);
  } else {
    freeValue.value = e;
  }
};

watch(
  () => props.unit,
  (newVal) => {
    if (newVal === "kg") {
      hours.value = "";
      minutes.value = "";
      seconds.value = "";
    } else {
      inputValue.value = "";
    }
  }
);

const deleteRecord = (id: any) => {
  del("/records_user/" + id, true).then((res) => {
    if (res.status && res.status > 300) {
      triggerError("Erreur à la suppression,");
    } else {
      getRecords();
    }
  });
};

const formattedDate = (dateString: string) => {
  const date = new Date(dateString);
  return date.toLocaleDateString();
};

const getRecords = () => {
  const id_record = routerNav.params.record_id;

  get(
    "/records_user/by-record?record_id=" + id_record,
    { body: {} },
    true
  ).then((res) => {
    if (res.status > 300) {
      triggerError("Erreur lors de la récupération du record");
    } else {
      record.value = res;
      console.log("record ", res);
      let find = false;
      let count = 0;
      setTimeout(() => {
        while (find == false && count < 3) {
          const items = document.querySelectorAll(".record-unit");

          if (items) {
            find = true;
            count = 4;
            for (let elem of items) {
              const style = document.createElement("style");

              // Ajoutez le CSS à l'élément style
              style.textContent = `
                .item-inner .input-wrapper {
                  padding-left : 10px !important;
                  padding-right : 10px !important;
                  width: 100%;
                  display : flex;
                  justify-content: space-between;
                }
                  .item-inner {
                  padding-left : 0px !important;
                  padding-right : 0px !important;
                }
              `;

              // Insérez l'élément style dans le shadowRoot
              //@ts-expect-error
              elem.shadowRoot.appendChild(style);
            }
          } else {
            count = count + 1;
          }
        }
      }, 200);
      console.log(chartInstance.value)
      if (chartInstance.value) {
        chartInstance.value.destroy();
      }

      if (res.performances.length > 0 && res.units !== "free") {
        if (chartInstance.value) {
        chartInstance.value.destroy();
      }
        setTimeout(() => {
          createChart();
        }, 400);
      }
    }
  });
};

const chartInstance = ref(null) as any;

// Fonction pour formater les dates en dd/mm/yyyy
const formatDate = (dateString: string) => {
  const date = new Date(dateString);
  const day = String(date.getDate()).padStart(2, "0");
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const year = date.getFullYear();
  return `${day}/${month}/${year}`;
};

// Fonction pour convertir le temps de hh:mm:ss en secondes
const timeToSeconds = (time: string) => {
  const timeParts = time.split(":");

  return (
    parseInt(timeParts[0]) * 3600 +
    parseInt(timeParts[1]) * 60 +
    parseInt(timeParts[2])
  );
};

// Fonction pour convertir les secondes en hh:mm:ss
const secondsToTime = (seconds: any) => {
  const h = String(Math.floor(seconds / 3600)).padStart(2, "0");
  const m = String(Math.floor((seconds % 3600) / 60)).padStart(2, "0");
  const s = String(seconds % 60).padStart(2, "0");
  return `${h}:${m}:${s}`;
};

const createChart = () => {
  const labels = record.value.performances.map((performance: any) =>
    formatDate(performance.date_record)
  );

  const data = record.value.performances.map((performance: any) =>
    record.value.units === "time"
      ? timeToSeconds(performance.time_value)
      : performance.record_value
  );

  chartInstance.value = markRaw(
    //@ts-expect-error
    new Chart(document.getElementById("chartStats"), {
      type: "line",
      data: {
        labels,
        datasets: [
          {
            label: "Performance",
            data,
            borderColor: "#3767B8",
            backgroundColor: "#E8F8FEa6",
            fill: true,
          },
        ],
      },
      options: {
        scales: {
          x: {
            title: {
              display: true,
              text: "Date",
            },
          },
          y: {
            ticks: {
              callback: (value : any) => {
                // Récupérer l'unité de l'enregistrement
                const unit = record.value.units;

                // Traiter la valeur en fonction de l'unité
                if (unit === "time") {
                  return secondsToTime(value); // Conversion pour le temps
                } else if (unit === "weight") {
                  return `${value.toFixed(2)} kg`; // Afficher avec un suffixe "kg" pour le poids
                } else if (unit === "distance_km") {
                  return `${value.toFixed(2)} km`; // Afficher avec un suffixe "km"
                } else if (unit === "distance_m") {
                  return `${value.toFixed(2)} m`; // Afficher avec un suffixe "m"
                } else if (unit === "points" || unit === "reps") {
                  return `${value.toFixed(0)}`; // Afficher comme un entier pour les points ou répétitions
                } else if (unit === "free") {
                  return value; // Pour "free" (personnalisé), affichez simplement la valeur telle quelle
                } else {
                  return value.toFixed(2); // Cas par défaut, afficher avec 2 décimales
                }
              },
            },
            title: {
              display: true,
              text: "Performance",
            },
          },
        },
        plugins: {
          legend: {
            display: true,
            labels: {
              font: {
                size: 12,
              },
              boxWidth: 30,
              boxHeight: 1,
            },
          },
        },
      },
    })
  );
};

const cleanValues = () => {
  errorAdd.value = false;
  hours.value = "";
  minutes.value = "";
  seconds.value = "";
  dateRecord.value = null;
  weightValue.value = "";
  dateRecord.value = "";
};

onMounted(() => {
  dateRecord.value = null;
  if (chartInstance.value) {
    chartInstance.value.destroy();
    setTimeout(() => {
      if (document.getElementById("chartStats")) createChart();
    }, 100);
  }
});

watch(
  record.value.performances,
  () => {
    if (chartInstance.value) {
      chartInstance.value.destroy();
    }
    createChart();
  },
  { deep: true }
);

const isTimeIsEmpty = () => {
  return hours.value !== "" || minutes.value != "" || seconds.value != "";
};
const submitRecord = async () => {
  if (record.value.units === "time" && isTimeIsEmpty()) {
    postData();
  } else if (
    recordArray.value.includes(record.value.units) &&
    weightValue.value != ""
  ) {
    postData();
  } else if (freeValue.value != "") {
    postData();
  } else {
    errorAdd.value = true;

    triggerError("Erreur à l'ajout, remplissez les champs");
  }
};

const postData = () => {
  const formattedTimeValue =
    record.value.units === "time" ? formatDuration(timeValue.value) : null;
  const body = {
    record: Number(routerNav.params.record_id),
    user: user.value.id,
    date_record: dateRecord.value,
    time_value:
      record.value.units === "time" &&
      (hours.value !== "" || minutes.value != "" || seconds.value != "")
        ? formattedTimeValue
        : null,
    record_value: recordArray.value.includes(record.value.units)
      ? weightValue.value
      : null,
    free_value: record.value.units === "free" ? freeValue.value : null,
  };

  try {
    post("/records_user/", { body }, true).then((res) => {
      if (res.status && res.status > 300) {
        // Gérer la réussite
        triggerError("Erreur à l'ajout du record");
      } else {
        modalRecord.value.$el.dismiss();
        if (chartInstance.value) {
          chartInstance.value.destroy();
        }
        cleanValues();
        getRecords();
        // Gérer l'erreur
      }
    });
  } catch (error) {
    console.error("Error:", error);
  }
};
const timeValue = computed(() => {
  return `${hours.value}:${minutes.value}:${seconds.value}`;
});

const showModal = async (modal: any) => {
  modal.$el.present();
};
const formatDuration = (time: any) => {
  const [hours, minutes, seconds] = time
    .split(":")
    .map((part: any) => part.padStart(2, "0"));

  // Format to HH:MM:SS
  const formattedDuration = `00 ${hours}:${minutes}:${seconds}`;
  return formattedDuration;
};
onIonViewWillEnter(async () => {
  cleanValues();
  const storeUser = await store.get("user");
  user.value = JSON.parse(storeUser).user;
  if (chartInstance.value) {
    chartInstance.value.destroy();
  }
  getRecords();
});

onUnmounted(() => {
  if (chartInstance.value) {
    chartInstance.value.destroy();
  }
});
</script>
