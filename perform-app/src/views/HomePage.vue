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
          <img
            width="200px"
            src="@/assets/logo_perform_bandeau.png"
            alt="logo"
          />
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
            <img
              :src="user ? setPP() : ''"
              alt="profile"
              style="height: 80px; border-radius: 50%"
            />
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
                <div
                  style="
                    padding: 20px 20px 5px 20px;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                  "
                >
                  <h3 style="font-size: 13px; margin: 0px">
                    Saissiez le welness du jour :
                  </h3>
                  <ion-icon
                    style="
                      color: red;
                      border: 1px solid red;
                      border-radius: 5px;
                    "
                    @click="dismiss"
                    :icon="close"
                  />
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
                      <ion-range
                        :value="welness.pain"
                        aria-label="Range with ticks"
                        :ticks="true"
                        :snaps="true"
                        :min="0"
                        :max="10"
                        @ionChange="onIonChange($event, 'pain')"
                      ></ion-range>
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
                      <ion-range
                        :value="welness.sleep"
                        aria-label="Range with ticks"
                        :ticks="true"
                        :snaps="true"
                        :min="0"
                        :max="10"
                        @ionChange="onIonChange($event, 'sleep')"
                      ></ion-range>
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
                      <ion-range
                        :value="welness.stress"
                        aria-label="Range with ticks"
                        :ticks="true"
                        :snaps="true"
                        :min="0"
                        :max="10"
                        @ionChange="onIonChange($event, 'stress')"
                      ></ion-range>
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
                      <ion-range
                        aria-label="Range with ticks"
                        :ticks="true"
                        :snaps="true"
                        :min="0"
                        :max="10"
                        :value="welness.fatigue"
                        @ionChange="onIonChange($event, 'fatigue')"
                      ></ion-range>
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
                      <ion-range
                        aria-label="Range with ticks"
                        :ticks="true"
                        :snaps="true"
                        :value="welness.hydratation"
                        :min="0"
                        :max="10"
                        @ionChange="onIonChange($event, 'hydratation')"
                      ></ion-range>
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
            <ion-modal
              class="static-modal"
              ref="modalStats"
              trigger="open-modal-stats"
            >
              <ion-content>
                <div
                  style="
                    padding: 20px 20px 5px 20px;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    flex-wrap: wrap;
                  "
                >
                  <h3>Satistiques :</h3>
                  <ion-icon
                    style="
                      color: red;
                      border: 1px solid red;
                      border-radius: 5px;
                    "
                    @click="dismiss"
                    :icon="close"
                  />
                </div>
                <div style="padding: 0px 20px 5px 20px">
                  <h4 style="width: 100%; margin-top: 0px; text-align: center">
                    Semaine du 26/03 au 3/03
                  </h4>
                  <div
                    style="
                      width: 100%;
                      display: flex;
                      justify-content: space-between;
                    "
                  >
                    <ion-button fill="outline" style="font-size: 8px">
                      < Semaine précédente</ion-button
                    >
                    <ion-button fill="outline" style="font-size: 8px">
                      Semaine suivante ></ion-button
                    >
                  </div>
                  <div style="">
                    <canvas
                      width="400px"
                      height="300px"
                      min="0"
                      max="10"
                      id="acquisitions"
                    ></canvas>
                  </div>
                </div>
              </ion-content>
            </ion-modal>

            <div v-if="wellnessNot">
              <p style="text-align: center; margin-top: 10px; font-size: 16px">
                Saissiez votre welness du jour !
                <ion-button id="open-modal" expand="block"
                  >Saisir le wellness</ion-button
                >
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
                    <ion-range
                      disabled
                      :value="welness.pain"
                      aria-label="Range with ticks"
                      :ticks="true"
                      :snaps="true"
                      :min="0"
                      :max="10"
                      @ionChange="onIonChange($event, 'pain')"
                    ></ion-range>
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
                    <ion-range
                      disabled
                      :value="welness.sleep"
                      aria-label="Range with ticks"
                      :ticks="true"
                      :snaps="true"
                      :min="0"
                      :max="10"
                      @ionChange="onIonChange($event, 'sleep')"
                    ></ion-range>
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
                    <ion-range
                      disabled
                      :value="welness.stress"
                      aria-label="Range with ticks"
                      :ticks="true"
                      :snaps="true"
                      :min="0"
                      :max="10"
                      @ionChange="onIonChange($event, 'stress')"
                    ></ion-range>
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
                    <ion-range
                      disabled
                      aria-label="Range with ticks"
                      :ticks="true"
                      :snaps="true"
                      :min="0"
                      :max="10"
                      :value="welness.fatigue"
                      @ionChange="onIonChange($event, 'fatigue')"
                    ></ion-range>
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
                    <ion-range
                      disabled
                      aria-label="Range with ticks"
                      :ticks="true"
                      :snaps="true"
                      :value="welness.hydratation"
                      :min="0"
                      :max="10"
                      @ionChange="onIonChange($event, 'hydratation')"
                    ></ion-range>
                  </div>
                </div>
                <div
                  style="
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                  "
                >
                  <ion-button fill="outline" @click="showStats"
                    >Satistiques</ion-button
                  >
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
import { ref, onMounted, onUpdated, hydrate } from "vue";
import { store } from "@/store/store";
import { get } from "@/lib/callApi";
import routes from "@/router";
import type { Sport } from "@/types";
import { close, save } from "ionicons/icons";
import { patch, post } from "../lib/callApi";
import Chart from "chart.js/auto";

