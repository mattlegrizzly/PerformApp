<template>
  <ion-page data-page="edit-injuries">
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton url="profile" text="Retour" back="back" />
        </div>
        <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
          Modifier une blessure
        </h1>
        <div class="input_injurie">
          <ion-label
            :class="errorAdd && injury.name == '' ? 'required_text' : ''"
            >Nom de la blessure *</ion-label
          >
          <ion-input
            :class="errorAdd && injury.name == '' ? 'required_class' : ''"
            label-placement="stacked"
            fill="outline"
            :value="injury.name"
            @ion-change="handleInput('name', $event.detail.value)"
            placeholder="Déchirure du quadriceps"
          ></ion-input>
        </div>
        <div class="input_injurie">
          <ion-label>Description de la blessure</ion-label>

          <ion-textarea
            :value="injury.description"
            variant="outlined"
            placeholder="Décrivez votre blessure"
            @ion-change="handleInput('description', $event.detail.value)"
          >
          </ion-textarea>
        </div>

        <div class="input_injurie">
          <ion-label
            :class="errorAdd && injury.zone.code == '' ? 'required_text' : ''"
            >Zone de la blessure</ion-label
          >

          <ion-list
            :class="errorAdd && injury.zone.code == '' ? 'required_class' : ''"
            class="filter-item"
          >
            <ion-item>
              <ion-select
                interface="popover"
                placeholder="Zone de la blessure"
                class="custom-ion-select"
                :toggle-icon="chevronDownOutline"
                justify="space-between"
                :value="injury.zone[0].zone.code"
                @click="setIonSize()"
                @ion-change="handleInput('zone', $event.detail.value)"
              >
                <ion-select-option
                  v-for="elem in muscles"
                  :key="elem.code"
                  :value="elem.code"
                  >{{ elem.name }}</ion-select-option
                >
              </ion-select>
            </ion-item>
          </ion-list>
        </div>
        <div class="input_injurie">
          <ion-label
            :class="errorAdd && injury.date == '' ? 'required_text' : ''"
            >Date de la blessure *</ion-label
          >
          <ion-input
            :class="errorAdd && injury.date == '' ? 'required_class' : ''"
            type="datetime-local"
            label-placement="stacked"
            fill="outline"
            placeholder="2021-09-01"
            :value="injury.date"
            @ion-change="handleInput('date', $event.detail.value)"
          ></ion-input>
        </div>
        <div class="input_injurie">
          <ion-label
            :class="errorAdd && injury.state == '' ? 'required_text' : ''"
            >Etat de la blessure *</ion-label
          >
          <ion-list
            :class="errorAdd && injury.state == '' ? 'required_class' : ''"
            class="filter-item"
          >
            <ion-item>
              <ion-select
                :value="injury.state"
                interface="popover"
                placeholder="Etat de la blessure"
                class="custom-ion-select"
                :toggle-icon="chevronDownOutline"
                justify="space-between"
                @click="setIonSize()"
                @ion-change="handleInput('state', $event.detail.value)"
              >
                <ion-select-option
                  v-for="elem in injuries_state"
                  :key="elem.code"
                  :value="elem.code"
                  >{{ elem.name }}</ion-select-option
                >
              </ion-select>
            </ion-item>
          </ion-list>
        </div>
        <div
          style="
            display: flex;
            width: 100%;
            margin-top: 16px;
            justify-content: center;
            align-items: center;
          "
        >
          <BodyComponent
            :setMuscleSelected="setMuscle"
            :muscleSelected="injury.zone"
            :height="'200'"
            :width="'100'"
            :viewOnly="'edit'"
          />
        </div>
        <NavButton
          style="width: 100%; height: 40px; margin-top: 20px"
          @click="addInjurie"
          :disabled="editing"
          :text="editing ? 'Enregistrement en cours..' : 'Enregistrer'"
          :noIcon="true"
        />
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
  IonLabel,
  onIonViewWillEnter,
} from "@ionic/vue";
import "@/assets/base.css";
import "@/assets/main.css";
import { chevronDownOutline } from "ionicons/icons";
import NavButton from "../../components/NavButton/NavButton.vue";
import { ref } from "vue";
import { get, patch } from "../../lib/callApi";
import "./index.css";
//@ts-expect-error
import { BodyComponent } from "perform-body-component-lib";
import { store } from "../../store/store";
import router from "../../router";
import { useRoute } from "vue-router";
import { useErrorHandler } from "../../lib/useErrorHandler";

