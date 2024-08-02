<style scoped>
ion-modal {
  --width: 80%;
  --height: 35%;
  --border-radius: 16px;
  --box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
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
      <div
        class="perform-page"
        style="display: flex; flex-direction: column; 
    height: calc(100% - 20px);"
      >
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
                    <template v-if="record.units === 'weight'" >
                      <ion-label position="stacked" :class="errorAdd && weightValue=='' ? 'required_text' : ''">Poids (en kg)</ion-label>
                      <ion-input
                       :class="errorAdd && weightValue=='' ? 'required_class' : ''"
                        v-model="inputValue"
                        type="number"
                        placeholder="Enter weight in kg"
                        style="padding-left: 10px;"
                        @ion-change="handleInput($event.detail.value, 'weight')"
                      ></ion-input>
                    </template>
                    <template v-else>
                      <ion-label position="stacked" :class="errorAdd && !isTimeIsEmpty() ? 'required_text' : ''"
                        >Temps (en hh:mm:ss)</ion-label
                      >

                      <div class="time-input">
                        <ion-input
                          v-model="hours"
                          type="number"
                          placeholder="HH"
                          maxLength="2"
                          class="time_input"
                          :class="errorAdd && !isTimeIsEmpty() ? 'required_class' : ''"
                        ></ion-input
                        >:
                        <ion-input
                          v-model="minutes"
                          type="number"
                          placeholder="MM"
                          maxLength="2"
                          class="time_input"
                           :class="errorAdd && !isTimeIsEmpty() ? 'required_class' : ''"
                        ></ion-input
                        >:
                        <ion-input
                          v-model="seconds"
                          type="number"
                          placeholder="SS"
                          maxLength="2"
                          class="time_input"
                          :class="errorAdd && !isTimeIsEmpty() ? 'required_class' : ''"
                        ></ion-input>
                      </div>
                    </template>
                  <div class="input_injurie" >
                    <ion-label
                      :class="errorAdd && (dateRecord == '' || dateRecord == null) ? 'required_text' : ''"
                      >Date du record *</ion-label
                    >
                    <ion-input
                      :class="errorAdd && (dateRecord == '' || dateRecord == null)? 'required_class' : ''"
                      type="date"
                      label-placement="stacked"
                      fill="outline"
                      placeholder="2021-09-01"
                      @ion-change="handleInput($event.detail.value, 'time')"
                    ></ion-input>
                  </div>
                  <div style="display: flex; justify-content: center; width: 100%;">
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
        <div
          v-else
          style="
            flex: 1;
            overflow: hidden;
            display: flex;
            flex-direction: column;
          "
        >
          <canvas
            id="chartStats"
            width="300px"
            height="200px"
            min="0"
            max="10"
          ></canvas>
          <h3>Mes records passés</h3>
          <div style="display: flex; justify-content: space-between;">
              <p>Records</p>
              <p>Date</p>
          </div>
          <div class="scrollable-container" style="flex: 1; overflow-y: scroll">
            <div
              style="display: flex; justify-content: space-between; width: 100%"
              id="recordListUser"
            >
            </div>
            <div style="overflow-y: auto; flex: 1">
              <ion-list
                style="height: auto"
                v-for="item in record.performances.slice().reverse()"
                :key="item.id"
                class="records-list"
              >
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
              </ion-list>
            </div>
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
} from "@ionic/vue";

import "@/assets/base.css";
import "@/assets/main.css";
import '../Profile/index.css'
import { get, post } from "../../lib/callApi";
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

const errorAdd = ref(false)

const inputValue = ref("");
const hours = ref("");
const minutes = ref("");
const seconds = ref("");
const user = ref("") as any;
const weightValue = ref("");
const dateRecord = ref("") as any;

const modalRecord = ref(null) as any;

const routerNav = useRoute();

