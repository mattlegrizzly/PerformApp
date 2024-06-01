<style scoped>
ion-modal {
  --height: 70%;
  --width: 80%;
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
  font-size: 4px !important;
  text-align: center;
  color: #aeaeae;
  transform: scale(0.7);
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
            <div v-if="wellnessNot">
              <p style="text-align: center; margin-top: 10px; font-size: 16px">
                Saissiez votre welness du jour !
                <ion-button id="open-modal" expand="block"
                  >Open Modal</ion-button
                >

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
                            :min="0"
                            :max="10"
                            @ionChange="onIonChange($event, 'hydratation')"
                          ></ion-range>
                        </div>
                      </div>
                      <div style="display: flex; justify-content: center">
                        <ion-button> Enregistrer </ion-button>
                      </div>
                    </div>
                  </ion-content>
                </ion-modal>
              </p>
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
  IonButtons,
  IonButton,
  IonModal,
  IonItem,
  IonList,
  IonAvatar,
  IonImg,
  IonLabel,
  IonToolbar,
  IonTitle,
  IonContent,
  IonPage,
} from "@ionic/vue";
import "@/assets/base.css";
import "@/assets/main.css";
import { ref, onMounted, onUpdated } from "vue";
import { store } from "@/store/store";
import { get } from "@/lib/callApi";
import routes from "@/router";
import type { Sport } from "@/types";
import { close, save } from "ionicons/icons";
const api = import.meta.env.VITE_API_URL;

const wellnessNot = ref(true);

const modal = ref(null);

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

const onIonChange = ({ detail }, name) => {
  console.log("ionChange emitted value: ", detail.value, " name ", name);
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
      res;
      const userToSet = {
        user: res,
        access: json.access,
        refresh: json.refresh,
      };
      store.set("user", JSON.stringify(userToSet));
    });
  });
};

onMounted(async () => {
  let storeUser = await store.get("user");
  if (storeUser !== "") {
    user.value = JSON.parse(storeUser).user;
  }

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