const { triggerError } = useErrorHandler() as any;

const navRoute = useRoute();

const editing = ref(false);

const errorAdd = ref(false);

const injury = ref({
  id: "",
  name: "",
  description: "",
  zone: [
    {
      zone: {
        name: "",
        code: "",
      },
    },
  ],
  date: "",
  user: "",
  state: "",
}) as any;

/**
 * Gère les entrées de l'utilisateur et met à jour les propriétés de l'objet `injury` correspondant.
 * @param {string} name - Le nom de la propriété à mettre à jour.
 * @param {string | undefined | null} valuePass - La valeur à affecter à la propriété.
 */
const handleInput = (name: string, valuePass: string | undefined | null) => {
  const value = valuePass as string;
  switch (name) {
    case "name":
      injury.value.name = value;
      break;
    case "description":
      injury.value.description = value;
      break;
    case "zone":
      injury.value.zone = [
        {
          zone: {
            code: value,
            name: "",
          },
        },
      ];
      break;
    case "date":
      injury.value.date = value;
      break;
    case "state":
      injury.value.state = value;
      break;
  }
};

const user = ref({} as any);
const id = ref(0);

/**
 * Définit la taille des popovers `ion-popover`.
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
};
/**
 * Ajoute une blessure en utilisant l'API `patch` et redirige vers la page de vue des blessures.
 */
const addInjurie = () => {
  editing.value = true;
  patch(
    "/injuries/" + id.value + "/",
    {
      body: {
        name: injury.value.name,
        description: injury.value.description,
        zone: injury.value.zone[0].zone.code,
        date: injury.value.date,
        state: injury.value.state,
        user: user.value.id,
      },
    },
    true
  ).then((res) => {
    if (res.status > 300) {
      triggerError("Erreur lors de la modification de la blessure");
      errorAdd.value = true;
      editing.value = false;
    } else {
      router.push("/view_injuries/" + id.value + "/?edit=true");
      errorAdd.value = false;
    }
  });
};

/**
 * Actions à exécuter lors de l'entrée dans la vue.
 */
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

const muscles = ref([] as any);

const setMuscle = (code: string) => {
  injury.value.zone = [
    {
      zone: {
        code: code,
        name: "",
      },
    },
  ];
};

onIonViewWillEnter(async () => {
  id.value = Number(navRoute.params.id);
  editing.value = false;
  injury.value = {
    id: "",
    name: "",
    description: "",
    zone: [
      {
        zone: {
          name: "",
          code: "",
        },
      },
    ],
    date: "",
    user: "",
    state: "",
  };
  store.get("user").then((res) => {
    const storeUser = res;
    if (storeUser !== "") {
      user.value = JSON.parse(storeUser).user;
      get("/injuries/" + id.value + "/", { body: {} }, true).then((res) => {
        if (res.status > 300) {
          triggerError("Erreur lors de la récupération des blessures");
        } else {
          injury.value = res;
          injury.value.zone = [
            {
              zone: {
                code: res.zone.code,
                name: "",
              },
            },
          ];
        }
      });
    }
  });
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

  get("/workzones/all", { body: {} }, false).then((res) => {
    if (res.status > 301) {
      triggerError("Erreur lors de la récupération des muscles");
    } else {
      muscles.value = res;
    }
  });
});
</script>
