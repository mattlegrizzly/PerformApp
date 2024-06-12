<style scoped>
ion-modal {
  --height: 90%;
  --width: 90%;
  --border-radius: 16px;
  --box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
}

.list-md.list-inset {
  padding-top: 0px !important;
  padding-bottom: 0px !important;
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

.input-fill-outline.sc-ion-input-md-h .input-outline-start.sc-ion-input-md {
  border-width: 0px !important;
  width: 0px !important;
}


.input-fill-outline.sc-ion-input-md-h .input-outline-end.sc-ion-input-md {
  border-width: 0px !important;
}
</style>

<template>
  <ion-page data-page="Exercises">
    <div id="header-wrapper">
      <div class="perform-page">
        <h1 style="margin-top: 0px">Exercices ({{ countExercices }})</h1>
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
              padding: 20px 20px 20px 20px;
              display: flex;
              align-items: center;
              justify-content: space-between;
              flex-wrap: wrap;
height: 85%;
    overflow: scroll;
            ">
            <div style="
                  width: 100%;
                  display: flex;
                  align-items: center;
                  justify-content: space-between;
                ">
              <h3>
                FILTRER
              </h3>
              <ion-icon style="color: red; border: 1px solid red; border-radius: 5px" @click="dismiss" :icon="close" />
            </div>
            <div class="input-div">
              <h4>Sports :</h4>
              <h6>Sélectionnez les sports à filtrer</h6>
              <ion-list>
                <ion-item>
                  <ion-select @ionChange="updateSelectedSports" class="custom-ion-select" :value="sports_selected"
                    aria-label="Sports" placeholder="Selectionner vos sports" :multiple="true"
                    :compareWith="compareWith">
                    <ion-select-option v-for="sport in sports" :value="{ sport: { id: sport.id, name: '' } }"
                      :key="sport.id" aria-selected="true">{{ sport.name }}</ion-select-option>
                  </ion-select>
                </ion-item>
              </ion-list>
            </div>
            <div class="input-div">
              <h4>Matériels :</h4>
              <h6>Sélectionnez les matériels à filtrer</h6>
              <v-row style="display: flex; flex-wrap: wrap; justify-content: center" dense>
                <v-col style="width: 30%; flex: none" v-for="material in materials" :key="material.id" cols="12" sm="4">
                  <v-card @click="addMaterialFilter(material.id)">
                    <v-img :src="material.pictures ? material.pictures.replace('http', 'https') : ''" class="align-end"
                      :gradient="findMaterial(material)
                        ? 'to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)'
                        : 'to bottom, rgba(0,0,0,.05), rgba(0,0,0,.1'
                        " height="80px" cover aspect-ratio="1">
                      <v-icon :icon="findMaterial(material) ? 'mdi-check' : ''"></v-icon>
                    </v-img>
                    <v-card-title style="
                        font-size: 12px;
                        height: 40px;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        white-space: normal !important;
                        padding: 5px;
                        text-align: center;
                      " class="textTitleCard">{{ material.name }}</v-card-title>
                  </v-card>
                </v-col>
              </v-row>
            </div>
            <div class="input-div" style="flex-wrap: wrap; justify-content: flex-start">
              <h4>Muscles :</h4>
              <h6>Sélectionnez les zones à cibler</h6>
              <div style=" display: flex; width: 100%; margin-top: 16px; justify-content: space-between; align-items:
              center; ">
                <BodyComponent :height="'300'" :width="'300'" :viewOnly="'edit'" :muscleSelected="muscle_selected"
                  :setMuscleSelected="setMuscleSelectedView" />
              </div>
            </div>
          </div>
          <div class="input-div"
            style="position:fixed; margin-top: 20px; margin-bottom: 20px; justify-content: center; display: flex">
            <ion-button @click="filterExercice"> Filtrer </ion-button>
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
            <ion-list lines="none" class="parent-list" :inset="true">
              <ion-item class="list-item" v-for="exercise in exercises" :key="exercise.id" @click="goPage(exercise.id)">
                <div v-if="exercise.thumbnail == null" class="exercice-img">
                  <ion-label>{{ exercise.name[0] }}</ion-label>
                </div>
                <div v-else class="exercice-thumbnail">
                  <img :src="exercise.thumbnail" alt="Miniature de l'exercice" />
                </div>
                <ion-label class="exercice_label">{{
                  exercise.name
                }}</ion-label>
                <ion-icon :icon="chevronForwardOutline"></ion-icon>
              </ion-item>
            </ion-list>
            <ion-infinite-scroll @ionInfinite="ionInfinite">
              <ion-infinite-scroll-content></ion-infinite-scroll-content>
            </ion-infinite-scroll>
          </v-tabs-window-item>

          <v-tabs-window-item value="two">
            <ion-list class="list-item" :inset="true" v-for="exercise in exercises_fav" :key="exercises.id"
              @click="goPage(exercise.fav_exercise.id)">
              <ion-item>
                <div class="exercice-img">
                  <ion-label>{{ exercise.fav_exercise.name[0] }}</ion-label>
                </div>
                <ion-label l class="exercice_label">{{
                  exercise.fav_exercise.name
                }}</ion-label>
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
  IonInfiniteScroll,
  IonInfiniteScrollContent,
  IonModal,
  InfiniteScrollCustomEvent,
  onIonViewWillEnter
} from "@ionic/vue";
import { get } from "../../lib/callApi";
import { reactive, ref } from "vue";
import { chevronForwardOutline, close } from "ionicons/icons";
import "./index.css";
import { useRoute, useRouter } from "vue-router";
import { store } from "../../store/store";
import { Muscle, Sport, Material, MaterialArray, SportArray } from "../../types/allTypes";
//@ts-expect-error
import { BodyComponent } from "perform-body-component-lib";
import IERequestOptions from "../../types/request";

