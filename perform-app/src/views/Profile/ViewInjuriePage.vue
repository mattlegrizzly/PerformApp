<style scoped></style>

<template>
    <ion-page>
        <ion-content>
            <div class="perform-page">
                <div style="display: flex; justify-content: space-between">
                    <NavButton url="profile" text="Retour" back="back" />
                    <NavButton text="Editer" :noIcon="true" />
                </div>
                <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
                    {{ injury.name }}
                </h1>
                <p>
                    {{ injury.description == "" ? 'Rien à signaler' : injury.description }}
                </p>
            </div>
        </ion-content>
    </ion-page>
</template>

<script setup lang="ts">
import { IonContent, IonPage } from "@ionic/vue";
import NavButton from "../../components/NavButton/NavButton.vue";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

import "@/assets/base.css";
import "@/assets/main.css";
import { get } from "../../lib/callApi";
import { Injurie } from "../../types/types";

const router = useRoute();

const injury = ref({
    name: '',
    description: "",
    state: '',
    date: '',
    zone: ''
});
const id = ref(0);
onMounted(() => {
    id.value = Number(router.params.id);
    get('/injuries/' + id.value + '/', { body: {} }, true).then((res) => {
        if (res.status > 300) {

        } else {
            injury.value = res;
        }
    })
})
</script>
