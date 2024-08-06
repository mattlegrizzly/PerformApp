<style scoped>
ion-modal {
  --height: 90%;
  --width: 90%;
  --border-radius: 16px;
  --box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
}

.filter-ion-chip {
  margin-bottom: 10px;
  min-height: 0px !important;
  pointer-events: auto; /* Pour que les chip restent cliquables */
  margin-right: 5px;
  height: 20px;
  font-size: 10px !important;
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
        <div v-if="searchValue === ''">
          <h1 v-if="tab == 'one'" style="margin-top: 0px">
            Exercices ({{ countExercices }})
          </h1>
          <h1 v-else style="margin-top: 0px">
            Exercices favoris ({{ countExercicesFav }})
          </h1>
        </div>
        <div v-else>
          <h1 v-if="tab == 'one'" style="margin-top: 0px">
            Résultats de la recherche pour : {{ searchValue }} ({{
              countExercices
            }})
          </h1>
        </div>
        <ion-label>Rechercher un exercice :</ion-label>
        <ion-input
          id="search-input"
          fill="outline"
          slot="end"
          placeholder="Cherchez un exercice"
          shape="round"
          @ionInput="handleSearchInput($event)"
        ></ion-input>
        <div class="filter-div">
          <ion-button @click="showFilter">Filtres</ion-button>
          <ion-list class="filter-item">
            <ion-item>
              <ion-select
                aria-label="Trier par"
                interface="popover"
                placeholder="Trier par"
                @ionChange="handleOrderChange($event)"
              >
                <ion-select-option
                  v-for="elem in order"
                  :key="elem.id"
                  :value="elem.id"
                  >{{ elem.value }}</ion-select-option
                >
              </ion-select>
            </ion-item>
          </ion-list>
        </div>
        <div class="displayFilter" v-if="isFilter()">
          <p>Filtres actifs :</p>
          <div
            class="displayFilterContainer"
            :class="showFilterResume ? 'showFullDisplayContainer' : ''"
          >
            <div class="displayFilterChipContainer" ref="chipFilterContainer">
              <ion-chip
                v-for="muscle of muscle_selected"
                class="filter-ion-chip"
                color="primary"
              >
                <ion-icon
                  :icon="close"
                  @click="
                    (event) => {
                      addMaterialFilter(
                        muscle.zone.code,
                        muscle_selected,
                        muscles,
                        'remove'
                      ).then(() => {
                        filterExercice();
                      });
                    }
                  "
                ></ion-icon>
                <ion-label>{{ muscle.zone.name }}</ion-label>
              </ion-chip>

              <ion-chip
                v-for="sport of sports_selected"
                :key="sport.sport.id"
                class="filter-ion-chip"
                color="primary"
              >
                <ion-icon
                  :icon="close"
                  @click="
                    (event) => {
                      event.stopPropagation();
                      addMaterialFilter(
                        sport.sport.id,
                        sports_selected,
                        sports,
                        'remove'

                      );
                      filterExercice();
                    }
                  "
                ></ion-icon>
                <ion-label>{{ sport.sport.name }}</ion-label>
              </ion-chip>

              <ion-chip
                v-for="material of materials_selected"
                :key="material.material.id"
                class="filter-ion-chip"
                color="primary"
              >
                <ion-icon
                  :icon="close"
                  @click="
                    (event) => {
                      event.stopPropagation();
                      addMaterialFilter(
                        material.material.id,
                        materials_selected,
                        materials,
                        'remove'

                      );
                      filterExercice();
                    }
                  "
                ></ion-icon>
                <ion-label>{{ material.material.name }}</ion-label>
              </ion-chip>
            </div>

            <ion-icon
              @click="resumeFilter"
              v-if="showIconResume"
              :icon="showFilterResume ? chevronUpOutline : chevronDownOutline"
            />
          </div>
        </div>
      </div>
      <ion-modal class="static-modal" ref="filterModal">
        <ion-content>
          <div
            style="
              padding: 20px 20px 20px 20px;
              display: flex;
              align-items: center;
              justify-content: space-between;
              flex-wrap: wrap;
              height: 83%;
              overflow: scroll;
            "
          >
            <div
              style="
                width: 100%;
                display: flex;
                align-items: center;
                justify-content: space-between;
              "
            >
              <h3 style="display: flex; align-items: center">
                FILTRER
                <ion-icon
                  style="margin-left: 10px"
                  @click="resetFilter"
                  v-if="isFilter()"
                  :icon="trashBinSharp"
                ></ion-icon>
              </h3>
              <ion-icon
                style="color: red; border: 1px solid red; border-radius: 5px"
                @click="dismiss"
                :icon="close"
              />
            </div>
            <div class="input-div">
              <h4>Sports :</h4>
              <h6>Sélectionnez les sports à filtrer</h6>
              <ion-list>
                <ion-item>
                  <ion-select
                    @ionChange="updateSelectedSports"
                    class="custom-ion-select"
                    :value="sports_selected"
                    aria-label="Sports"
                    placeholder="Selectionner vos sports"
                    :multiple="true"
                    :compareWith="compareWith"
                  >
                    <ion-select-option
                      v-for="sport in sports"
                      :value="{ sport: { id: sport.id, name: sport.name } }"
                      :key="sport.id"
                      aria-selected="true"
                      >{{ sport.name }}</ion-select-option
                    >
                  </ion-select>
                </ion-item>
              </ion-list>
            </div>
            <div class="input-div">
              <h4>Matériels :</h4>
              <h6>Sélectionnez les matériels à filtrer</h6>
              <v-row
                style="display: flex; flex-wrap: wrap; justify-content: center"
                dense
              >
                <v-col
                  style="width: 30%; flex: none"
                  v-for="material in materials"
                  :key="material.id"
                  cols="12"
                  sm="4"
                >
                  <v-card
                    @click="
                      addMaterialFilter(
                        material.id,
                        materials_selected,
                        materials
                      )
                    "
                    :style="
                      findMaterial(material)
                        ? 'box-shadow:inset 0px 0px 0px 2px var(--primary-blue)'
                        : ''
                    "
                  >
                    <v-img
                      :src="
                        material.pictures
                          ? material.pictures.replace('http', 'https')
                          : ''
                      "
                      class="align-end"
                      gradient="to bottom, rgba(0,0,0,.05), rgba(0,0,0,.1)
                      "
                      height="80px"
                      cover
                      aspect-ratio="1"
                    >
                      <v-icon
                        :icon="findMaterial(material) ? 'mdi-check' : ''"
                      ></v-icon>
                    </v-img>
                    <v-card-title
                      style="
                        font-size: 12px;
                        height: 40px;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        white-space: normal !important;
                        padding: 5px;
                        text-align: center;
                      "
                      class="textTitleCard"
                      >{{ material.name }}</v-card-title
                    >
                  </v-card>
                </v-col>
              </v-row>
            </div>
            <div
              class="input-div"
              style="flex-wrap: wrap; justify-content: flex-start"
            >
              <h4>Muscles :</h4>
              <h6>Sélectionnez les zones à cibler</h6>
              <div
                style="
                  display: flex;
                  width: 100%;
                  margin-top: 16px;
                  justify-content: space-between;
                  align-items: center;
                "
              >
                <BodyComponent
                  :height="'300'"
                  :width="'300'"
                  :viewOnly="'edit'"
                  :muscleSelected="muscle_selected"
                  :setMuscleSelected="setMuscleSelectedView"
                />
              </div>
            </div>
          </div>
          <div
            class="input-div"
            style="
              position: fixed;
              margin-top: 10px;
              margin-bottom: 10px;
              justify-content: space-around;
              display: flex;
            "
          >
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
              <ion-item
                class="list-item"
                v-for="exercise in exercises"
                :key="exercise.id"
                @click="goPage(exercise.id)"
              >
                <div v-if="exercise.thumbnail == null" class="exercice-img">
                  <ion-label>{{ exercise.name[0] }}</ion-label>
                </div>
                <div v-else class="exercice-thumbnail">
                  <img
                    :src="exercise.thumbnail.replace('http', 'https')"
                    alt="Miniature de l'exercice"
                  />
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
            <ion-list lines="none" class="parent-list" :inset="true">
              <ion-item
                class="list-item"
                v-for="exercise in exercises_fav"
                :key="exercise.id"
                @click="goPage(exercise.id)"
              >
                <div v-if="exercise.thumbnail == null" class="exercice-img">
                  <ion-label>{{ exercise.name[0] }}</ion-label>
                </div>
                <div v-else class="exercice-thumbnail">
                  <img
                    :src="getThumbnail(exercise.thumbnail)"
                    alt="Miniature de l'exercice"
                  />
                </div>
                <ion-label class="exercice_label">{{
                  exercise.name
                }}</ion-label>
                <ion-icon :icon="chevronForwardOutline"></ion-icon>
              </ion-item>
            </ion-list>
            <ion-infinite-scroll @ionInfinite="ionInfiniteFavorite">
              <ion-infinite-scroll-content></ion-infinite-scroll-content>
            </ion-infinite-scroll>
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
  onIonViewWillEnter,
  IonChip,
} from "@ionic/vue";
import { get } from "../../lib/callApi";
import { ref, watch } from "vue";
import {
  chevronForwardOutline,
  close,
  trashBinSharp,
  chevronDownOutline,
  chevronUpOutline,
} from "ionicons/icons";
import "./index.css";
import { useRoute, useRouter } from "vue-router";
import { store } from "../../store/store";
import {
  Muscle,
  Sport,
  Material,
  MaterialArray,
  SportArray,
} from "../../types/allTypes";