const router = useRouter();

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
const filterModal = ref(null) as any;
const searchValue = ref("");
const orderBy = ref({ id: "default", value: "Par défaut" });
const exercises: any = ref([]);
const exercises_fav: any = reactive([]);
const sports = ref([] as Sport[]);
const sports_selected = ref([] as SportArray[]);
const navRoute = useRoute();
const muscles = ref([] as Muscle[]);
const muscle_selected = ref([] as Muscle[]);
const materials = ref([] as Material[]);
const materials_selected = ref([] as MaterialArray[]);
const page = ref(0);
const countExercices = ref(0);
const pageMax = ref(1);

const findMaterial = (material: any) => {
  let findMaterial = false;
  materials_selected.value.map((elem) => {
    if (Number(elem.material.id) === material.id) {
      findMaterial = true;
    }
  });
  return findMaterial;
};

const generateItems = async (type: string) => {
  if (type === "refresh") {
    exercises.value = [];
    page.value = 1;
  } else {
    page.value = page.value + 1;
  }
  getExercises().then((res) => {
    console.log('res ', res)
    if (res && res !== exercises.value) {
      for (const element of res) {
        exercises.value.push(element)
        console.log('exercises ', exercises.value)
      };
    }
  });
}
const ionInfinite = (ev: InfiniteScrollCustomEvent) => {
  if (page.value < pageMax.value) {
    generateItems('');
  }
  setTimeout(() => ev.target.complete(), 500);
};


const compareWith = (o1: any, o2: any) => {
  console.log(o1, ' ', o2)
  return o1 && o2 ? o1.sport.id === o2.sport.id : o1 === o2;
};

const goPage = (id: any) => {
  router.push('/exercises/' + id);
};

const dismiss = () => {
  filterModal.value.$el.dismiss();
};

const setMuscleSelectedView = (key: string, action: string) => {
  if (action === "add") {
    const findKey =
      muscle_selected.value.filter(function (element: Muscle) {
        return element.zone.code === key;
      }).length == 0;
    if (findKey) {
      muscle_selected.value.push({ zone: { name: "", code: key } });
    }
  } else {
    let index = muscle_selected.value.indexOf(key as any);
    muscle_selected.value.map((muscle) => {
      if (muscle.zone.code === key) {
        index = muscle_selected.value.indexOf(muscle);
      }
      if (index !== -1) {
        muscle_selected.value.splice(index, 1);
      }
    });
  }
};

const addMaterialFilter = (id: any) => {
  const findKey =
    materials_selected.value.filter(function (element: any) {
      return Number(element.material.id) === id;
    }).length == 0;
  if (findKey) {
    materials_selected.value.push({ material: { id: id, pictures: "", name: '' } });
  } else {
    materials_selected.value.map((elem, index) => {
      if (elem.material.id == id) {
        materials_selected.value.splice(index, 1);

      }
    })
  }
};

const handleOrderChange = (event: any) => {
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
  generateItems('refresh');
};

