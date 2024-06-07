<style scoped></style>

<template>
  <ion-page>
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton url="profile" text="Retour" back="back" />
          <NavButton text="Enregistrer" :noIcon="true" />
        </div>
        <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
          Toutes mes blessures
        </h1>
        <button @click="goBack">Go back</button>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonContent, IonPage } from "@ionic/vue";
import "@/assets/base.css";
import "@/assets/main.css";
import { onBeforeUnmount, onMounted, onUpdated } from "vue";

import { useRouter } from "vue-router";
const router = useRouter()

const goBack = () => router.push('/exercises')

onMounted(() => {
  console.log('mounter')
})

onUpdated(() => {
  console.log('updated')
})

onBeforeUnmount(() => {
  console.log('before unmount')
})
</script>