const api = import.meta.env.VITE_API_URL;

const wellnessNot = ref(true);

const welness = ref({
  sleep: 0,
  stress: 0,
  hydratation: 0,
  pain: 0,
  fatigue: 0,
  id: 4,
} as any);

const modal = ref(null);
const modalStats = ref(null);

const dismiss = () => {
  console.log(modal.value);
  modal.value.$el.dismiss();
};

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
  sports_user: [] as Sport[],
  user_injuries: [],
  users_wellness: [],
});

const setLongDate = (date: any) => {
  const year = date.getFullYear();
  const months = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDay() + 1).padStart(2, "0");
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

const showStats = async () => {
  modalStats.value.$el.present();
  const data = [
    {
      date: "2024-06-01",
      sleep: 8,
      fatigue: 3,
      hydratation: 7,
      pain: 2,
      stress: 5,
    },
    {
      date: "2024-06-02",
      sleep: 7,
      fatigue: 4,
      hydratation: 6,
      pain: 3,
      stress: 6,
    },
    {
      date: "2024-06-03",
      sleep: 6,
      fatigue: 5,
      hydratation: 5,
      pain: 4,
      stress: 4,
    },
    {
      date: "2024-06-04",
      sleep: 9,
      fatigue: 2,
      hydratation: 8,
      pain: 1,
      stress: 3,
    },
    {
      date: "2024-06-05",
      sleep: 5,
      fatigue: 6,
      hydratation: 4,
      pain: 5,
      stress: 7,
    },
    {
      date: "2024-06-06",
      sleep: 7,
      fatigue: 3,
      hydratation: 6,
      pain: 2,
      stress: 4,
    },
    {
      date: "2024-06-07",
      sleep: 8,
      fatigue: 2,
      hydratation: 7,
      pain: 1,
      stress: 5,
    },
  ];

  setTimeout(() => {
    console.log(document.getElementById("acquisitions"));
    new Chart(document.getElementById("acquisitions"), {
      type: "line",
      data: {
        labels: data.map((elem) => elem.date),
        datasets: [
          {
            label: "Sleep",
            data: data.map((elem) => elem.sleep),
          },
          {
            label: "Pain",
            data: data.map((elem) => elem.pain),
          },
          {
            label: "Stress",
            data: data.map((elem) => elem.stress),
          },
          {
            label: "Hydratation",
            data: data.map((elem) => elem.hydratation),
          },
          {
            label: "Fatigue",
            data: data.map((elem) => elem.fatigue),
          },
        ],
      },
      options: {
        scales: {
          y: {
            min: 0,
            max: 10,
          },
        },
      },
    });
  }, 100);
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

const onIonChange = ({ detail }, name) => {
  console.log("ionChange emitted value: ", detail.value, " name ", name);
  welness.value[name] = detail.value;
  console.log(welness.value[name]);
};

const setPP = () => {
  if (user.value.profile_picture.includes(api.split("//")[1])) {
    return user.value.profile_picture;
  } else {
    return api + user.value.profile_picture;
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
      user.value.users_wellness.map((welnessItem) => {
        console.log(
          "load ",
          welnessItem.date == setLongDate(new Date(Date.now()))
        );
        if (welnessItem.date == setLongDate(new Date(Date.now()))) {
          wellnessNot.value = false;
          welness.value = welnessItem;
          welness.value.id = 4;
          console.log(welness.value);
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

  user.value.users_wellness.map((welnessItem) => {
    console.log(welnessItem.date == setLongDate(new Date(Date.now())));
    if (welnessItem.date == setLongDate(new Date(Date.now()))) {
      wellnessNot.value = false;
      welness.value = welnessItem;
      welness.value.id = 4;
      console.log(welness.value);
    }
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
