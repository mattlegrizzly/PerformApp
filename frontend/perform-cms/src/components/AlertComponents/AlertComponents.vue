<template>
  <v-alert :model-value="props.alertValue" border="start" close-label="Close Alert" :color="type" :title="title"
    closable @click:close="closePopup" class="alert_css">
    {{ message_alert }}
  </v-alert>
</template>

<style></style>

<script setup>
import { defineProps } from 'vue';
import { onMounted } from 'vue';
import { ref } from 'vue';

const props = defineProps(['message_alert', 'type', 'title', 'alertValue', 'setAlertValue'])

const closePopup = () => {
  props.setAlertValue(props.type)
}

</script>

<style></style>