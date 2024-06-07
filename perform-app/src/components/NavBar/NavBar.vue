<template>
  <ion-page>
    <ion-tabs>
      <ion-router-outlet></ion-router-outlet>
      <ion-tab-bar id="nav-menu-tab" style="border-radius: 20px 20px 0px 0px; height: 70px" slot="bottom">
        <ion-tab-button tab="home" @click="navigateTo('/home')">
          <ion-icon :name="isRouteActive(['Home']) ? 'home-selected' : 'home'" />
        </ion-tab-button>
        <ion-tab-button tab="search" @click="navigateTo('/search')">
          <ion-icon name="program" />
        </ion-tab-button>
        <ion-tab-button tab="exercises" @click="navigateTo('/exercises')">
          <ion-icon :name="isRouteActive(['Exercises', 'ExercisesView']) ? 'exercise-selected' : 'exercise'" />
        </ion-tab-button>
        <ion-tab-button tab="search" @click="navigateTo('/search')">
          <ion-icon name="trainer" />
        </ion-tab-button>
        <ion-tab-button @click="navigateTo('/profile')" tab="profile">
          <ion-icon
            :name="isRouteActive(['Profile', 'AddInjurie', 'ListInjuries', 'EditInjurie', 'ViewInjurie']) ? 'profile-selected' : 'profile'" />
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
} from "@ionic/vue";
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
