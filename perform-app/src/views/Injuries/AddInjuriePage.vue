<template>
  <ion-page data-page="add-injuries">
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton url="profile" text="Retour" back="back" />
          
        </div>
        <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
          Ajouter une blessure
        </h1>
        <div class="input_injurie">
          <ion-label :class="errorAdd && nameInjury == '' ? 'required_text' : ''">Nom de la blessure *</ion-label>
          <ion-input label-placement="stacked" :class="errorAdd  && nameInjury == '' ? 'required_class' : ''" fill="outline" @ion-input="handleInput('name', $event.detail.value)"
            placeholder="Déchirure du quadriceps" :value="nameInjury"></ion-input>
        </div>
        <div class="input_injurie">
          <ion-label>Description de la blessure</ion-label>

          <ion-textarea variant="outlined" color="danger"  placeholder="Décrivez votre blessure"
            @ion-change="handleInput('description', $event.detail.value)">
          </ion-textarea>
        </div>

        <div class="input_injurie">
          <ion-label :class="errorAdd && muscleSelected[0].zone.code == '' ? 'required_text' : ''">Zone de la blessure *</ion-label>

          <ion-list class="filter-item"  :class="errorAdd  && muscleSelected[0].zone.code == '' ? 'required_class' : ''">
            <ion-item>
              <ion-select interface="popover" placeholder="Zone de la blessure" class="custom-ion-select"
                :toggle-icon="chevronDownOutline" justify="space-between" @click="setIonSize()"
                @ion-change="handleInput('zone', $event.detail.value)" :value="muscleSelected[0].zone.code">
                <ion-select-option v-for="elem in muscles" :key="elem.code" :value="elem.code">{{
                  elem.name }}</ion-select-option>
              </ion-select>
            </ion-item>
          </ion-list>
        </div>
        <div class="input_injurie">
          <ion-label :class="errorAdd && date == '' ? 'required_text' : ''">Date de la blessure *</ion-label>
          <ion-input :class="errorAdd  && date == '' ? 'required_class' : ''" type="date" label-placement="stacked" fill="outline" placeholder="2021-09-01"
            @ion-change="handleInput('date', $event.detail.value)"></ion-input>
        </div>
        <div class="input_injurie">
          <ion-label :class="errorAdd && state == '' ? 'required_text' : ''">Etat de la blessure *</ion-label>
          <ion-list :class="errorAdd && state == '' ? 'required_class' : ''" class="filter-item">
            <ion-item>
              <ion-select interface="popover" placeholder="Etat de la blessure" class="custom-ion-select"
                :toggle-icon="chevronDownOutline" justify="space-between" @click="setIonSize()"
                @ion-change="handleInput('state', $event.detail.value)">
                <ion-select-option v-for="elem in injuries_state" :key="elem.code" :value="elem.code">{{ elem.name
                  }}</ion-select-option>
              </ion-select>
            </ion-item>
          </ion-list>
        </div>
        <div style="
            display: flex;
            width: 100%;
            margin-top: 16px;
            justify-content: center;
            align-items: center;
          ">
          <BodyComponent :setMuscleSelected="setMuscle" :muscleSelected="muscleSelected" :height="'300'" :width="'200'"
            :viewOnly="'edit'" :isInjury="true"/>

        </div>
        <div>
          <NavButton style="width: 100%; height: 40px; margin-top: 20px;" @click="addInjurie" :disabled="adding" :text="adding ? 'Ajout en cours': 'Ajouter la blessure'" :noIcon="true" />
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonContent,
  IonPage,
  IonList,
  IonItem,
  IonSelect,
  IonSelectOption,
  IonInput,
  IonTextarea,
  onIonViewWillEnter,
  IonLabel
} from "@ionic/vue";
import "@/assets/base.css";
import "@/assets/main.css";
import { chevronDownOutline } from "ionicons/icons";
import NavButton from "../../components/NavButton/NavButton.vue";
import { ref, watch } from "vue";
import { get, post } from "../../lib/callApi";
import type { Muscles } from "../../types/allTypes";
import "../Profile/index.css";
//@ts-expect-error
import { BodyComponent } from 'perform-body-component-lib'
import { store } from "../../store/store";
import router from "../../router";

