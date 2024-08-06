<template>
  <ion-page data-page="Login" class="home-ion-page">
    <ion-content
      id="login-home-page"
      style="align-content: center; justify-content: center; display: flex"
    >
      <div class="logo_perform_login">
        <img
          style="width: 250px"
          src="../../assets/logo_perform.png"
          alt="logo perform"
        />
      </div>
      <div class="login_inputs">
        <div
          style="
            padding-left: 50px;
            padding-right: 50px;
            width: 50%;
            padding-bottom: 30px;
            border-radius: 25px;
            box-shadow: 0px 0px 10px 5px lightgray;
          "
        >
          <h1>CONNEXION</h1>
          <form>
            <div class="input-div">
              <ion-label>Email : </ion-label>
              <ion-input
                class="login-input"
                :class="error ? 'errorInput' : ''"
                fill="outline"
                slot="end"
                id="email-input"
                placeholder="force@gmail.com"
                inputmode="email"
                @ionFocus="onFocus"
                @ionBlur="onBlur"
                shape="round"
                @ionInput="handleEmailInput($event)"
                :value="email"
              ></ion-input>
            </div>
            <div class="input-div">
              <ion-label>Mot de passe : </ion-label>
              <ion-input
                class="login-input"
                :class="error ? 'errorInput' : ''"
                fill="outline"
                slot="start"
                placeholder="****"
                :type="showPassword ? 'text' : 'password'"
                shape="round"
                @ionInput="handlePwdInput($event)"
                :value="pwd"
                ><ion-icon
                  :icon="!showPassword ? eyeOff : eye"
                  slot="end"
                  @click="togglePasswordVisibility"
                  class="password-toggle-icon"
                ></ion-icon
              ></ion-input>

              <ion-label id="forgot-password">Mot de passe oublié ?</ion-label>
            </div>
            <div class="input-div">
              <ion-label v-if="error" class="error_label"
                >Email ou mot de passe incorrect</ion-label
              >
            </div>
            <div
              class="input-div"
              style="display: flex; justify-content: center"
            >
              <ion-button :disabled="loading" style="margin-top: 10px;" size="small" @click="connect">
                {{ loading ? "Connexion ... " : "Se connecter" }}
              </ion-button>
            </div>
          </form>
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
  IonButton,
  IonIcon,
  onIonViewWillEnter,
} from "@ionic/vue";
import { ref } from "vue";
import "@/assets/base.css";
import "@/assets/main.css";
import { store } from "../../store/store";
import { eye, eyeOff } from "ionicons/icons";
import { post } from "../../lib/callApi";
import router from "../../router";
import "./index.css";
import { useErrorHandler } from "../../lib/useErrorHandler";

const { triggerError } = useErrorHandler() as any;

const error = ref(false);
const pwd = ref("");
const email = ref("");
const loading = ref(false);
const showPassword = ref(false);

onIonViewWillEnter(async () => {
  
});

const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value;
};

const onFocus = () => {
  
  if (isMobileDevice()) {
    document.body.classList.add("keyboard-open");
  }
};
const onBlur = () => {
  if (isMobileDevice()) {
    document.body.classList.remove("keyboard-open");
  }
};

/**
 * Fonction de connexion
 */
const connect = () => {
  loading.value = true;
  const options = {
    body: {
      email: email.value,
      password: pwd.value,
    },
  };
  try {
    post("/login/", options, false).then((res) => {
      
      error.value = false;
      if (res.status > 301) {
        triggerError("Erreur de connexion");
        error.value = true;
        loading.value = false;
      } else {
        store.set("user", JSON.stringify(res)).then(() => {
          email.value = "";
          pwd.value = "";
          loading.value = false;
          router.push("/home");
        });
      }
    });
  } catch (error) {
    
    triggerError(error);
  }
};

/**
 * Fonction de modification de la value du mail
 * @param event
 */
const handleEmailInput = (event: any) => {
  email.value = event.target.value;
};

/**
 * Fonction de modification de la value du mot de passe
 * @param event
 */
const handlePwdInput = (event: any) => {
  pwd.value = event.target.value;
};

const isMobileDevice = () => {
  return /Mobi|Android/i.test(navigator.userAgent);
};
</script>

<style scoped>
ion-content .scroll-y {
  display: flex;
  justify-content: center;
  align-content: center;
}
</style>