//@ts-expect-error
import { BodyComponent } from "perform-body-component-lib";
import IERequestOptions from "../../types/request";
import { useErrorHandler } from "../../lib/useErrorHandler";

const { triggerError } = useErrorHandler() as any;

const router = useRouter();

const order = [
  { id: "orderByNameAsc", value: "Nom (Croissant)" },
  { id: "orderByNameDesc", value: "Nom (Décroissant)" },
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
const exercises_fav: any = ref([]);
const sports = ref([] as Sport[]);
const sports_selected = ref([] as SportArray[]);
const navRoute = useRoute();
const muscles = ref([] as Muscle[]);
const muscle_selected = ref([] as Muscle[]);
const materials = ref([] as Material[]);
const materials_selected = ref([] as MaterialArray[]);
const page = ref(0);
const pageFav = ref(0);
const countExercices = ref(0);
const countExercicesFav = ref(0);
const pageMax = ref(1);
const pageMaxFav = ref(1);
const chipFilterContainer = ref<HTMLElement | null>(null) as any;

const showFilterResume = ref(false);
const showIconResume = ref(false);

const isFilter = () => {
  return (
    muscle_selected.value.length > 0 ||
    materials_selected.value.length > 0 ||
    sports_selected.value.length > 0
  );
};

const resetFilter = () => {
  muscle_selected.value = [];
  materials_selected.value = [];
  sports_selected.value = [];
  filterExercice();
};

const getThumbnail = (path: string) => {
  return import.meta.env.VITE_API_URL + path;
};

const resumeFilter = () => {
  showFilterResume.value = !showFilterResume.value;
};

watch(
  () =>
    muscle_selected.value.length |
    materials_selected.value.length |
    sports_selected.value.length,
  () => {
    setTimeout(() => {
      if (
        chipFilterContainer &&
        chipFilterContainer.value.clientHeight &&
        chipFilterContainer.value.clientHeight > 43
      ) {
        showIconResume.value = true;
      } else {
        showIconResume.value = false;
      }
    }, 100);
  }
);

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
    getExercises("").then((res) => {
      exercises.value = res;
    });
  } else {
    page.value = page.value + 1;
    getExercises("").then((res) => {
      for (const elem of res) {
        exercises.value.push(elem);
      }
    });
  }
};

