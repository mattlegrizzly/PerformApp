<script setup>
import router from "@/router";
import { IonButton, IonIcon } from "@ionic/vue";
import { chevronBackOutline } from "ionicons/icons";

const props = defineProps(["url", "text", "back"]);
const nav = () => {
  console.log(props.url);
  if (props.back == "back") {
    router.back(props.url);
  } else {
    router.push(props.url);
  }
};
</script>
<style lang=""></style>

<template lang="">
  <ion-button size="small" @click="nav">
    <ion-icon :icon="chevronBackOutline"></ion-icon>
    {{ props.text }}
  </ion-button>
</template>
