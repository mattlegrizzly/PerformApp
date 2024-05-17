<style scoped></style>

<template>
  <ion-page>
    <div id="header-wrapper">
      <div class="perform-page">
        <h1 style=" margin-top: 0px;">Liste exercices</h1>
        <ion-input label="Outline input" label-placement="floating" fill="outline"
          placeholder="Cherchez un exercice"></ion-input>
        <div class="filter-div">
          <ion-button>Filtres</ion-button>
          <ion-list class="filter-item">
            <ion-item>
              <ion-select aria-label="Trier par" interface="popover" placeholder="Trier par">
                <ion-select-option value="apples">Apples</ion-select-option>
                <ion-select-option value="oranges">Oranges</ion-select-option>
                <ion-select-option value="bananas">Bananas</ion-select-option>
              </ion-select>
            </ion-item>
          </ion-list>
        </div>
      </div>
      <ion-segment value="all">
        <ion-segment-button value="all">
          <ion-label>Tous les exercices</ion-label>
        </ion-segment-button>
        <ion-segment-button value="favorites">
          <ion-label>Mes favoris</ion-label>
        </ion-segment-button>
      </ion-segment>
    </div>

    <ion-content color="light">
      <ion-list class="list-item" :inset="true" v-for="exercise in exercises" :key="exercises.id">
        <ion-item>
          <ion-label>{{ exercise.name }}</ion-label>
          <ion-icon :icon="chevronForwardOutline"></ion-icon>
        </ion-item>
      </ion-list>
    </ion-content>

  </ion-page>
</template>

<script lang="ts" setup>

import { IonLabel, IonList, IonItem, IonSegment, IonSegmentButton, IonIcon, IonInput, IonContent, IonPage } from '@ionic/vue';
import { get } from '@/lib/callApi.ts';
import { onMounted, ref } from 'vue';
import { chevronForwardOutline } from 'ionicons/icons';

const exercises: any = ref([]);

import './index.css'

onMounted(() => {
  get('/exercises', { body: {} }, false, false).then((res: any) => {
    if (res.status > 300) {
    } else {
      exercises.value = res.results;
    }
  })
})
</script>