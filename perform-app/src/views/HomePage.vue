<style scoped></style>

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
            <div v-if="!profilePicture" class="profile_placeholder">
              {{ user.first_name[0] }}
            </div>
            <img v-else :src="profilePicture" alt="profile" class="profile_img" />
          </div>
        </div>
        <div class="block_100">
          <div class="users_infos">
            <UserInfo title="Discipline(s)"
              :info="user.sports_user.slice(0, 2).map((sport: any) => sport.sport.name)" />
            <UserInfo title="Âge" :info="user.age + ' ans'" />
            <UserInfo title="Poids" :info="user.weight + ' kg'" />
            <UserInfo title="Taille" :info="user.size + ' cm'" />
          </div>
        </div>
        <div :class="hideWelness
          ? 'block_100 wellness_100 wellness_100_hidden'
          : 'block_100 wellness_100'
          ">
          <div class="display_flex" @click="hideWelness = !hideWelness">
            <h3>Welness</h3>
            <ion-icon :icon="hideWelness ? chevronUpOutline : chevronDownOutline" />
          </div>
          <ion-modal ref="modal" trigger="open-modal">
            <ion-content>
              <div class="modal-header">
                <h3>Saissiez le welness du jour :</h3>
                <ion-icon class="close-icon" @click="dismiss" :icon="close" />
              </div>
              <div class="divs_range">
                <WellnessRange id="pain_range" title="Douleurs" :value="welness.pain" :min="0" :max="10"
                  descriptionStart="Journée douloureuse" descriptionEnd="Aucune douleur"
                  @change="onIonChange($event, 'pain')" />
                <WellnessRange id="sleep_range" title="Sommeil" :value="welness.sleep" :min="0" :max="10"
                  descriptionStart="Mauvais sommeil" descriptionEnd="Très bon sommeil"
                  @change="onIonChange($event, 'sleep')" />
                <WellnessRange id="stress_range" title="Stress" :value="welness.stress" :min="0" :max="10"
                  descriptionStart="Journée stressante" descriptionEnd="Journée détendue"
                  @change="onIonChange($event, 'stress')" />
                <WellnessRange id="fatigue_range" title="Fatigue" :value="welness.fatigue" :min="0" :max="10"
                  descriptionStart="Très fatigué" descriptionEnd="Je pète la forme"
                  @change="onIonChange($event, 'fatigue')" />
                <WellnessRange id="hydratation_range" title="Hydratation" :value="welness.hydratation" :min="0"
                  :max="10" descriptionStart="- de 1L" descriptionEnd="+ de 3L"
                  @change="onIonChange($event, 'hydratation')" />
                <div class="display_flex" style="justify-content: center; margin-top: 10px">
                  <ion-button v-if="wellnessNot" @click="postWelness">
                    Enregistrer
                  </ion-button>
                  <ion-button size="small" v-else @click="patchWelness">
                    Mettre à jour
                  </ion-button>
                </div>
              </div>
            </ion-content>
          </ion-modal>
          <ion-modal class="static-modal" ref="modalStats">
            <ion-content>
              <div class="modal-header">
                <h3>Satistiques :</h3>
                <ion-icon class="close-icon" @click="modalStats ? modalStats.$el.dismiss() : ''" :icon="close" />
              </div>
              <div class="modal-body">
                <h4>Semaine du {{ weekRange }}</h4>
                <div class="week-navigation">
                  <ion-button @click="setPreviousWeek" fill="outline">
                    < Semaine précédente</ion-button>
                      <ion-button :disabled="getWeekNumber(new Date(Date.now())) == getWeekNumber(tempDate)"
                        @click="setNextWeek" fill="outline">Semaine
                        suivante ></ion-button>
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
          <div v-else class="divs_range show_divs_range" :class="hideWelness ? 'show_divs_range_hidden' : ''">
            <WellnessRange id="pain_range" title="Douleurs" :value="welness.pain" :min="0" :max="10" disabled
              descriptionStart="Journée douloureuse" descriptionEnd="Aucune douleur" />
            <WellnessRange id="sleep_range" title="Sommeil" :value="welness.sleep" :min="0" :max="10" disabled
              descriptionStart="Mauvais sommeil" descriptionEnd="Très bon sommeil" />
            <WellnessRange id="stress_range" title="Stress" :value="welness.stress" :min="0" :max="10" disabled
              descriptionStart="Journée stressante" descriptionEnd="Journée détendue" />
            <WellnessRange id="fatigue_range" title="Fatigue" :value="welness.fatigue" :min="0" :max="10" disabled
              descriptionStart="Très fatigué" descriptionEnd="Je pète la forme" />
            <WellnessRange id="hydratation_range" title="Hydratation" :value="welness.hydratation" :min="0" :max="10"
              disabled descriptionStart="- de 1L" descriptionEnd="+ de 3L" />
            <div class="actions">
              <ion-button size="small" fill="outline" @click="showStats">Satistiques</ion-button>
              <ion-button size="small" @click="modal.$el.present()">Editer</ion-button>
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
} from "@ionic/vue";
import "@/assets/base.css";
import "@/assets/main.css";
import "./homepage.css";
import { ref, onMounted, computed, onUpdated, markRaw, onBeforeUnmount } from "vue";
import { store } from "../store/store";
import { useRoute } from "vue-router";
import { close, chevronDownOutline, chevronUpOutline } from "ionicons/icons";
import { patch, post, get } from "../lib/callApi";
import UserInfo from "@/components/UserInfo/UserInfo.vue";
import WellnessRange from "@/components/WellnessRange/WellnessRange.vue";
import Chart from "chart.js/auto";