const jointByComa = (
  arrayPass: string[] | SportArray[] | Muscle[] | MaterialArray[],
  name: string = ""
) => {
  let stringWithCommas = "";
  for (let i = 0; i < arrayPass.length; i++) {
    if (name == "sport") {
      let array = arrayPass as SportArray[];
      stringWithCommas += String(array[i].sport.id);
    } else if (name == "muscle") {
      let array = arrayPass as Muscle[];
      stringWithCommas += String(array[i].zone.code);
    } else if (name == "material") {
      let array = arrayPass as MaterialArray[];
      stringWithCommas += array[i].material.id;
    }
    if (i < arrayPass.length - 1) {
      stringWithCommas += ",";
    }
  }
  return stringWithCommas;
};

const filterExercice = () => {
  const option = {} as any;
  if (materials_selected.value.length > 0) {
    option.material_id = jointByComa(materials_selected.value, "material");
  } else {
    option.material_id = "";
  }
  if (muscle_selected.value.length > 0) {
    option.workzone_code = jointByComa(muscle_selected.value, "muscle");
  } else {
    option.workzone_code = "";
  }
  if (sports_selected.value.length > 0) {
    option.sport_id = jointByComa(sports_selected.value, "sport");
    console.log('option sport ', option.sport_id)
  } else {
    option.sport_id = "";
  }
  router
    .replace({
      path: navRoute.path,
      query: Object.assign({}, navRoute.query, option),
    })
    .then(() => {
      generateItems('refresh');

      if (filterModal.value) filterModal.value.$el.dismiss();
    });
};

const getExercises = async () => {
  console.log('get Exercises page :', page.value, ' pageMax ', pageMax.value)
  if (page.value <= pageMax.value) {
    const option = {
      body: {},
    } as IERequestOptions;
    if (orderBy.value) {
      option.orderBy = orderBy.value;
    }
    if (searchValue.value !== "") {
      option.search = searchValue.value;
    }

    const wk_zone = navRoute.query.workzone_code;
    const mat_id = navRoute.query.material_id;
    const sport_id = navRoute.query.sport_id;
    if (mat_id && mat_id != "") {
      option.material_id = String(mat_id);
    }

    if (sport_id && sport_id != "") {
      option.sport_id = String(sport_id);
    }

    if (wk_zone && wk_zone != "") {
      option.workzone_code = String(wk_zone);
    }

    const res = await get("/exercises/?page=" + page.value, option);
    countExercices.value = await res.count
    pageMax.value = Math.ceil(res.count / 10);
    return res.results;
  } else {
    return {}
  }

};

const showFilter = () => {
  const work_zone = navRoute.query.workzone_code as string;
  const mucsle_temp = work_zone ? work_zone.split(",") : [];
  muscle_selected.value = mucsle_temp.map((muscle) => {
    return { zone: { name: "", code: muscle } };
  });
  const mat_id = navRoute.query.material_id as string;
  const mat_temp = mat_id ? mat_id.split(",") : [];
  materials_selected.value = mat_temp.map((materialElem) => {
    return { material: { id: materialElem, pictures: '', name: '' } };
  });
  const sport_id = navRoute.query.sport_id as string;
  const sport_temp = sport_id ? sport_id.split(",") : [];
  sports_selected.value = sport_temp.map((sport) => {
    return { sport: { name: "", id: Number(sport) } };
  });

  setTimeout(() => {
    const ionSelect = document.querySelectorAll(".custom-ion-select");
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
  }, 100);
  filterModal.value.$el.present();
};

const updateSelectedSports = (change: any) => {
  sports_selected.value = change.detail.value;
};

const handleSearchInput = async (event: any) => {
  console.log('handle search')
  searchValue.value = event.target.value;
  generateItems('refresh');
};

onIonViewWillEnter(async () => {
  store.get("user").then((res) => {
    user_id.value = JSON.parse(res).user.id;
    get(
      "/userfavexercises/user/" + user_id.value + "/",
      { body: {} },
      true
    ).then((res: any) => {
      if (res.status > 300) {
        console.log("error ", res.status);
      } else {
        exercises_fav.value = res;
      }
    });
  });

  generateItems('refresh');


  get("/sports/all", { body: {} }, false).then((res: any) => {
    if (res.status > 300) {
      console.log("error ", res.status);
    } else {
      sports.value = res;
    }
  });

  get("/materials/all", { body: {} }, false).then((res: any) => {
    if (res.status > 300) {
      console.log("error ", res.status);
    } else {
      materials.value = res;
    }
  });

  get("/workzones/all", { body: {} }, false).then((res: any) => {
    if (res.status > 300) {
      console.log("error ", res.status);
    } else {
      muscles.value = res;
    }
  });
});
</script>
