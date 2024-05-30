<script setup>
import router from "@/router";
import { IonButton, IonIcon } from "@ionic/vue";
import { chevronBackOutline } from "ionicons/icons";
import { onMounted, ref } from "vue";

const props = defineProps(["url", "text", "back", "noIcon"]);

const noIconYes = ref(false);
const nav = () => {
  if (props.url == undefined) {
    return;
  }
  if (props.back == "back") {
    router.back(props.url);
  } else {
    console.log(props.url);
    router.push(props.url);
  }
};
onMounted(() => {
  console.log(props);
  if (props.noIcon == true) {
    noIconYes.value = true;
  } else {
    noIconYes.value = false;
  }
});
</script>
<style lang=""></style>

<template lang="">
  <ion-button size="small" @click="nav">
    <ion-icon v-if="noIconYes == false" :icon="chevronBackOutline"></ion-icon>
    {{ props.text }}
  </ion-button>
</template>
