<style scoped>
ion-modal {
  --height: 70%;
  --width: 80%;
  --border-radius: 16px;
  --box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
}

.static-modal {
  --height: 50%;
  --width: 100%;
  --border-radius: 16px;
  --box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
}

ion-modal::part(backdrop) {
  background: rgba(209, 213, 219);
  opacity: 1;
}

ion-modal ion-toolbar {
  --background: rgb(14 116 144);
  --color: white;
}

ion-range {
  --bar-height: 2px;
  --bar-border-radius: 8px;
  --knob-size: 10px;
}

.example-content {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.home_div {
  margin-left: var(--pd-l);
  margin-right: var(--pd-r);
}

.header_img {
  display: flex;
  justify-content: center;
  margin-top: 50px;
}

.block_100 {
  display: flex;
  margin-top: 20px;
  justify-content: space-between;
  width: auto;
  align-items: center;
  align-items: center;
  border: 0.5px solid #e0e0e0;
  padding: 10px;
  box-shadow: 0 0 10px #e0e0e0;
  border-radius: 10px;
}

.block_50 {
  width: 42% !important;
  margin-top: 20px;
  width: auto;
  align-items: flex-start;
  border: 0.5px solid #e0e0e0;
  padding: 20px 10px 10px 10px;
  box-shadow: 0 0 10px #e0e0e0;
  border-radius: 10px;
  flex-wrap: wrap;
}

.block_50 h3 {
  margin-top: 0px;
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 0px;
}

.div_info {
  width: 70%;
  text-wrap: wrap;
}

.users_infos {
  display: flex;
  justify-content: space-between;
  width: 100%;
  align-items: center;
}

.users_infos h3 {
  margin-top: 0px;
  width: 100;
  text-decoration: underline;
  font-size: 13px;
  text-align: center;
  font-weight: 700;
}

.profile_picture {
  width: 100px;
  height: 100px;
  border-radius: 100px;
  border: 2px var(--primary-blue) solid;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.profile_picture img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.div_user_info p {
  text-align: center;
}

.split_div {
  display: flex;
  justify-content: space-between;
  width: auto;
}

.range_div {
  display: flex;
  justify-content: space-between;
  width: 100%;
  flex-wrap: wrap;
}

.range_div .title_range {
  width: 100%;
  text-align: center;
}

.range_container {
  height: 30px;
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.range_container p {
  font-size: 10px !important;
  text-align: center;
  color: #aeaeae;
}

.divs_range {
  padding: 0px 10px 10px 10px;
}

.range_inner {
  display: flex;
  justify-content: center;
  padding-left: 20px;
  padding-right: 20px;
}
</style>

<template>
  <ion-page>
    <ion-content>
      <div class="home_div">
        <div class="header_img">
          <img width="200px" src="@/assets/logo_perform_bandeau.png" alt="logo" />
        </div>
        <div class="block_100">
          <div class="div_info">
            <h1>
              Salut <br />
              {{ user.first_name }} !
            </h1>
            <p>
              {{ new Date(Date.now()).toLocaleString("fr").split(" ")[0] }}
            </p>
          </div>
          <div class="profile_picture">
            <div style="
                display: flex;
                justify-content: center;
                align-items: center;
                font-size: 2rem;
                font-weight: bold;
                color: var(--primary-blue);
                background-color: white;
                border-radius: 50%;
                width: 100%;
                height: 100%;
                text-transform: capitalize;
              " v-if="setPP() == ''">
              {{ user.first_name[0] }}
            </div>
            <img v-else :src="user ? setPP() : ''" alt="profile" style="height: 80px; border-radius: 50%" />
          </div>
        </div>
        <div class="block_100">
          <div class="users_infos">
            <div class="div_user_info">
              <h3>Discipline(s) :</h3>
              <p v-for="sport of user.sports_user.splice(0, 2)">
                {{ sport.sport.name }}
              </p>
              <p>...</p>
            </div>
            <div class="div_user_info">
              <h3>Âge :</h3>
              <p>{{ user.age }}</p>
            </div>

            <div class="div_user_info">
              <h3>Poids :</h3>
              <p>{{ user.weight }} kg</p>
            </div>

            <div class="div_user_info">
              <h3>Taille :</h3>
              <p>{{ user.size }} cm</p>
            </div>
          </div>
        </div>
        <div class="split_div">
          <div class="block_50">
            <h3>Welness</h3>
            <ion-modal ref="modal" trigger="open-modal">
              <ion-content>
                <div style="
                    padding: 20px 20px 5px 20px;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                  ">
                  <h3 style="font-size: 13px; margin: 0px">
                    Saissiez le welness du jour :
                  </h3>
                  <ion-icon style="
                      color: red;
                      border: 1px solid red;
                      border-radius: 5px;
                    " @click="dismiss" :icon="close" />
                </div>
                <div class="divs_range">
                  <div id="pain_range">
                    <div class="range_div">
                      <ion-label class="title_range">Douleurs</ion-label>
                      <div class="range_container">
                        <p>Journée<br />douloureuse</p>
                        <p>
                          Aucune<br />
                          douleur
                        </p>
                      </div>
                    </div>
                    <div class="range_inner">
                      <ion-range :value="welness.pain" aria-label="Range with ticks" :ticks="true" :snaps="true"
                        :min="0" :max="10" @ionChange="onIonChange($event, 'pain')"></ion-range>
                    </div>
                  </div>
                  <div id="sleep_range">
                    <div class="range_div">
                      <ion-label class="title_range">Sommeil</ion-label>
                      <div class="range_container">
                        <p>Mauvais<br />sommeil</p>
                        <p>
                          Très bon<br />
                          sommeil
                        </p>
                      </div>
                    </div>
                    <div class="range_inner">
                      <ion-range :value="welness.sleep" aria-label="Range with ticks" :ticks="true" :snaps="true"
                        :min="0" :max="10" @ionChange="onIonChange($event, 'sleep')"></ion-range>
                    </div>
                  </div>
                  <div id="stress_range">
                    <div class="range_div">
                      <ion-label class="title_range">Stress</ion-label>
                      <div class="range_container">
                        <p>Journée<br />stressante</p>
                        <p>
                          Journée<br />
                          détendue
                        </p>
                      </div>
                    </div>
                    <div class="range_inner">
                      <ion-range :value="welness.stress" aria-label="Range with ticks" :ticks="true" :snaps="true"
                        :min="0" :max="10" @ionChange="onIonChange($event, 'stress')"></ion-range>
                    </div>
                  </div>
                  <div id="fatigue_range">
                    <div class="range_div">
                      <ion-label class="title_range">Fatigue</ion-label>
                      <div class="range_container">
                        <p>Très<br />fatigué</p>
                        <p>
                          Je pète<br />
                          la forme
                        </p>
                      </div>
                    </div>
                    <div class="range_inner">
                      <ion-range aria-label="Range with ticks" :ticks="true" :snaps="true" :min="0" :max="10"
                        :value="welness.fatigue" @ionChange="onIonChange($event, 'fatigue')"></ion-range>
                    </div>
                  </div>
                  <div id="hydratation_range">
                    <div class="range_div">
                      <ion-label class="title_range">Hydratation</ion-label>
                      <div class="range_container">
                        <p>- de<br />1L</p>
                        <p>
                          + de<br />
                          3L
                        </p>
                      </div>
                    </div>
                    <div class="range_inner">
                      <ion-range aria-label="Range with ticks" :ticks="true" :snaps="true" :value="welness.hydratation"
                        :min="0" :max="10" @ionChange="onIonChange($event, 'hydratation')"></ion-range>
                    </div>
                  </div>
                  <div style="display: flex; justify-content: center">
                    <ion-button v-if="wellnessNot" @click="postWelness">
                      Enregistrer
                    </ion-button>
                    <ion-button v-else @click="patchWelness">
                      Editer
                    </ion-button>
                  </div>
                </div>
              </ion-content>
            </ion-modal>
            <ion-modal class="static-modal" ref="modalStats">
              <ion-content>
                <div style="
                    padding: 20px 20px 5px 20px;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    flex-wrap: wrap;
                  ">
                  <h3>Satistiques :</h3>
                  <ion-icon style="
                      color: red;
                      border: 1px solid red;
                      border-radius: 5px;
                    " @click="modalStats ? modalStats.$el.dismiss() : ''" :icon="close" />
                </div>
                <div style="padding: 0px 20px 5px 20px">
                  <h4 style="width: 100%; margin-top: 0px; text-align: center">
                    Semaine du
                    {{
                      new Date(weekWelnessTemp[0].date).getDate() +
                      "/" +
                      (new Date(weekWelnessTemp[0].date).getMonth() + 1)
                    }}
                    au
                    {{
                      new Date(weekWelnessTemp[6].date).getDate() +
                      "/" +
                      (new Date(weekWelnessTemp[6].date).getMonth() + 1)
                    }}
                  </h4>
                  <div style="
                      width: 100%;
                      display: flex;
                      justify-content: space-between;
                    ">
                    <ion-button @click="setPreviousWeek" fill="outline" style="font-size: 8px">
                      < Semaine précédente</ion-button>
                        <ion-button @click="setNexWeek" fill="outline" style="font-size: 8px">
                          Semaine suivante ></ion-button>
                  </div>
                  <div>
                    <canvas width="300px" height="200px" min="0" max="10" id="acquisitions"></canvas>
                  </div>
                </div>
              </ion-content>
            </ion-modal>

            <div v-if="wellnessNot">
              <p style="text-align: center; margin-top: 10px; font-size: 16px">
                Saissiez votre welness du jour !
                <ion-button id="open-modal" expand="block">Saisir le wellness</ion-button>
              </p>
            </div>
            <div v-else>
              <div class="divs_range">
                <div id="pain_range">
                  <div class="range_div">
                    <ion-label class="title_range">Douleurs</ion-label>
                    <div class="range_container">
                      <p>Journée<br />douloureuse</p>
                      <p>
                        Aucune<br />
                        douleur
                      </p>
                    </div>
                  </div>
                  <div class="range_inner">
                    <ion-range disabled :value="welness.pain" aria-label="Range with ticks" :ticks="true" :snaps="true"
                      :min="0" :max="10" @ionChange="onIonChange($event, 'pain')"></ion-range>
                  </div>
                </div>
                <div id="sleep_range">
                  <div class="range_div">
                    <ion-label class="title_range">Sommeil</ion-label>
                    <div class="range_container">
                      <p>Mauvais<br />sommeil</p>
                      <p>
                        Très bon<br />
                        sommeil
                      </p>
                    </div>
                  </div>
                  <div class="range_inner">
                    <ion-range disabled :value="welness.sleep" aria-label="Range with ticks" :ticks="true" :snaps="true"
                      :min="0" :max="10" @ionChange="onIonChange($event, 'sleep')"></ion-range>
                  </div>
                </div>
                <div id="stress_range">
                  <div class="range_div">
                    <ion-label class="title_range">Stress</ion-label>
                    <div class="range_container">
                      <p>Journée<br />stressante</p>
                      <p>
                        Journée<br />
                        détendue
                      </p>
                    </div>
                  </div>
                  <div class="range_inner">
                    <ion-range disabled :value="welness.stress" aria-label="Range with ticks" :ticks="true"
                      :snaps="true" :min="0" :max="10" @ionChange="onIonChange($event, 'stress')"></ion-range>
                  </div>
                </div>
                <div id="fatigue_range">
                  <div class="range_div">
                    <ion-label class="title_range">Fatigue</ion-label>
                    <div class="range_container">
                      <p>Très<br />fatigué</p>
                      <p>
                        Je pète<br />
                        la forme
                      </p>
                    </div>
                  </div>
                  <div class="range_inner">
                    <ion-range disabled aria-label="Range with ticks" :ticks="true" :snaps="true" :min="0" :max="10"
                      :value="welness.fatigue" @ionChange="onIonChange($event, 'fatigue')"></ion-range>
                  </div>
                </div>
                <div id="hydratation_range">
                  <div class="range_div">
                    <ion-label class="title_range">Hydratation</ion-label>
                    <div class="range_container">
                      <p>- de<br />1L</p>
                      <p>
                        + de<br />
                        3L
                      </p>
                    </div>
                  </div>
                  <div class="range_inner">
                    <ion-range disabled aria-label="Range with ticks" :ticks="true" :snaps="true"
                      :value="welness.hydratation" :min="0" :max="10"
                      @ionChange="onIonChange($event, 'hydratation')"></ion-range>
                  </div>
                </div>
                <div style="
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                  ">
                  <ion-button fill="outline" @click="showStats">Satistiques</ion-button>
                  <ion-button @click="modal.$el.present()">Editer</ion-button>
                </div>
              </div>
            </div>
          </div>
          <div class="block_50">
            <h3>Postural scoring</h3>
            <h4>Dernier en date : 26/02/2024</h4>
            <div v-if="wellnessNot"></div>
          </div>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonButton,
  IonRange,
  IonIcon,
  IonModal,
  IonLabel,
  IonContent,
  IonPage,
} from "@ionic/vue";
import "@/assets/base.css";
import "@/assets/main.css";
import { ref, onMounted, onUpdated, markRaw } from "vue";
import { store } from "../store/store";
import { useRoute } from "vue-router";
import { close } from "ionicons/icons";
import { patch, post, get } from "../lib/callApi";
import Chart from "chart.js/auto";
const routes = useRoute();


const api = import.meta.env.VITE_API_URL;

const wellnessNot = ref(true);

const weekWelness: any = ref([]);
const weekWelnessTemp: any = ref([]);

const tempDate: any = ref(new Date(Date.now()));

const welness = ref({
  sleep: 0,
  stress: 0,
  hydratation: 0,
  pain: 0,
  fatigue: 0,
  id: 0,
} as any);

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

const dismiss = () => {
  modal.value.$el.dismiss();
};

const setLongDate = (date: any) => {
  const year = date.getFullYear();
  const months = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  const longDate = `${year}-${months}-${day}`;
  return longDate;
};

const postWelness = async () => {
  post(
    "/wellness/",
    {
      body: {
        sleep: welness.value.sleep,
        hydratation: welness.value.hydratation,
        fatigue: welness.value.fatigue,
        pain: welness.value.pain,
        stress: welness.value.stress,
        user: user.value.id,
        date: setLongDate(new Date(Date.now())),
      },
    },
    true
  ).then(async (res) => {
    if (res.status > 301) {
    } else {
      const userResponse = await get(
        "/admin/users_all/me/",
        { body: {} },
        true
      );
      await store.set("user", JSON.stringify(userResponse));
      //SET LE SERIALIZER DE WELLNESS EN DETAILER POUR STOCKER LE WELLNESS CORRECTEMENT + SET WELLNESSNOT A FALSE
      console.log("res ", res);
      welness.value = res;
      console.log("welness ", welness.value);
      wellnessNot.value = false;
      dismiss();
    }
  });
};

const chart = ref(null) as any;

const showStats = async () => {
  modalStats.value.$el.present();
  weekWelnessTemp.value = weekWelness.value;
  setTimeout(() => {
    //@ts-expect-error
    const chartObj = new Chart(document.getElementById("acquisitions"), {
      type: "line",
      data: {
        labels: ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"],
        datasets: [
          {
            label: "Sommeil",
            data: weekWelness.value.map((elem: { sleep: any; }) => elem.sleep),
          },
          {
            label: "Douleurs",
            data: weekWelness.value.map((elem: { pain: any; }) => elem.pain),
          },
          {
            label: "Stress",
            data: weekWelness.value.map((elem: { stress: any; }) => elem.stress),
          },
          {
            label: "Hydratation",
            data: weekWelness.value.map((elem: { hydratation: any; }) => elem.hydratation),
          },
          {
            label: "Fatigue",
            data: weekWelness.value.map((elem: { fatigue: any; }) => elem.fatigue),
          },
        ],
      },
      options: {
        spanGaps: true,
        scales: {
          y: {
            min: 0,
            max: 10,
          },
        },
        fullSize: true,
      },
    });
    chart.value = markRaw(chartObj);
  }, 100);
};

const setPreviousWeek = () => {
  const newDate = new Date(tempDate.value);
  newDate.setDate(newDate.getDate() - 7);
  tempDate.value = newDate;

  get(
    "/wellness/user/" +
    user.value.id +
    "/week?date=" +
    setLongDate(tempDate.value),
    { body: {} },
    true
  )
    .then((res) => {
      weekWelnessTemp.value = JSON.parse(JSON.stringify(res));
      chart.value.destroy();
      //@ts-expect-error
      const chartObj = new Chart(document.getElementById("acquisitions"), {
        type: "line",
        data: {
          labels: ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"],
          datasets: [
            {
              label: "Sommeil",
              data: weekWelnessTemp.value.map((elem: { sleep: any; }) => elem.sleep),
            },
            {
              label: "Douleurs",
              data: weekWelnessTemp.value.map((elem: { pain: any; }) => elem.pain),
            },
            {
              label: "Stress",
              data: weekWelnessTemp.value.map((elem: { stress: any; }) => elem.stress),
            },
            {
              label: "Hydratation",
              data: weekWelnessTemp.value.map((elem: { hydratation: any; }) => elem.hydratation),
            },
            {
              label: "Fatigue",
              data: weekWelnessTemp.value.map((elem: { fatigue: any; }) => elem.fatigue),
            },
          ],
        },
        options: {
          spanGaps: true,
          scales: {
            y: {
              min: 0,
              max: 10,
            },
          },
          fullSize: true,
        },
      });
      chart.value = markRaw(chartObj);
    })
    .catch((error) => {
      console.error("Erreur lors de la récupération des données:", error);
    });
};

const setNexWeek = () => {
  const newDate = new Date(tempDate.value);
  newDate.setDate(newDate.getDate() + 7);
  tempDate.value = newDate;
  get(
    "/wellness/user/" + user.value.id + "/week?date=" + setLongDate(newDate),
    { body: {} },
    true
  ).then((res: any) => {
    weekWelnessTemp.value = JSON.parse(JSON.stringify(res));
    chart.value.destroy();
    //@ts-expect-error
    const chartObj = new Chart(document.getElementById("acquisitions"), {
      type: "line",
      data: {
        labels: ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"],
        datasets: [
          {
            label: "Sommeil",
            data: weekWelnessTemp.value.map((elem: { sleep: any; }) => elem.sleep),
          },
          {
            label: "Douleurs",
            data: weekWelnessTemp.value.map((elem: { pain: any; }) => elem.pain),
          },
          {
            label: "Stress",
            data: weekWelnessTemp.value.map((elem: { stress: any; }) => elem.stress),
          },
          {
            label: "Hydratation",
            data: weekWelnessTemp.value.map((elem: { hydratation: any; }) => elem.hydratation),
          },
          {
            label: "Fatigue",
            data: weekWelnessTemp.value.map((elem: { fatigue: any; }) => elem.fatigue),
          },
        ],
      },
      options: {
        spanGaps: true,
        scales: {
          y: {
            min: 0,
            max: 10,
          },
        },
        fullSize: true,
      },
    });
    chart.value = markRaw(chartObj);
  });
};

const patchWelness = async () => {
  patch(
    "/wellness/" + welness.value.id + "/",
    {
      body: {
        sleep: welness.value.sleep,
        hydratation: welness.value.hydratation,
        fatigue: welness.value.fatigue,
        pain: welness.value.pain,
        stress: welness.value.stress,
      },
    },
    true
  ).then(async (res) => {
    if (res.status > 301) {
      console.log("error");
    } else {
      const userResponse = await get(
        "/admin/users_all/me/",
        { body: {} },
        true
      );
      await store.set("user", JSON.stringify(userResponse));

      dismiss();
    }
  });
};

const onIonChange = ({ detail }: any, name: any) => {
  welness.value[name] = detail.value;
};

const setPP = () => {
  if (
    user.value.profile_picture &&
    user.value.profile_picture.includes(api.split("//")[1])
  ) {
    console.log(user.value.profile_picture);
    return user.value.profile_picture;
  } else {
    if (
      user.value.profile_picture === null ||
      user.value.profile_picture === ""
    ) {
      return "";
    } else {
      return api + user.value.profile_picture;
    }
  }
};
const load = () => {
  store.get("user").then((res) => {
    const json = JSON.parse(res);
    user.value = json.user;
    get("/admin/users_all/" + user.value.id, { body: {} }, true).then((res) => {
      user.value = res;
      const userToSet = {
        user: res,
        access: json.access,
        refresh: json.refresh,
      };
      store.set("user", JSON.stringify(userToSet));
      user.value.users_wellness.map((welnessItem: any) => {
        if (welnessItem.date == setLongDate(new Date(Date.now()))) {
          wellnessNot.value = false;
          welness.value = welnessItem;
        }
      });
    });
  });
};

onMounted(async () => {
  let storeUser = await store.get("user");
  if (storeUser !== "") {
    user.value = JSON.parse(storeUser).user;
  }

  get(
    "/wellness/user/" +
    user.value.id +
    "/week?date=" +
    setLongDate(new Date(Date.now())),
    { body: {} },
    true
  ).then((res: any) => {
    res.map((welnessItem: any) => {
      if (welnessItem.date == setLongDate(new Date(Date.now()))) {
        if (welnessItem.sleep !== null) {
          wellnessNot.value = false;
          welness.value = welnessItem;
        }
      }
    });

    weekWelness.value = res;
    weekWelnessTemp.value = res;
  });

  const ionSelect = document.querySelectorAll(".custom_nav");
  if (ionSelect === null) return;
  for (const elem of ionSelect) {
    const shadowRoot = elem.shadowRoot;
    if (shadowRoot === null) return;
    const style = document.createElement("style");
    style.textContent = `
        .button-inner {
        justify-content: flex-start !important;
        }
    `;
    shadowRoot.appendChild(style);
  }
});

onUpdated(() => {
  if (routes.name == "Home") {
    load();
  }
});
</script>
