<style scoped>
ion-modal {
  --height: 90%;
  --width: 90%;
  --border-radius: 16px;
  --box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
}

.input-div {
  width: 100%;
}

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

.input-div ion-item {
  border-radius: 30px;
  border: 1px solid #d4d4d4;
  min-height: 40px !important;
  height: 40px;

  width: 100%;
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
          <ion-button @click="showFilter">Filtres</ion-button>
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
      <ion-modal class="static-modal" ref="filterModal">
        <ion-content>
          <div style="
                    padding: 20px 20px 5px 20px;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    flex-wrap: wrap;
                  ">
            <h3> FILTRER </h3>
            <div class="input-div">
              <h4>Sports :</h4>
              <ion-list>
                <ion-item>
                  <ion-select @ionChange="updateSelectedSports" class="custom-ion-select" :value="sports_selected"
                    aria-label="Fruit" placeholder="Selectionner vos sports" :multiple="true"
                    :compareWith="compareWith">
                    <ion-select-option v-for="(sport, index) in sports" :value="{ id: sport.id, name: sport.name }"
                      :key="sport.id" aria-selected="true">{{ sport.name }}</ion-select-option>
                  </ion-select>
                </ion-item>
              </ion-list>
            </div>
            <div class="input-div">
              <h4>Matériels :</h4>
            </div>
            <div class="input-div">
              <h4>Muscles :</h4>
              <div style="
                  display: flex;
                  width: 100%;
                  margin-top: 16px;
                  justify-content: space-between;
                  align-items: center;
                ">
                <BodyComponent :height="'300'" :width="'300'" :viewOnly="'edit'"
                  :muscleSelected="exercises.zone_exercises" :setMuscleSelected='setMuscleSelected' />
              </div>
              <div class="input-div">
                <ion-button @click="filterExercice">
                  Filtrer
                </ion-button>
              </div>
            </div>
          </div>
        </ion-content>
      </ion-modal>
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
            <ion-list class="list-item" :inset="true" v-for="exercise in exercises_fav" :key="exercises.id"
              @click="goPage(exercise.fav_exercise.id)">
              <ion-item>
                <div class="exercice-img">
                  <label>{{ exercise.fav_exercise.name[0] }}</label>
                </div>
                <ion-label>{{ exercise.fav_exercise.name }}</ion-label>
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
  IonIcon,
  IonInput,
  IonContent,
  IonPage,
  IonSelect,
  IonSelectOption,
  IonButton,
  IonModal
} from "@ionic/vue";
import { get } from "../../lib/callApi";
import { onMounted, ref, onUpdated } from "vue";
import { chevronForwardOutline } from "ionicons/icons";
import "./index.css";
import router from "../../router";
import { useRoute } from "vue-router";
import { store } from "../../store/store";
import { Muscle, Sport } from "@/types/types";
import { BodyComponent } from "perform-body-component-lib";

const order = [
  { id: "orderByNameAsc", value: "Nom (Croissant)" },
  { id: "orderByNameDesc", value: "Nom (Décroissant)" },
  { id: "orderByIdAsc", value: "Id (Croissant)" },
  { id: "orderByIdDesc", value: "Id (Décroissant)" },
  { id: "orderByDateAsc", value: "Date (Croissant)" },
  { id: "orderByDateDesc", value: "Date (Décroissant)" },
  { id: "default", value: "Par défaut" },
];

const user_id = ref(0);
const tab = ref(null);
const filterModal = ref(null);
const searchValue = ref("");
const orderBy = ref({ id: "default", value: "Par défaut" });
const exercises: any = ref([]);
const exercises_fav: any = ref([]);
const sports = ref([] as Sport[])
const sports_selected = ref([] as Sport[]);
const navRoute = useRoute();
const muscles = ref([] as Muscle[])
const muscle_selected = ref([] as Muscle[]);

const compareWith = (o1, o2) => {
  return o1 && o2 ? o1.id === o2.id : o1 === o2;
};

const goPage = (id: any) => {
  router.push({ name: "ExercisesView", params: { id: id } });
};

const setMuscleSelected = (key: string, action: string) => {
  if (action === 'add') {
    const findKey =
      muscle_selected.value.filter(function (element: string) {
        return element === key
      }).length == 0
    if (findKey) {
      muscle_selected.value.push(key)
    }
  } else {
    // Trouver l'index de la valeur à supprimer
    var index = muscle_selected.value.indexOf(key)

    if (index !== -1) {
      // Supprimer la valeur à l'index trouvé
      muscle_selected.value.splice(index, 1)
    }
  }
}

