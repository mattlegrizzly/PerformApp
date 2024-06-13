<template>
    <ion-toast trigger="open-toast" :message="props.message" :isOpen='props.open' color="danger"
        :duration="3000"></ion-toast>
</template>

<script setup lang="ts">
import { IonToast } from '@ionic/vue';

const props = defineProps(['message', 'open'])
</script>