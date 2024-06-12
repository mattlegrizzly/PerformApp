<template>
  <ion-app>
    <ion-router-outlet :animated="true">
      <router-view v-slot="{ Component, route }">
        <transition name="slide-left">
          <component :is="Component" />
        </transition>
      </router-view>
    </ion-router-outlet>
  </ion-app>
</template>

<script lang="ts" setup>
import { IonApp, IonRouterOutlet } from '@ionic/vue';
import { ref, watch } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();
const transitionName = ref('ion-slide');

const navigateTo = (to: any, animation: any) => {
  router.push({ path: to, params: { animation: animation } });
}

</script>

<style>
.default-animation-enter-active,
.default-animation-leave-active {
  transition: opacity 0.5s;
}

.default-animation-enter,
.default-animation-leave-to {
  opacity: 0;
}

.slide-left-enter-active,
.slide-left-leave-active {
  transition: transform 0.5s;
}

.slide-left-enter,
.slide-left-leave-to {
  transform: translateX(100%);
}

.slide-right-enter-active,
.slide-right-leave-active {
  transition: transform 0.5s;
}

.slide-right-enter,
.slide-right-leave-to {
  transform: translateX(-100%);
}
</style>