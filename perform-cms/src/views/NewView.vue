  <script setup lang="ts">
    import { IonBackButton, IonButtons, IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/vue';
    import { useRouter } from 'vue-router';
    const router = useRouter();
  </script>

<template>
    <ion-page>
      <ion-content>
        <ion-button @click="() => {
          router.back();
        }">Back</ion-button> 
      </ion-content>
    </ion-page>
  </template>
  