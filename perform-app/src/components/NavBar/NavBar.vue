<template>
  <ion-page>
    <ion-tabs>
      <ion-router-outlet></ion-router-outlet>
      <ion-tab-bar
        id="nav-menu-tab"
        style="border-radius: 20px 20px 0px 0px; height: 70px"
        slot="bottom"
      >
        <ion-tab-button tab="home" href="/home">
          <ion-icon :name="isRouteActive('Home') ? 'home-selected' : 'home'" />
        </ion-tab-button>
        <ion-tab-button tab="search" href="/search">
          <ion-icon name="program" />
        </ion-tab-button>
        <ion-tab-button tab="exercises" href="/exercises">
          <ion-icon
            :name="
              isRouteActive('Exercises') ? 'exercise-selected' : 'exercise'
            "
          />
        </ion-tab-button>
        <ion-tab-button tab="search" href="/search">
          <ion-icon name="trainer" />
        </ion-tab-button>
        <ion-tab-button href="/profile" tab="profile">
          <ion-icon
            :name="isRouteActive('Profile') ? 'profile-selected' : 'profile'"
          />
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
  IonLabel,
  IonIcon,
} from "@ionic/vue";
import { useRoute } from "vue-router";
import "./index.css";
import "../../assets/base.css";
const route = useRoute();

const isRouteActive = (routeName: string) => {
  console.log(routeName, " ", route.name);
  return route.name === routeName;
};
</script>