const generateItemsFav = async (type: string) => {
  if (type === "refresh") {
    exercises_fav.value = [];
    pageFav.value = 1;
    getExercises("favorite").then((res) => {
      exercises_fav.value = res;
    });
  } else {
    pageFav.value = pageFav.value + 1;
    getExercises("favorite").then((res) => {
      for (const elem of res) {
        exercises_fav.value.push(elem);
      }
    });
  }
};

const ionInfiniteFavorite = (ev: InfiniteScrollCustomEvent) => {
  if (pageFav.value < pageMaxFav.value) {
    generateItemsFav("");
  }
  setTimeout(() => ev.target.complete(), 500);
};

const ionInfinite = (ev: InfiniteScrollCustomEvent) => {
  if (page.value < pageMax.value) {
    generateItems("");
  }
  setTimeout(() => ev.target.complete(), 500);
};

const compareWith = (o1: any, o2: any) => {
  return o1 && o2 ? o1.sport.id === o2.sport.id : o1 === o2;
};

const goPage = (id: any) => {
  router.push("/exercises/" + id);
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
      const muscleFind = muscles.value.find((el: any) => el.code == key) as any;
      muscle_selected.value.push({
        zone: { name: muscleFind.name, code: muscleFind.code },
      });
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

const addMaterialFilter = async (id: any, array: any, constArray: any, remove : string = 'add') => {
  
  const findKey =
    array.filter(function (element: any) {
      if (element.zone) {
        return Number(element.zone.code) === id;
      } else if (element.material) {
        return Number(element.material.code) === id;
      } else if (element.sport) {
        return Number(element.sport.code) === id;
      } else {
      }
      return Number(element.material.id) === id;
    }).length == 0;
  if (findKey && remove == "add") {
    const materialFind = constArray.find((el) => el.id == id) as any;
    array.push({ material: materialFind });
  } else {
    array.map((elem, index) => {
      if (elem.zone) {
        if (elem.zone.code == id) {
          array.splice(index, 1);
        }
      } else if (elem.material) {
        if (elem.material.id == id) {
          array.splice(index, 1);
        }
      } else if (elem.sport) {
        if (elem.sport.id == id) {
          array.splice(index, 1);
        }
      } else {
      }
    });
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
  setTimeout(() => {
    generateItems("refresh");
  }, 500);
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
  } else {
    option.sport_id = "";
  }
  router
    .replace({
      path: navRoute.path,
      query: Object.assign({}, navRoute.query, option),
    })
    .then(() => {
      generateItems("refresh");

      if (filterModal.value) filterModal.value.$el.dismiss();
    });
};

const getExercises = async (type: string) => {
  pageMax.value = pageMax.value || 1;
  pageMaxFav.value = pageMaxFav.value || 1;

  const isFavorite = type === "favorite";
  const pageTemp = isFavorite ? pageFav.value : page.value;
  const pageMaxTemp = isFavorite ? pageMaxFav.value : pageMax.value;

  if (pageTemp > pageMaxTemp) {
    return {};
  }

  const option = {} as IERequestOptions;
  if (orderBy.value) {
    option.orderBy = orderBy.value;
  }
  if (searchValue.value) {
    option.search = searchValue.value;
  }

  const { workzone_code, material_id, sport_id } = navRoute.query;

  if (material_id) {
    option.material_id = String(material_id);
  }
  if (sport_id) {
    option.sport_id = String(sport_id);
  }
  if (workzone_code) {
    option.workzone_code = String(workzone_code);
  }

  if (isFavorite) {
    const res = await get(`/userfavexercises/user/${user_id.value}/`, option);
    if (res.status !== undefined && res.status > 301) {
      triggerError("Erreur lors de la récupération des exercices favoris");
    }
    const favs = res.map((exo: any) => exo.fav_exercise);
    countExercicesFav.value = favs.length;
    pageMaxFav.value = Math.ceil(favs.length / 10);
    return favs;
  } else {
    const res = await get(`/exercises/?page=${pageTemp}`, option);
    if (res.status > 301) {
      triggerError("Erreur lors de la récupération des exercices");
    }
    countExercices.value = res.count;
    pageMax.value = Math.ceil(res.count / 10);
    return res.results;
  }
};

const getFilter = () => {
  const work_zone = navRoute.query.workzone_code as string;
  const mucsle_temp = work_zone ? work_zone.split(",") : [];
  muscle_selected.value = mucsle_temp.map((muscle) => {
    const muscleFind = muscles.value.find(
      (el: any) => el.code == muscle
    ) as any;
    return { zone: { name: muscleFind.name, code: muscleFind.code } };
  });
  const mat_id = navRoute.query.material_id as string;
  const mat_temp = mat_id ? mat_id.split(",") : [];
  materials_selected.value = mat_temp.map((materialElem) => {
    const materialFind = materials.value.find(
      (el: any) => el.id == materialElem
    ) as any;
    return {
      material: { id: materialFind.id, pictures: "", name: materialFind.name },
    };
  });
  const sport_id = navRoute.query.sport_id as string;
  const sport_temp = sport_id ? sport_id.split(",") : [];
  sports_selected.value = sport_temp.map((sport) => {
    const sportFind = sports.value.find((el: any) => el.id == sport) as any;
    return { sport: { name: sportFind.name, id: Number(sportFind.id) } };
  });
};
const showFilter = () => {
  getFilter();
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
  searchValue.value = event.target.value;
  generateItems("refresh");
};

onIonViewWillEnter(async () => {
  muscle_selected.value = [];
  store.get("user").then((res) => {
    user_id.value = JSON.parse(res).user.id;
    generateItemsFav("refresh");
  });

  generateItems("refresh");

  get("/sports/all", { body: {} }, false).then((res: any) => {
    if (res.status > 300) {
      triggerError("Erreur lors de la récupération des sports");
    } else {
      sports.value = res;

      get("/materials/all", { body: {} }, false).then((res: any) => {
        if (res.status > 300) {
          triggerError("Erreur lors de la récupération des matériels");
        } else {
          materials.value = res;
          get("/workzones/all", { body: {} }, false).then((res: any) => {
            if (res.status > 300) {
              triggerError("Erreur lors de la récupération des muscles");
            } else {
              muscles.value = res;
              getFilter();
            }
          });
        }
      });
    }
  });
});
</script>
