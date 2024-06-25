<template>
  <ion-app>
    <ion-toast color="danger" :isOpen="showToast" @didDismiss="setOpen(false)" :message="toastMessage"
      :duration="2000" />
    <ion-router-outlet :animated="true">
      <router-view v-slot="{ Component }">
        <transition name="slide-left">
          <component :is="Component" />
        </transition>
      </router-view>
    </ion-router-outlet>
  </ion-app>
</template>

<script lang="ts" setup>
import { IonApp, IonRouterOutlet, IonToast } from '@ionic/vue';
import { ref, provide } from 'vue';


const showToast = ref(false);
const toastMessage = ref('');

const triggerError = (message: string) => {
  toastMessage.value = message;
  showToast.value = true;
};
const setOpen = (state: boolean) => {
  showToast.value = state;
};
provide('triggerError', triggerError);

</script>