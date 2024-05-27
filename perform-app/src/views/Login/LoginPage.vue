<style scoped></style>

<template>
  <ion-page>
    <ion-content style="align-content: center;">
      <div style="display: flex; justify-content: center; position: absolute; top : 200px">
        <img style="width: 300px;" src="../../assets/logo_perform.png">
      </div>
      <div>
        <h1>CONNEXION</h1>
        <ion-label>Email </ion-label>
        <ion-input id="search-input" fill="outline" slot="end" placeholder="force@gmail.com" shape="round"
          @ionInput="handleSearchInput($event)"></ion-input>
        <ion-label>Email </ion-label>
        <ion-input id="search-input" fill="outline" slot="end" placeholder="****" shape="round"
          @ionInput="handleSearchInput($event)"></ion-input>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonContent, IonPage, IonInput, IonLabel } from "@ionic/vue";
import "@/assets/base.css";
import "@/assets/main.css";
</script>
