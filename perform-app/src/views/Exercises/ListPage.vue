<style scoped></style>

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
          <div class="orderByParent">
            <div class="orderBy">
              <label>Trier par:</label>
              <v-select :items="order" :model-value="orderBy" item-title="value" item-value="id"
                @update:modelValue="changeOrder($event)"></v-select>
            </div>
          </div>
        </div>
      </div>
      <ion-segment @ionChange="handleChange($event)" value="all">
        <ion-segment-button value="all">
          <ion-label>Tous les exercices</ion-label>
        </ion-segment-button>
        <ion-segment-button value="favorites">
          <ion-label>Mes favoris</ion-label>
        </ion-segment-button>
      </ion-segment>
    </div>

    <ion-content color="light">
      <ion-list v-if="showExercises" class="list-item" :inset="true" v-for="exercise in exercises" :key="exercises.id"
        @click="goPage(exercise.id)">
        <ion-item>
          <div class="exercice-img">
            <label>{{ exercise.name[0] }}</label>
          </div>
          <ion-label>{{ exercise.name }}</ion-label>
          <ion-icon :icon="chevronForwardOutline"></ion-icon>
        </ion-item>
      </ion-list>
      <ion-list v-if="!showExercises" class="list-item" :inset="true" v-for="exercise in exercises" :key="exercises.id">
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

const searchValue = ref("");
const orderBy = ref({ id: "default", value: "Par défaut" });
const showExercises = ref(true);
const exercises: any = ref([]);

const navRoute = useRoute()

const changeOrder = (e: any) => {
  let find = false
  order.map((order) => {
    if (order.id === e) {
      orderBy.value = order;
      find = true
    }
  })
  if (!find) {
    orderBy.value = { id: 'default', value: 'Par défaut' }
  }
  router.replace({
    path: navRoute.path,
    query: Object.assign({}, navRoute.query, { orderBy: e })
  })
}

const goPage = (id: any) => {
  router.push({ name: "ExercisesView", params: { id: id } });
};

const handleChange = (event: any) => {
  if (event.detail.value == "all") {
    showExercises.value = true;
  } else {
    showExercises.value = false;
  }
};

const handleOrderChange = (event: any) => {
  orderBy.value = event.detail.value;
  const option = {
    body: {},
    search: searchValue.value != "" ? searchValue.value : "",
    orderBy: { id: event.detail.value },
  }; /* as IERequestOptions; */
  console.log(orderBy.value);
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

  get("/exercises", option, false).then((res) => {
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
    option.orderBy.id = orderBy.value;
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