import { useErrorHandler } from '../../lib/useErrorHandler';

const errorAdd = ref(false); 

const { triggerError } = useErrorHandler() as any;

const nameInjury = ref("");
const description = ref("");
const date = ref("");
const state = ref("");
const muscleSelected = ref([{
  zone: {
    name: "",
    code: ""
  }
}]);
const muscles = ref([] as Muscles[]);
const user = ref({} as any);

const adding = ref(false);

const injuries_state = ref([
  {
    code: "TR",
    name: "Soignée",
  },
  {
    code: "NT",
    name: "Pas soignée",
  },
  {
    code: "IP",
    name: "En cours",
  },
]);

watch(nameInjury, () => {
  if(nameInjury.value.length > 0) {
    nameInjury.value = nameInjury.value[0].toUpperCase() + nameInjury.value.slice(1)
  }
})

/**
 * Handle input changes and update relevant reactive variables.
 * @param {string} name - The name of the input.
 * @param {string | undefined | null} valuePass - The value passed from the input.
 */
const handleInput = (name: string, valuePass: string | undefined | null) => {
  console.log('oui')
  let value = valuePass as string;
  switch (name) {
    case "name":
      nameInjury.value = value[0].toUpperCase() + value.slice(1);
      break;
    case "description":
      description.value = value;
      break;
    case "zone":
      muscleSelected.value =
        [{
          zone: {
            code: value,
            name: ''
          }
        }]

      break;
    case "date":
      date.value = value;
      break;
    case "state":
      state.value = value;
      break;
    case undefined:
      state.value = "";
  }
};


const setMuscle = (code: string) => {
  console.log('code ', code)
  console.log(muscles)
  const muscleToSet = muscles.value.find((element: any) => element.code == code) as any
  console.log(muscleToSet)
  muscleSelected.value = [{
    zone: {
      code: muscleToSet.code,
      name: muscleToSet?.name
    }
  }];
}

/**
 * Ajuste la taille et le style des éléments ion-popover.
 */
const setIonSize = () => {
  const popover = document.querySelectorAll("ion-popover");
  if (popover === null) return;
  for (const elem of popover) {
    const shadowRoot = elem.shadowRoot;
    if (shadowRoot === null) return;
    const style = document.createElement("style");
    style.textContent = `
      .popover-content {
            margin-left: 9px;
            margin-top: 20px;
      }

    `;
    shadowRoot.appendChild(style);
    const stylePopover = document.createElement("style");
    stylePopover.textContent = `
      .sc-ion-select-popover-md-h {
            left : 10px;
            width: calc(100vw - 40px);
      }

    `;
    elem.appendChild(stylePopover);
  }
}

/**
 * Ajoute une nouvelle blessure en envoyant une requête POST au serveur.
 */
const addInjurie = () => {
  adding.value = true;
  post(
    "/injuries/",
    {
      body: {
        name: nameInjury.value,
        description: description.value,
        zone: muscleSelected.value[0].zone.code,
        date: date.value,
        state: state.value,
        user: user.value.id,
      },
    },
    true
  ).then((res) => {
    if (res.status > 300) {
      triggerError('Erreur lors de la création de la blessure');
      errorAdd.value = true;
      adding.value = false;
    } else {
      errorAdd.value = false;
      router.push("/view_injuries/" + res.id + "/?edit=true")

    }
  });
};

/**
 * Hook pour exécuter du code lorsque l'IonView est sur le point d'entrer et de devenir actif.
 */
onIonViewWillEnter(async () => {
  adding.value = false;
  let storeUser = await store.get("user");
  if (storeUser !== "") {
    user.value = JSON.parse(storeUser).user;
  }
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
  get("/workzones/all_injury", { body: {} }, false).then((res) => {
    if (res.status > 301) {
      triggerError('Erreur lors de la récupération des muscles');
    } else {
      muscles.value = res;
    }
  });
});
</script>