const handleInput = (e: any, type: string) => {
  console.log(e);
  if (type == "time") {
    dateRecord.value = new Date(e);
  } else {
    weightValue.value = e;
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

const formattedDate = (dateString: string) => {
  const date = new Date(dateString);
  return date.toLocaleDateString();
};

const getRecords = () => {
  const id_record = routerNav.params.record_id;
  console.log(user.value);
  get(
    "/records_user/by-record?record_id=" + id_record,
    { body: {} },
    true
  ).then((res) => {
    if (res.status > 300) {
      triggerError("Erreur lors de la récupération du record");
    } else {
      record.value = res;
      let find = false;
      let count = 0;
      setTimeout(() => {
        while (find == false && count < 3) {
          console.log("find ", find);
          console.log("count  ", count);
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

      if (chartInstance.value) {
        chartInstance.value.destroy();
      }
      setTimeout(() => {
        createChart();
      }, 200);
    }
  });
};

const chartInstance = ref(null) as any;

// Fonction pour formater les dates en dd/mm/yyyy
const formatDate = (dateString : string ) => {
  const date = new Date(dateString);
  const day = String(date.getDate()).padStart(2, "0");
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const year = date.getFullYear();
  return `${day}/${month}/${year}`;
};

// Fonction pour convertir le temps de hh:mm:ss en secondes
const timeToSeconds = (time : string) => {
  const timeParts = time.split(":");
  console.log(timeParts);
  return (
    parseInt(timeParts[0]) * 3600 +
    parseInt(timeParts[1]) * 60 +
    parseInt(timeParts[2])
  );
};

// Fonction pour convertir les secondes en hh:mm:ss
const secondsToTime = (seconds : any) => {
  const h = String(Math.floor(seconds / 3600)).padStart(2, "0");
  const m = String(Math.floor((seconds % 3600) / 60)).padStart(2, "0");
  const s = String(seconds % 60).padStart(2, "0");
  return `${h}:${m}:${s}`;
};

const createChart = () => {
  const labels = record.value.performances.map((performance : any) =>
    formatDate(performance.date_record)
  );
  console.log(record.value.performances);
  const data = record.value.performances.map((performance : any) =>
    record.value.units === "time"
      ? timeToSeconds(performance.time_value)
      : performance.weight_value
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
                const unit = record.value.units; // Assume all records have the same unit
                return unit === "time"
                  ? secondsToTime(value)
                  : `${value.toFixed(2)} kg`;
              },
            },
            title: {
              display: true,
              text: "Performance",
            },
          },
        },
      },
    })
  );
};

const updateChart = () => {
  if (!chartInstance) return;

  const labels = record.value.performances.map((performance : any) =>
    new Date(performance.date_record).toLocaleDateString()
  );
  const data = record.value.performances.map((performance : any) => {
    const timeParts = performance.time_value.split(":");
    return (
      parseInt(timeParts[0]) * 3600 +
      parseInt(timeParts[1]) * 60 +
      parseInt(timeParts[2])
    );
  });

  chartInstance.data.labels = labels;
  chartInstance.data.datasets[0].data = data;
  chartInstance.update();
};

const cleanValues = () => {
    errorAdd.value = false;
    hours.value = "";
              minutes.value = "";
              seconds.value = "";
              dateRecord.value = null;
              weightValue.value = ""
              dateRecord.value = "";
}

onMounted(() => {
    dateRecord.value = null;
  if (chartInstance.value) {
    chartInstance.value.destroy();
    setTimeout(() => {
      if (document.getElementById("chartStats")) createChart();
    }, 100);
  } else {
    if (document.getElementById("chartStats")) createChart();
  }
});

watch(
  record.value.performances,
  () => {
    if (chartInstance.value) {
      chartInstance.value.destroy();
    }
    updateChart();
  },
  { deep: true }
);

const isTimeIsEmpty = () => {
    return (hours.value  !== "" || minutes.value != "" || seconds.value != "")
}
const submitRecord = async () => {
    if(record.value.units ==="time" && isTimeIsEmpty()) {
        postData()
    } else if (record.value.units == 'weight' && weightValue.value != "") {
        postData()
    }else {
        console.log('je suis vide zebi')
        errorAdd.value = true;
        console.log(dateRecord.value)
        triggerError("Erreur à l'ajout, remplissez les champs")
    }
};

const postData = () => {
    const formattedTimeValue =
          record.value.units === "time" ? formatDuration(timeValue.value) : null;
        const body = {
          record: Number(routerNav.params.record_id),
          user: user.value.id,
          date_record: dateRecord.value,
          time_value: record.value.units === "time"  &&( hours.value  !== "" || minutes.value != "" || seconds.value != "")  ? formattedTimeValue : null,
          weight_value: record.value.units === "weight" ? weightValue.value : null,
        };
      
        try {
          post("/records_user/", { body }, true).then((res) => {
            console.log(res);
      
            if (res.status && res.status > 300) {
              // Gérer la réussite
              triggerError("Erreur à l'ajout du record")
            } else {
              console.log("Record added successfully");
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
}
const timeValue = computed(() => {
  return `${hours.value}:${minutes.value}:${seconds.value}`;
});

const showModal = async (modal: any) => {
  modal.$el.present();
};
const formatDuration = (time : any) => {
  const [hours, minutes, seconds] = time
    .split(":")
    .map((part : any) => part.padStart(2, "0"));

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
