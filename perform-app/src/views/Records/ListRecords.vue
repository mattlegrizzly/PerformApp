<style scoped>
#tabs-exercise v-tabs-window{
    margin: 10px
}


.records-div {
    margin-bottom: 20px;
}

.record-unit::part(native) {
    padding-left: 0 !important;
}


</style>

<template>
  <ion-page>
    <ion-content >
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
          style="
            width: 100%;
            justify-content: center;
            align-items: center;
          "
          :style="find ? 'display:none;': 'display:flex'"
          key="spinner"
          
        >
          <v-progress-circular
            color="primary"
            indeterminate
          ></v-progress-circular>
        </div>
      
        <v-tabs-window 
        v-model="tab">
          <v-tabs-window-item  :style="find ? 'display:block;' : 'display:none'
                " value="one">
            <div class="records-div" v-for="(items, key) in records" :key="key">
              <h4 style="padding-left: 10px;">{{ key }}</h4>
              <ion-list v-for="item in items" :key="item.id" class="records-list">
                <ion-item @click="router.push('/show_records/'+item.record)" class="record-unit" >
                        <p>{{ item.record_name }}</p>
                        <div style="display: flex; justify-content: center; align-items: center;">
                          <p style="font-size: 15px">{{ item.units == "time" ? item.time_value : item.weight_value+'kg' }}</p>
                          <ion-icon :icon="chevronForwardOutline"></ion-icon>
                        </div>
                </ion-item>
              </ion-list>
            </div>
          </v-tabs-window-item>

          <v-tabs-window-item value="two"> </v-tabs-window-item>
        </v-tabs-window>
      </v-card-text>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  chevronForwardOutline
} from "ionicons/icons";
import { IonContent, IonPage, onIonViewWillEnter , IonList, IonItem, IonIcon} from "@ionic/vue";
import { ref } from "vue";
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

const records = ref([
]) as any;

onIonViewWillEnter(async () => {
  find.value =  false;
  let storeUser = await store.get("user");
  let stringifyUser = JSON.parse(storeUser)
  if (stringifyUser !== "") {
    console.log(stringifyUser)
    get("/records_user/by-user?user_id=" +stringifyUser.user.id, { body: {} }, true).then((res) => {
      if (res.status > 300) {
        triggerError("Erreur lors de la récupération des records");
      } else {
        records.value = res;
      }
    });
    
    let count = 0;
      setTimeout(() => {
      while(find.value == false && count < 3){
        console.log('find ', find)
        console.log('count  ', count)
          const items = document.querySelectorAll('.record-unit');
      
          if (items){
            find.value = true;
            count = 4;
            console.log(find)
              for (let elem of items){
                const style = document.createElement('style');
        
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
        },400)
    
  }
});
</script>
