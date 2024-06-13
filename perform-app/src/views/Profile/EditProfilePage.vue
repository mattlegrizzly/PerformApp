<style scoped>
.input-div ion-list {
  width: auto;
  height: 40px;
  display: flex;
  min-height: 40px !important;
  align-items: center;
}

.input-div ion-input {
  padding-left: 20px !important;
  border-radius: 30px;
  border: 1px solid #d4d4d4;
  min-height: 40px !important;
  width: calc(100% - 20px);
  --padding-start: 0px !important;
  --padding-end: 0px !important;
  --border: none;
  --border-color: none;
  --border-width: none;
}

.input-div ion-item {
  border-radius: 30px;
  border: 1px solid #d4d4d4;
  min-height: 40px !important;
  height: 40px;

  width: 100%;
}

.edit_profile_div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: auto;
}

.profile_image {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 130px;
  height: 130px;
}


.img_div {
  overflow: hidden;
  border-radius: 200px;

}

.div_pp {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.div_pp ion-label {
  width: 100%;

}

ion-chip {
  padding-left: 10px;
  padding-right: 10px;
  color: white;
  background-color: var(--primary-blue);
}
</style>

<template>
  <ion-page data-page="edit-profile">
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton url="profile" text="Retour" back="back" />
        </div>
        <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
          Modifier mes informations
        </h1>
        <div class="edit_profile_div">
          <div class="div_pp">
            <ion-label>Photo de profil : </ion-label>
            <div class="profile_image">
              <div class="img_div">
                <ion-img
                  :src="fileToDisplay != '' ? fileToDisplay : 'https://static.vecteezy.com/system/resources/previews/004/968/473/original/upload-or-add-a-picture-jpg-file-concept-illustration-flat-design-eps10-modern-graphic-element-for-landing-page-empty-state-ui-infographic-icon-etc-vector.jpg'"
                  style="object-fit: cover;
    overflow: hidden;
    height: 130px;
    width: 130px;
    display: flex;
    justify-content: center;
    align-items: center;" @click="triggerFileInput"></ion-img>
                <ion-icon style="color:black; position: absolute; right: 0px;" :icon="pencil"></ion-icon>
              </div>
              <input type="file" accept="image/*" id="fileINput" ref="fileInput" @change="handleFileChange"
                style="display: none"></input>
            </div>

          </div>
          <div class="input-div">
            <ion-label>Nom : </ion-label>
            <ion-input type="text" class="login-input" fill="outline" slot="end" placeholder="Prénom" shape="round"
              @ionInput="handleInput('first_name', $event.detail.value)" :value="user.first_name"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Prénom : </ion-label>
            <ion-input type="text" class="login-input" fill="outline" slot="end" placeholder="Nom" shape="round"
              @ionInput="handleInput('last_name', $event.detail.value)" :value="user.last_name">
            </ion-input>
          </div>
          <div class="input-div">
            <ion-label>Email : </ion-label>
            <ion-input type="email" class="login-input" fill="outline" slot="end" placeholder="email@perform.com"
              shape="round" @ionInput="handleInput('email', $event.detail.value)" :value="user.email"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Âge : </ion-label>
            <ion-input type="number" class="login-input" fill="outline" slot="end" placeholder="20" shape="round"
              @ionInput="handleInput('age', $event.detail.value)" :value="user.age"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Taille : </ion-label>
            <ion-input type="number" class="login-input" fill="outline" slot="end" placeholder="170" shape="round"
              @ionInput="handleInput('size', $event.detail.value)" :value="user.size"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Poids : </ion-label>
            <ion-input type="number" class="login-input" fill="outline" slot="end" placeholder="80" shape="round"
              @ionInput="handleInput('weight', $event.detail.value)" :value="user.weight"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Sélectionne tes sports : </ion-label>
            <ion-list>
              <ion-item>
                <ion-select @ionChange="updateSelectedSports" class="custom-ion-select" :value="sports_user_temp"
                  aria-label="Fruit" placeholder="Selectionner vos sports" :multiple="true" :compareWith="compareWith">
                  <ion-select-option v-for="(sport) in sports" :value="{ id: sport.id, name: sport.name }"
                    :key="sport.id" aria-selected="true">{{ sport.name }}</ion-select-option>
                </ion-select>
              </ion-item>
            </ion-list>
            <div style="margin-top: 10px; margin-bottom: 10px">
              <ion-chip :icon="close" v-for="sport of sports_user_temp" color="primary">
                <ion-icon :id="sport.id" :icon="close" @click="removeSport"></ion-icon>
                <ion-label>{{ sport.name }}</ion-label>
              </ion-chip>
            </div>
          </div>
          <NavButton style="margin-bottom: 10px" text="Enregistrer" @click="editProfile" />
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonContent,
  IonPage,
  IonInput,
  IonLabel,
  IonList,
  IonItem,
  IonSelect,
  IonSelectOption,
  IonImg,
  IonIcon,
  IonChip,
  onIonViewWillEnter
} from "@ionic/vue";
import { ref } from "vue";
import { close, pencil } from "ionicons/icons";
import "@/assets/base.css";
import "@/assets/main.css";
import { store } from "../../store/store";
import router from "../../router";
import { Sport, IEUserData } from "../../types/allTypes";
import NavButton from "../../components/NavButton/NavButton.vue";
import { get, patch, del, post } from "../../lib/callApi";
import "./index.css";

