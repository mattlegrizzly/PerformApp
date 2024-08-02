<style scoped>

.img_div {
    height: 100px;
    margin: 10px;
    width: calc(100% - 20px);
    overflow: hidden;
    border-radius: 10px;
    display: flex;
    align-items: center;

}
.img_program {
    border-radius: 10px;
    object-fit:fill;
    width: 100%;
}

.description_card_program p {
    font-size: 10px;
}

.program-title {
    font-weight: 600;
}

.description-text {
  display: -webkit-box;
  -webkit-line-clamp: 3; /* Nombre de lignes à afficher */
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  max-height: 70px; /* Hauteur maximale en pixels */
}

.description_card_program ion-chip {
        padding-left: 5px;
        padding-right: 5px;
        height: 15px !important;
        min-height: 0px;
        color: white;
        font-size: 8px;
        background-color: var(--secondary-blue);
        pointer-events: none;
}
</style>

<template>
  <ion-card>
    <div class="img_div">
        <img
        class="img_program"
          alt="Silhouette of mountains"
          :src=props.program.photo_url
        />
    </div>
    <ion-card-header>
    </ion-card-header>
    
    <ion-card-content class="description_card_program">
        <ion-card-title class="program-title">{{ props.program.title }}</ion-card-title>
        <ion-chip>{{props.program.sport}}</ion-chip>
        <p class="description-text">
    {{ props.program.description }}
  </p>
        <p style="font-weight: 600; width: 100%; font-size: 8px;">Durée {{props.program.duration}}</p>
        <div style="display: flex; justify-content: space-between;">
            <p style="font-weight: 600;">{{props.program.price}}</p>
            <p>Voir plus</p>
        </div>
    </ion-card-content>
  </ion-card>
</template>

<script setup lang="ts">
import {
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonCardTitle,
  IonChip
} from "@ionic/vue";
import "@/assets/base.css";
import "@/assets/main.css";
import { defineProps } from "vue";
import { useRouter } from "vue-router";

const props = defineProps(["program"]);

const router = useRouter();

const goBack = () => router.push("/exercises");
</script>
