<style scoped>
.input-div ion-list {
  width: auto;
  display: flex;
  align-items: center;
}

.input-div ion-input {
  padding-left: 20px !important;
  border-radius: 30px;
  border: 1px solid #d4d4d4;
  min-height: 40px !important;
  width: calc(100% - 20px);
  --padding-start: 0px !important;
  --padding-end: 20px !important;
  --border: none;
  --border-color: none;
  --border-width: none;
}

.input-div ion-item {
  border-radius: 30px;
  border: 1px solid #d4d4d4;
  min-height: 40px !important;
  height: 35px;

  width: 100%;
}

.edit_profile_div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: auto;
}
</style>

<template>
  <ion-page data-page="edit-profile">
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton url="profile" text="Retour" back="back" />
        </div>
        <h1 style="color: black; margin-top: 15px; margin-bottom: 10px">
          Modifier mon mot de passe
        </h1>
        <div class="edit_profile_div">
          <form>
            <div class="input-div">
              <ion-label
              :class="errorAdd ? 'required_text' : ''"
              >
                Mot de passe : </ion-label>
              <ion-input
                :type="showPassword ? 'text' : 'password'"
                class="login-input"
                :class="errorAdd ? 'required_class' : ''"
                fill="outline"
                slot="end"
                placeholder="Nouveau mot de passe (Inchangé si vide)"
                shape="round"
                @ionInput="handlePassword($event.detail.value)"
                :value="password"
                ><ion-icon
                  :icon="!showPassword ? eyeOff : eye"
                  slot="end"
                  @click="togglePasswordVisibility('showPassword')"
                  class="password-toggle-icon"
                ></ion-icon
              ></ion-input>
            </div>
            <div style="margin-top: 15px" class="input-div">
              <ion-label 
              :class="errorAdd ? 'required_text' : ''"
              >Répétez le mot de passe : </ion-label>
              <ion-input
              :class="errorAdd ? 'required_class' : ''"

                :type="showPasswordRepeat ? 'text' : 'password'"
                class="login-input"
                fill="outline"
                slot="end"
                placeholder="Nouveau mot de passe (Inchangé si vide)"
                shape="round"
                @ionInput="handlePasswordRepeat($event.detail.value)"
                :value="repeatPassword"
                ><ion-icon
                  :icon="!showPasswordRepeat ? eyeOff : eye"
                  slot="end"
                  @click="togglePasswordVisibility('showPasswordRepeat')"
                  class="password-toggle-icon"
                ></ion-icon
              ></ion-input>
            </div>
          </form>
          <NavButton
            style="margin-bottom: 10px; margin-top: 40px; height: 35px"
            :text="loading ? 'Enregistrement en cours..' : 'Enregistrer'"
            :noIcon="true"
            @click="editProfile"
            :disabled="loading"
          />
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
  IonIcon,
  onIonViewWillEnter,
} from "@ionic/vue";
import { ref } from "vue";
import { eye, eyeOff } from "ionicons/icons";
import "@/assets/base.css";
import "@/assets/main.css";
import { store } from "../../store/store";
import router from "../../router";
import NavButton from "../../components/NavButton/NavButton.vue";
import { patch } from "../../lib/callApi";
import "./index.css";

import { useErrorHandler } from "../../lib/useErrorHandler";

const { triggerError } = useErrorHandler() as any;

const loading = ref(false);
const errorAdd = ref(false);
const password = ref<string>("");
const repeatPassword = ref<string>("");
const showPassword = ref(false);
const showPasswordRepeat = ref(false);

const togglePasswordVisibility = (ref: any) => {
  if (ref == "showPassword") {
    showPassword.value = !showPassword.value;
  } else {
    showPasswordRepeat.value = !showPasswordRepeat.value;
  }
};

/**
 * Méthode pour changer la variable du password
 * @param value - Valeur passé par l'input
 */
const handlePassword = (value: string | null | undefined) => {
  if (value != null || value != undefined) password.value = value;
};

const handlePasswordRepeat = (value: string | null | undefined) => {
  if (value != null || value != undefined) repeatPassword.value = value;
};

/**
 * Édite le profil de l'utilisateur et met à jour les sports associés.
 */
const editProfile = async ()  => {
  if(password.value !== "" && (password.value == repeatPassword.value)){
    const user = await store.get('user')
    const parseUser = JSON.parse(user)
    
    patch(
      "/users/" + parseUser.user.id + "/set_password/",
      {
        body: {
          password: password.value,
        },
      },
      true
    ).then((res) => {
      
      if (res.status > 301) {
        if(res.data.password){
          triggerError(res.data.password)
        } else {
          triggerError('Erreur à la modification ré essayez')
        }
      } else {
        errorAdd.value = false;
        router.push('profile')
      }
    });
  } else {
    if(password.value ==""){
      triggerError('Le champ est vide')
    } else {
      triggerError('Les mots de passes sont différents')
    }

    errorAdd.value = true;
  }
};

/**
 * Actions à exécuter lors de l'entrée dans la vue.
 */
onIonViewWillEnter(async () => {
  password.value = "";
  repeatPassword.value = "";
  showPassword.value = false;
  showPasswordRepeat.value = false;
  errorAdd.value = false;
});
</script>