const routes = useRoute();
const api = import.meta.env.VITE_API_URL;

const hideWelness = ref(false);
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

const currentDate = computed(() => new Date(Date.now()).toLocaleString("fr").split(" ")[0]);

const weekRange = computed(() => {
  const start = new Date(weekWelnessTemp.value[0].date);
  const end = new Date(weekWelnessTemp.value[6].date);
  return `${start.getDate()}/${start.getMonth() + 1} au ${end.getDate()}/${end.getMonth() + 1}`;
});

const dismiss = () => {
  if (modal.value) {
    modal.value.$el.dismiss();
  }
};

const setLongDate = (date: any) => {
  return date.toISOString().split('T')[0];
};

const postWelness = async () => {
  const response = await post("/wellness/", {
    body: {
      sleep: welness.value.sleep,
      hydratation: welness.value.hydratation,
      fatigue: welness.value.fatigue,
      pain: welness.value.pain,
      stress: welness.value.stress,
      user: user.value.id,
      date: setLongDate(new Date()),
    },
  }, true);

  if (response.status <= 301) {
    const userResponse = await get("/admin/users_all/me/", { body: {} }, true);
    await store.set("user", JSON.stringify(userResponse));
    welness.value = response;
    wellnessNot.value = false;
    dismiss();
  }
};

const chart = ref(null) as any;

const showStats = async () => {
  modalStats.value.$el.present();
  weekWelnessTemp.value = weekWelness.value;
  setTimeout(() => {
    createChart(weekWelness.value);
  }, 100);
};

const setPreviousWeek = async () => {
  const newDate = new Date(tempDate.value);
  newDate.setDate(newDate.getDate() - 7);
  tempDate.value = newDate;
  await updateWeekWelness();
};

const setNextWeek = async () => {
  const newDate = new Date(tempDate.value);
  newDate.setDate(newDate.getDate() + 7);
  tempDate.value = newDate;
  await updateWeekWelness();
};

const updateWeekWelness = async () => {
  const res = await get(`/wellness/user/${user.value.id}/week?date=${setLongDate(tempDate.value)}`, { body: {} }, true);
  weekWelnessTemp.value = JSON.parse(JSON.stringify(res));
  chart.value.destroy();
  createChart(weekWelnessTemp.value);
};

