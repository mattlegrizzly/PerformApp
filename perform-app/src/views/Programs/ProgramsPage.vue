<style scoped>
.example-content {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
</style>

<template>
  <ion-page>
    <ion-content>
      <div>
        <div style=" height: calc(42vh - 50px); padding-top : 50px; width: 100%; display : flex; justify-content : center">
            <img width="200px" height="50px" src="@/assets/logo_perform.png" alt="logo" />
          </div>
        <h2 style="text-align: center; width: 100%;">Nos programmes à venir</h2>
      </div>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { IonHeader, IonToolbar, IonTitle, IonContent, IonPage } from '@ionic/vue';

export default {
  components: { IonHeader, IonToolbar, IonTitle, IonContent, IonPage },
};
</script>