const handleOrderChange = (event: any) => {
  const option = {
    body: {},
    search: searchValue.value != "" ? searchValue.value : "",
    orderBy: {},
  }; /* as IERequestOptions; */
  let find = false;
  order.map((order) => {
    if (order.id === event.detail.value) {
      orderBy.value = order;
      find = true;
    }
  });
  if (!find) {
    orderBy.value = { id: "default", value: "Par défaut" };
  }
  option.orderBy = orderBy.value;
  router.replace({
    path: navRoute.path,
    query: Object.assign({}, navRoute.query, { orderBy: orderBy.value.id }),
  });
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

const jointByComa = (array: Array<string | Sport>, name: string = '') => {
  let stringWithCommas = ''
  for (let i = 0; i < array.length; i++) {
    if (name == 'sport') {
      stringWithCommas += array[i].id

    } else {
      stringWithCommas += array[i]
    }
    if (i < array.length - 1) {
      stringWithCommas += ', '
    }
  }
  return stringWithCommas
}

const filterExercice = () => {
  //showFilter.value = false
  const option = {} as any
  /*   if (materials_id_filter.value.length > 0) {
      option.material_id = jointByComa(materials_id_filter.value)
    } */
  console.log(muscle_selected.value)
  console.log(sports_selected.value)
  if (muscle_selected.value.length > 0) {
    option.workzone_code = jointByComa(muscle_selected.value)
  } else {
    option.workzone_code = ''
  }
  if (sports_selected.value.length > 0) {
    option.sport_id = jointByComa(sports_selected.value, 'sport')
  } else {
    option.sport_id = ""
  }
  router.replace({
    path: navRoute.path,
    query: Object.assign({}, navRoute.query, option)
  })
  getExercises()
  filterModal.value.$el.dismiss();
}

const getExercises = async () => {
  const option = {
    body: {},
    /*     itemsPerPage: itemsPerPage.value.toString(),
        page: page.value.toString(), */
    /*     search: {
          name: ''
        }, */
    orderBy: { id: 'default', value: 'Par défaut' }
  } as any
  if (orderBy.value) {
    option.orderBy = orderBy.value
  }
  /*  if (searchValue.value !== '') {
     option.search = {
       name: searchValue.value
     }
   } */

  /*   if (materials_id_filter.value.length > 0) {
      option.material_id = jointByComa(materials_id_filter.value)
    } */

  if (sports_selected.value.length > 0) {
    option.sport_id = jointByComa(sports_selected.value, 'sport')
  }

  if (muscle_selected.value.length > 0) {
    option.workzone_code = jointByComa(muscle_selected.value)
  }

  get('/admin/exercises', option).then((res) => {
    if (res.status > 300) {
      /* error_message.value = res.data
      alertErr.value = true
      error_title.value = 'Error while retrieve exercises' */
    } else {
      exercises.value = res.results
      /*       exercisesCount.value = res.count
            pagination.value = Math.ceil(exercisesCount.value / itemsPerPage.value) */
    }
  })
}

const showFilter = () => {
  setTimeout(() => {
    const ionSelect = document.querySelectorAll(".custom-ion-select");
    console.log(ionSelect)
    if (ionSelect === null) return;
    for (const elem of ionSelect) {
      const shadowRoot = elem.shadowRoot;
      if (shadowRoot === null) return;
      const style = document.createElement("style");
      style.textContent = `
          .select-wrapper-inner {
          width: 100%; /* Ajustez cette valeur selon vos besoins */
          justify-content: space-between;
        }
      `;
      shadowRoot.appendChild(style);
    }
  }, 100)
  filterModal.value.$el.present();
}

const updateSelectedSports = (change) => {
  sports_selected.value = change.detail.value;
  console.log(sports_selected.value)
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
};

const load = () => {
  get("/exercises/", { body: {} }, false).then((res: any) => {
    if (res.status > 300) {
    } else {
      exercises.value = res.results;
    }
  });
  get("/userfavexercises/user/" + user_id.value + "/", { body: {} }, true).then(
    (res: any) => {
      if (res.status > 300 || res.length <= 0) {
        exercises_fav.value = [];
      } else {
        exercises_fav.value = res;
      }
    }
  );
};

onUpdated(() => {
  if (navRoute.name == "Exercises") {
    load();
  }
});

onMounted(() => {
  store.get("user").then((res) => {
    user_id.value = JSON.parse(res).user.id;
    get(
      "/userfavexercises/user/" + user_id.value + "/",
      { body: {} },
      true
    ).then((res: any) => {
      if (res.status > 300) {
      } else {
        exercises_fav.value = res;
      }
    });
  });

  get("/exercises", { body: {} }, false).then((res: any) => {
    if (res.status > 300) {
    } else {
      exercises.value = res.results;
    }
  });

  get("/sports", { body: {} }, false).then((res: any) => {
    if (res.status > 300) {
    } else {
      sports.value = res.results;
    }
  });

  get("/workzones", { body: {} }, false).then((res: any) => {
    if (res.status > 300) {
    } else {
      muscles.value = res.results;
    }
  });

});
</script>