const createChart = (data: any) => {
  //@ts-expect-error
  chart.value = markRaw(new Chart(document.getElementById("acquisitions"), {
    type: "line",
    data: {
      labels: ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"],
      datasets: [
        { label: "Sommeil", data: data.map((elem: { sleep: any }) => elem.sleep) },
        { label: "Douleurs", data: data.map((elem: { pain: any }) => elem.pain) },
        { label: "Stress", data: data.map((elem: { stress: any }) => elem.stress) },
        { label: "Hydratation", data: data.map((elem: { hydratation: any }) => elem.hydratation) },
        { label: "Fatigue", data: data.map((elem: { fatigue: any }) => elem.fatigue) },
      ],
    },
    options: {
      spanGaps: true,
      scales: { y: { min: 0, max: 10 } },
      fullSize: true,
    },
  }));
};

const patchWelness = async () => {
  const response = await patch(`/wellness/${welness.value.id}/`, {
    body: {
      sleep: welness.value.sleep,
      hydratation: welness.value.hydratation,
      fatigue: welness.value.fatigue,
      pain: welness.value.pain,
      stress: welness.value.stress,
    },
  }, true);

  if (response.status <= 301) {
    const userResponse = await get("/admin/users_all/me/", { body: {} }, true);
    await store.set("user", JSON.stringify(userResponse));
    dismiss();
  }
};

const onIonChange = ({ detail }: any, name: any) => {
  welness.value[name] = detail.value;
};

const profilePicture = computed(() => {
  if (user.value.profile_picture?.includes(api.split("//")[1])) {
    return user.value.profile_picture.replace('http', 'https');
  }
  return user.value.profile_picture ? api + user.value.profile_picture : "";
});

const loadUser = async () => {
  const storeUser = await store.get("user");
  if (storeUser) {
    user.value = JSON.parse(storeUser).user;
  }
  await refreshUser();
};

const refreshUser = async () => {
  const response = await get(`/admin/users_all/${user.value.id}`, { body: {} }, true);
  user.value = response;
  const userToSet = {
    user: response,
    access: JSON.parse(await store.get("user")).access,
    refresh: JSON.parse(await store.get("user")).refresh,
  };
  store.set("user", JSON.stringify(userToSet));
  checkUserWellness();
};

const checkUserWellness = async () => {
  const res = await get(`/wellness/user/${user.value.id}/week?date=${setLongDate(new Date())}`, { body: {} }, true);
  res.forEach((welnessItem: any) => {
    if (welnessItem.date === setLongDate(new Date())) {
      wellnessNot.value = false;
      welness.value = welnessItem;
    }
  });
};

function getWeekNumber(d: any) {
  // Créer une copie de la date
  d = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
  d.setUTCDate(d.getUTCDate() + 4 - (d.getUTCDay() || 7));
  let yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
  //@ts-expect-error
  let weekNo = Math.ceil((((d - yearStart) / 86400000) + 1) / 7);
  return weekNo;
}

onIonViewWillEnter(async () => {
  await loadUser();

  const res = await get(`/wellness/user/${user.value.id}/week?date=${setLongDate(new Date())}`, { body: {} }, true);
  res.forEach((welnessItem: any) => {
    if (welnessItem.date === setLongDate(new Date())) {
      if (welnessItem.sleep !== null) {
        wellnessNot.value = false;
        welness.value = welnessItem;
      }
    }
  });

  weekWelness.value = res;
  weekWelnessTemp.value = res;

  document.querySelectorAll(".custom_nav").forEach(elem => {
    const shadowRoot = elem.shadowRoot;
    if (shadowRoot) {
      const style = document.createElement("style");
      style.textContent = `.button-inner { justify-content: flex-start !important; }`;
      shadowRoot.appendChild(style);
    }
  });
});

onIonViewWillLeave(() => {
  if (chart.value) {
    chart.value.destroy();
  }
})
</script>
