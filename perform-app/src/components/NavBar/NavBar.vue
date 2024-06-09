<template>
  <ion-page>
    <ion-tabs>
      <ion-router-outlet></ion-router-outlet>
      <ion-tab-bar id="nav-menu-tab" style="border-radius: 20px 20px 0px 0px; height: 60px" slot="bottom">
        <ion-tab-button tab="home" @click="navigateTo('/home')">
          <ion-icon :name="isRouteActive(['Home']) ? 'home-selected' : 'home'" />
          <ion-label>Accueil</ion-label>
        </ion-tab-button>
        <ion-tab-button tab="programs" @click="navigateTo('/programs')">
          <ion-icon name="program" />
          <ion-label>Programmes</ion-label>
        </ion-tab-button>
        <ion-tab-button tab="exercises" @click="navigateTo('/exercises')">
          <ion-icon :name="isRouteActive(['Exercises', 'ExercisesView']) ? 'exercise-selected' : 'exercise'" />
          <ion-label>Bibliothèque</ion-label>
        </ion-tab-button>
        <ion-tab-button tab="stats" @click="navigateTo('/stats')">
          <ion-icon style="color: white" :icon="isRouteActive(['Statistics']) ? statsChart : statsChartOutline" />
          <ion-label>Stats</ion-label>

        </ion-tab-button>
        <ion-tab-button @click="navigateTo('/profile')" tab="profile">
          <ion-icon
            :name="isRouteActive(['Profile', 'AddInjurie', 'ListInjuries', 'EditInjurie', 'ViewInjurie']) ? 'profile-selected' : 'profile'" />
          <ion-label>Profil</ion-label>

        </ion-tab-button>
      </ion-tab-bar>
    </ion-tabs>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonPage,
  IonTabs,
  IonRouterOutlet,
  IonTabBar,
  IonTabButton,
  IonIcon,
  IonLabel
} from "@ionic/vue";
import { statsChart, statsChartOutline } from 'ionicons/icons'
import { useRoute, useRouter } from "vue-router";
import "./index.css";
import "../../assets/base.css";

const route = useRoute();
const router = useRouter();

const isRouteActive = (routeNames: string[]) => {
  return routeNames.includes(route.name?.toString() || '');
};

const navigateTo = (path: string) => {
  if (router.currentRoute.value.path !== path) {
    router.push(path);
  }
};
</script>
