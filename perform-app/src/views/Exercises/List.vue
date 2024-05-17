<style scoped>
.example-content {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

#header-list #background-content {
  height: 180px;
}
</style>

<template>
  <ion-page>
    <ion-content id="header-list" style="height: 180px !important;" color="light">
      <div style="height: auto; background-color: white; ">
        <h1 style="margin-top: 0px;">Liste exercices</h1>
        <ion-input label="Outline input" label-placement="floating" fill="outline" placeholder="Enter text"></ion-input>
        <ion-segment value="all">
          <ion-segment-button value="all">
            <ion-label>Tous les exercices</ion-label>
          </ion-segment-button>
          <ion-segment-button value="favorites">
            <ion-label>Mes favoris</ion-label>
          </ion-segment-button>
        </ion-segment>
      </div>
    </ion-content>

    <ion-content color="light">

      <div style="height: auto;">
        <ion-list :inset="true" v-for="exercise in exercises" :key="exercises.id">
          <ion-item>
            <ion-label>{{ exercise.name }}</ion-label>
          </ion-item>
        </ion-list>
      </div>
    </ion-content>

  </ion-page>
</template>

<script lang="ts" setup>

import { IonLabel, IonList, IonItem, IonSegment, IonSegmentButton, IonButton, IonInput, IonContent, IonPage } from '@ionic/vue';
import { get } from '@/lib/callApi.ts';
import { onMounted, ref } from 'vue';

const exercises: any = ref([]);
onMounted(() => {
  get('/exercises', { body: {} }, false, false).then((res: any) => {
    if (res.status > 300) {
    } else {
      exercises.value = res.results;
    }
  })
})
</script>