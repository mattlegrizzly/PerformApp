<template>
  <ion-app>
    <ion-router-outlet :animated="true" @ionNavWillChange="handleNavChange">
      <router-view />
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

const handleNavChange = () => {
  const currentRoute = router.currentRoute.value.name;
  // Définir le nom de la transition en fonction de la route
  if (currentRoute === 'Home' || currentRoute === "Exercises") {
    transitionName.value = 'ion-fade';
    console.log('fade')
  } else {

    transitionName.value = 'ion-slide';
  }

  const outlet = document.querySelector('ion-router-outlet');
  if (outlet) {
    console.log(outlet)
    outlet.classList.remove('ion-fade', 'ion-slide');
    outlet.classList.add(transitionName.value);
  }
};

watch(
  () => route.name,
  () => {
    handleNavChange();
  }
);
</script>

<style>
/* Animation de glissement */
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.5s;
}

.slide-enter,
.slide-leave-to

/* .slide-leave-active in <2.1.8 */
  {
  transform: translateX(100%);
}

.slide-leave,
.slide-enter-to {
  transform: translateX(0);
}

/* Animation de fondu */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to

/* .fade-leave-active in <2.1.8 */
  {
  opacity: 0;
}
</style>