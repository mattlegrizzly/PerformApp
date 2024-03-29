<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { IonButtons, IonContent, IonHeader, IonMenu, IonMenuButton, IonPage, IonTitle, IonToolbar } from '@ionic/vue';
import { defineComponent } from 'vue';

</script>

<template>
  <header>

    <template>
      <a href="/home">Home</a>
      <a href="/users">Users</a>
      <a href="/exercices">Exercices</a>
      <a href="/materials">Materials</a>
    </template>


  </header>

  <RouterView />
</template>