import { useErrorHandler } from '../../lib/useErrorHandler';

const { triggerError } = useErrorHandler() as any;

const api = import.meta.env.VITE_API_URL;
const fileInput = ref(null);

/**
 * Utilisateur avec ses propriétés et ses sports associés.
 */
const user = ref<{
  age: number,
  weight: number,
  size: number,
  email: string,
  first_name: string,
  gender: string,
  id: number,
  last_name: string,
  profile_picture: string,
  sports_user: Sport[],
}>({
  age: 0,
  weight: 0,
  size: 0,
  email: "",
  first_name: "",
  gender: "",
  id: 1,
  last_name: "",
  profile_picture: "",
  sports_user: [] as Sport[],
});

const sports_user_temp = ref<Sport[]>([]);
const sports = ref<Sport[]>([]);
const fileToDisplay = ref<string>('');
const fileToSend = ref<File | null>(null);

/**
 * Gère l'entrée de l'utilisateur et met à jour la propriété correspondante.
 * @param {string} key - La clé de l'objet utilisateur à mettre à jour.
 * @param {string | null | undefined} valuePass - La valeur à affecter à la clé.
 */
const handleInput = (key: keyof IEUserData, valuePass: string | null | undefined): void => {
  const value = valuePass as never;
  user.value[key] = value;
};

/**
 * Compare deux objets en fonction de leur propriété `id`.
 * @param {any} o1 - Premier objet à comparer.
 * @param {any} o2 - Deuxième objet à comparer.
 * @returns {boolean} - Vrai si les objets ont le même `id`, sinon faux.
 */
const compareWith = (o1: any, o2: any): boolean => {
  return o1 && o2 ? o1.id === o2.id : o1 === o2;
};

/**
 * Trouve un élément dans un tableau par son identifiant.
 * @param {any[]} array - Tableau dans lequel chercher.
 * @param {string | number | Sport} id - Identifiant de l'élément à trouver.
 * @returns {any} - Élément trouvé ou undefined.
 */
function findById(array: any[], id: string | number | Sport): any {
  return array.find(item => item.id === id);
}

/**
 * Édite le profil de l'utilisateur et met à jour les sports associés.
 */
