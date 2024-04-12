<template>
    <v-alert
    :model-value="props.alertValue"
    border="start"
    close-label="Close Alert"
    :color="type"
    :title="title"
    closable
    @click:close="closePopup"
  >
    {{ message_alert }}
  </v-alert>
</template>

<style>
</style>

<script setup>
import { defineProps } from 'vue';
import { onMounted } from 'vue';
import { ref } from 'vue';

const props = defineProps(['message_alert', 'type', 'title', 'alertValue'])

onMounted(() => {
  console.log(props)
})

const closePopup = () => {
  alert.value = false
}

</script>