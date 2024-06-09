<style scoped>
ion-content .scroll-y {
  display: flex;
  justify-content: center;
  align-content: center;
}
</style>

<template>
  <ion-page>
    <ion-content style="align-content: center; justify-content: center; display: flex">
      <div style="
          display: flex;
          justify-content: center;
          position: absolute;
          top: 90px;
          width: 100%;
        ">
        <img style="width: 300px" src="../../assets/logo_perform.png" />
      </div>
      <div class="login_inputs">
        <div style="padding-left: 50px; padding-right: 50px">
          <h1>CONNEXION</h1>
          <div class="input-div">
            <ion-label>Email : </ion-label>
            <ion-input class="login-input" :class="error ? 'errorInput' : ''" fill="outline" slot="end"
              placeholder="force@gmail.com" shape="round" @ionInput="handleEmailInput($event)"
              :value="email"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Mot de passe : </ion-label>
            <ion-input class="login-input" :class="error ? 'errorInput' : ''" fill="outline" slot="end"
              placeholder="****" type="password" shape="round" @ionInput="handlePwdInput($event)"
              :value="pwd"></ion-input>
            <ion-label id="forgot-password">Mot de passe oublié ?</ion-label>
          </div>
          <div class="input-div">
            <ion-label v-if="error" class="error_label">Email ou mot de passe incorrect</ion-label>
          </div>
          <div class="input-div">
            <ion-button :disabled="loading" size="small" @click="connect">
              {{ loading ? "Connexion ... " : "Se connecter" }}
            </ion-button>
          </div>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonContent, IonPage, IonInput, IonLabel, IonButton } from "@ionic/vue";
import { ref } from "vue";
import "@/assets/base.css";
import "@/assets/main.css";
import { store } from "../../store/store";
import { post } from "../../lib/callApi";
import router from "../../router";
import "./index.css";

const error = ref(false);
const pwd = ref("");
const email = ref("");
const loading = ref(false);

const connect = () => {
  loading.value = true;
  const options = {
    body: {
      email: email.value,
      password: pwd.value,
    },
  };
  post("/login/", options, false).then((res) => {
    error.value = false;
    if (res.status > 301) {
      console.log("error");
      error.value = true;
      loading.value = false;
    } else {
      store.set("user", JSON.stringify(res)).then(() => {
        email.value = "";
        pwd.value = "";
        loading.value = false;
        router.push("/");
      });
    }
  });
};

const handleEmailInput = (event: any) => {
  email.value = event.target.value;
};

const handlePwdInput = (event: any) => {
  pwd.value = event.target.value;
};
</script>
