<template>
  <ion-app>
    <ion-router-outlet>
      <router-view />
    </ion-router-outlet>
  </ion-app>
</template>

<script lang="ts" setup>
import { IonApp, IonRouterOutlet } from '@ionic/vue';
import { useRoute } from 'vue-router';

const route = useRoute()
</script>