const editProfile = (): void => {
  const userEdit = {
    age: user.value.age,
    weight: user.value.weight,
    size: user.value.size,
    email: user.value.email,
    last_name: user.value.last_name,
    first_name: user.value.first_name,
  } as any;
  if (fileToSend.value) {
    userEdit['profile_picture'] = fileToSend.value;
  }

  const inPlus: Sport[] = [];
  const inMinus: Sport[] = [];
  const equivalent: Sport[] = [];

  for (const newItem of sports_user_temp.value) {
    let find = false;
    for (const constSport of user.value.sports_user) {
      //@ts-expect-error
      if (newItem.id === constSport.sport.id) {
        equivalent.push(newItem)
        find = true;
      }
    }
    if (!find) {
      inPlus.push(newItem)
    }
  }

  user.value.sports_user.forEach((baseItem: any) => {
    const matchInNew = findById(sports_user_temp.value, baseItem.sport.id);
    if (!matchInNew) {
      inMinus.push(baseItem);
    }
  });

  inPlus.forEach(sport => {
    post("/sports_user/", { body: { user: user.value.id, sport: sport.id } }, true, true).then((res) => {
      if (res.status > 300) {
        triggerError('Erreur lors de l\'ajout du sport : ', sport.name);
      }
    });
  });

  inMinus.forEach(sport => {
    del("/sports_user/" + sport.id + "/").then((res) => {
      if (res.status > 300) {
        triggerError('Erreur lors de la suppression du sport : ', sport.name);
      }
    });
  });

  patch("/users/" + user.value.id + "/", { body: userEdit }, true, true).then((res) => {
    if (res.status > 300) {
      triggerError('Erreur lors de la modification, réessayez');

    } else {
      router.push('/profile');
    }
  });
};


/**
 * Déclenche l'entrée de fichier pour sélectionner un fichier.
 */
const triggerFileInput = () => {
  //@ts-expect-error
  if (fileInput.value) fileInput.value.click();
};

/**
 * Gère le changement de fichier pour l'upload de l'image de profil.
 * @param {Event} event - Événement de changement de fichier.
 */
const handleFileChange = (event: Event): void => {
  const target = event.target as HTMLInputElement;
  const file = target.files?.[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      const result = e.target?.result;
      if (result) {
        fileToDisplay.value = result as string;
        fileToSend.value = file;
      }
    };
    reader.readAsDataURL(file);
  }
};

/**
 * Supprime un sport de la liste temporaire de sports.
 * @param {Event} event - Événement de suppression.
 */
const removeSport = (event: Event): void => {
  const target = event.target as HTMLButtonElement;
  const id = Number(target.id);
  sports_user_temp.value = sports_user_temp.value.filter(sport => sport.id !== id);
};

/**
 * Met à jour les sports sélectionnés temporairement.
 * @param {CustomEvent} change - Événement de changement de sélection.
 */
const updateSelectedSports = (change: CustomEvent): void => {
  sports_user_temp.value = change.detail.value;
};

/**
 * Actions à exécuter lors de l'entrée dans la vue.
 */
onIonViewWillEnter(async () => {
  sports_user_temp.value = [];
  const storeUser = await store.get("user");
  if (storeUser !== "") {
    user.value = JSON.parse(storeUser).user;
    if (user.value.profile_picture) {
      fileToDisplay.value = api + user.value.profile_picture;
    }
    user.value.sports_user.forEach((sport: any) => {
      sports_user_temp.value.push(sport.sport);
    });
  }

  get("/sports", { body: {} }, false).then((res) => {
    if (res.status > 300) {
      triggerError('Erreur lors de la récupération des sports');
    } else {
      sports.value = res.results;
    }
  });

  const ionSelect = document.querySelectorAll(".custom-ion-select");
  ionSelect.forEach(elem => {
    const shadowRoot = elem.shadowRoot;
    if (shadowRoot) {
      const style = document.createElement("style");
      style.textContent = `
        .select-wrapper-inner {
          width: 100%;
          justify-content: space-between;
        }
      `;
      shadowRoot.appendChild(style);
    }
  });
});
</script>