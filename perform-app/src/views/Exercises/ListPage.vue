<style scoped>
.orderBy {
  width: 100%;
  right: 0px;
}

.orderBy .v-field__field {
  height: 30px;
  display: flex;
  align-items: center;
}


.orderBy .v-field__field .v-field__input {
  padding: 0px !important;
  padding-left: 20px !important;
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 14px;
}

.orderByParent {
  width: 45%;
  display: flex;
  justify-content: end;
}

.orderBy .v-input .v-input__details {
  display: none;
}
</style>

<template>
  <ion-page>
    <div id="header-wrapper">
      <div class="perform-page">
        <h1 style="margin-top: 0px">Exercices</h1>
        <ion-label>Rechercher un exercice :</ion-label>
        <ion-input id="search-input" fill="outline" slot="end" placeholder="Cherchez un exercice" shape="round"
          @ionInput="handleSearchInput($event)"></ion-input>
        <div class="filter-div">
          <ion-button>Filtres</ion-button>
          <ion-list class="filter-item">
            <ion-item>
              <ion-select aria-label="Trier par" interface="popover" placeholder="Trier par"
                @ionChange="handleOrderChange($event)">
                <ion-select-option v-for="elem in order" :key="elem.id" :value="elem.id">{{ elem.value
                  }}</ion-select-option>
              </ion-select>
            </ion-item>
          </ion-list>
        </div>
      </div>
      <v-tabs id="tabs-exercise" v-model="tab">
        <v-tab value="one">Tous les exercices</v-tab>
        <v-tab value="two">Mes favoris</v-tab>
      </v-tabs>
    </div>

    <ion-content color="light">
      <v-card-text>
        <v-tabs-window v-model="tab">
          <v-tabs-window-item value="one">
            <ion-list class="list-item" :inset="true" v-for="exercise in exercises" :key="exercises.id"
              @click="goPage(exercise.id)">
              <ion-item>
                <div class="exercice-img">
                  <label>{{ exercise.name[0] }}</label>
                </div>
                <ion-label>{{ exercise.name }}</ion-label>
                <ion-icon :icon="chevronForwardOutline"></ion-icon>
              </ion-item>
            </ion-list>
          </v-tabs-window-item>

          <v-tabs-window-item value="two">

            <ion-list class="list-item" :inset="true" v-for="exercise in exercises" :key="exercises.id">
              <ion-item>
                <div class="exercice-img">
                  <label>oui</label>
                </div>
                <ion-label>oui</ion-label>
                <ion-icon :icon="chevronForwardOutline"></ion-icon>
              </ion-item>
              <ion-item>
                <div class="exercice-img">
                  <label>{{ exercise.name[0] }}</label>
                </div>
                <ion-label>{{ exercise.name }}</ion-label>
                <ion-icon :icon="chevronForwardOutline"></ion-icon>
              </ion-item>
            </ion-list>
          </v-tabs-window-item>

        </v-tabs-window>
      </v-card-text>


    </ion-content>
  </ion-page>
</template>

<script lang="ts" setup>
import {
  IonLabel,
  IonList,
  IonItem,
  IonSegment,
  IonSegmentButton,
  IonIcon,
  IonInput,
  IonContent,
  IonPage,
  IonSelect,
  IonSelectOption,
  IonButton,
} from "@ionic/vue";
import { get } from "../../lib/callApi";
import { onMounted, ref } from "vue";
import { chevronForwardOutline } from "ionicons/icons";
import "./index.css";
import router from "../../router";
import { useRoute } from 'vue-router'

const order = [
  { id: "orderByNameAsc", value: "Nom (Croissant)" },
  { id: "orderByNameDesc", value: "Nom (Décroissant)" },
  { id: "orderByIdAsc", value: "Id (Croissant)" },
  { id: "orderByIdDesc", value: "Id (Décroissant)" },
  { id: "orderByDateAsc", value: "Date (Croissant)" },
  { id: "orderByDateDesc", value: "Date (Décroissant)" },
  { id: "default", value: "Par défaut" },
];

const tab = ref(null)
const searchValue = ref("");
const orderBy = ref({ id: "default", value: "Par défaut" });
const showExercises = ref(true);
const exercises: any = ref([]);

const navRoute = useRoute()


const goPage = (id: any) => {
  router.push({ name: "ExercisesView", params: { id: id } });
};


const handleOrderChange = (event: any) => {

  const option = {
    body: {},
    search: searchValue.value != "" ? searchValue.value : "",
    orderBy: {},
  }; /* as IERequestOptions; */
  console.log(orderBy.value);
  let find = false
  order.map((order) => {
    console.log(order)
    if (order.id === event.detail.value) {
      orderBy.value = order;
      find = true

    }
  })
  if (!find) {
    orderBy.value = { id: 'default', value: 'Par défaut' }
  }
  option.orderBy = orderBy.value
  router.replace({
    path: navRoute.path,
    query: Object.assign({}, navRoute.query, { orderBy: orderBy.value.id })
  })
  /* if (orderBy.value) {
    option.orderBy = orderBy.value;
  }
  if (materials_id_filter.value.length > 0) {
    option.material_id = materials_id_filter.value;
  }
  if (muscle_selected.value.length > 0) {
    option.workzone_code = muscle_selected.value;
  }
  if (sport_selected.value.length > 0) {
    option.sport_id = sport_selected.value;
  } */

  get("/exercises/", option, false).then((res) => {
    if (res.status > 300) {
    } else {
      exercises.value = res.results;
    }
  });
};
const handleSearchInput = (event: any) => {
  searchValue.value = event.target.value;
  const option = {
    body: {},
    search: event.target.value,
    orderBy: {
      id: "",
    },
  }; /* as IERequestOptions; */
  if (orderBy.value) {
    option.orderBy = orderBy.value;
  }
  /*
  if (materials_id_filter.value.length > 0) {
    option.material_id = materials_id_filter.value;
  }
  if (muscle_selected.value.length > 0) {
    option.workzone_code = muscle_selected.value;
  }
  if (sport_selected.value.length > 0) {
    option.sport_id = sport_selected.value;
  } */

  get("/exercises", option, false).then((res) => {
    if (res.status > 300) {
    } else {
      exercises.value = res.results;
    }
  });
};

onMounted(() => {
  get("/exercises", { body: {} }, false).then((res: any) => {
    if (res.status > 300) {
    } else {
      exercises.value = res.results;
    }
  });
});
</script>
