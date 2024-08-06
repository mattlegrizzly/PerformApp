<style scoped>
#tabs-exercise v-tabs-window {
  margin: 10px;
}

.records-div {
  margin-bottom: 20px;
}

.record-unit::part(native) {
  padding-left: 0 !important;
}

.records-list {
  margin-top: 15px;
}
</style>

<template>
  <ion-page data-page="Records">
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton url="profile" text="Retour" back="back" />
        </div>
        <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
          Mes records
        </h1>
      </div>
      <v-tabs id="tabs-exercise" v-model="tab">
        <v-tab value="one">Générales</v-tab>
        <v-tab value="two">Mes sports</v-tab>
      </v-tabs>
      <v-card-text>
        <div
          style="width: 100%; justify-content: center; align-items: center"
          :style="find ? 'display:none;' : 'display:flex'"
          key="spinner"
        >
          <v-progress-circular
            color="primary"
            indeterminate
          ></v-progress-circular>
        </div>

        <v-tabs-window v-model="tab">
          <v-tabs-window-item
            :style="find ? 'display:block;' : 'display:none'"
            value="one"
          >
            <div class="records-div" v-for="(items, key) in records" :key="key">
              <h4 style="padding-left: 10px; margin-bottom: 10px">{{ key }}</h4>
              <div
                v-for="(item, key) in items"
                :key="item.id"
                class="records-list"
              >
                <ion-label
                  position="stacked"
                  style="
                    margin-left: 10px;
                    font-weight: 500;
                    font-style: italic;
                  "
                  >Thème : {{ key }}</ion-label
                >
                <ion-list v-for="rec of item">
                  <ion-item
                    @click="router.push('/show_records/' + rec.record)"
                    class="record-unit"
                  >
                    <p>{{ rec.record_name }}</p>
                    <div
                      style="
                        display: flex;
                        justify-content: center;
                        align-items: center;
                      "
                    >
                      <p style="font-size: 15px">{{ rec.formatted_record }}</p>
                      <ion-icon :icon="chevronForwardOutline"></ion-icon>
                    </div>
                  </ion-item>
                </ion-list>
              </div>
            </div>
          </v-tabs-window-item>

          <v-tabs-window-item value="two"
          :style="find ? 'display:block;' : 'display:none'"
          >
            <div
              class="records-div"
              v-for="(items, key) in recordsSports"
              :key="key"
            >
              <h4 style="padding-left: 10px; margin-bottom: 10px">{{ key }}</h4>
              <div
                v-for="(item, key) in items"
                :key="item.id"
                class="records-list"
              >
                <ion-label
                  position="stacked"
                  style="
                    margin-left: 10px;
                    font-weight: 500;
                    font-style: italic;
                  "
                  >Thème : {{ key }}</ion-label
                >
                <ion-list v-for="rec of item">
                  <ion-item
                    @click="router.push('/show_records/' + rec.record)"
                    class="record-unit"
                  >
                    <p>{{ rec.record_name }}</p>
                    <div
                      style="
                        display: flex;
                        justify-content: center;
                        align-items: center;
                      "
                    >
                      <p style="font-size: 15px">{{ rec.formatted_record }}</p>
                      <ion-icon :icon="chevronForwardOutline"></ion-icon>
                    </div>
                  </ion-item>
                </ion-list>
              </div>
            </div>
          </v-tabs-window-item>
        </v-tabs-window>
      </v-card-text>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { chevronForwardOutline } from "ionicons/icons";
import {
  IonContent,
  IonPage,
  onIonViewWillEnter,
  IonList,
  IonItem,
  IonIcon,
  IonLabel,
} from "@ionic/vue";
import { ref, watch } from "vue";
import "@/assets/base.css";
import "@/assets/main.css";
import NavButton from "../../components/NavButton/NavButton.vue";
import { useRouter } from "vue-router";
import { get } from "../../lib/callApi";
import "../Exercises/index.css";
import { store } from "../../store/store";
import { useErrorHandler } from "../../lib/useErrorHandler";

const { triggerError } = useErrorHandler() as any;
const tab = ref(null);

const find = ref(false);

const router = useRouter();

const records = ref([]) as any;
const recordsSports = ref([]) as any;

const tabOneStyle = ref(false);
const tabTwoStyle = ref(false);

watch(tab, () => {
  if(find.value == true && tabTwoStyle.value == false){
    find.value = false;
  }
  if(find.value == true && tabOneStyle.value == false){
    find.value = false;
  }
  if (tab.value == "one" && tabOneStyle.value === false) {
    setShadowStyle();
    tabOneStyle.value = true;
  }
  if (tab.value == "two" && tabTwoStyle.value === false) {
    
    setShadowStyle();
    tabTwoStyle.value = true;
  }
});

const setShadowStyle = () => {
  let count = 0;
  let isFind = false;
  setTimeout(() => {
    while (isFind == false && count < 3) {
      const items = document.querySelectorAll(".record-unit");
      
      if (items) {
        isFind = true;
        find.value = true;
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
  }, 500);
};

onIonViewWillEnter(async () => {
  find.value = false;
  let storeUser = await store.get("user");
  let stringifyUser = JSON.parse(storeUser);
  if (stringifyUser !== "") {
    
    get(
      "/records_user/by-theme-sports?user_id=" + stringifyUser.user.id,
      { body: {} },
      true
    ).then((res) => {
      if (res.status > 300) {
        triggerError("Erreur lors de la récupération des records");
      } else {
        records.value = res;
      }
    });

    get(
      "/records_user/by-user-sports?user_id=" + stringifyUser.user.id,
      { body: {} },
      true
    ).then((res) => {
      if (res.status > 300) {
        triggerError("Erreur lors de la récupération des records");
      } else {
        recordsSports.value = res;
      }
    });
    setShadowStyle();
  }
});
</script>
