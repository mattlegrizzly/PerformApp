<script setup lang="ts">
import NavMenu from '@/components/NavMenu/NavMenu.vue'
import { ref } from 'vue'
import { get } from '@/lib/callApi'
import { useRoute } from 'vue-router'
import { onMounted } from 'vue'
import NavButton from '@/components/NavButton/NavButton.vue'
import AlertComponents from '@/components/AlertComponents/AlertComponents.vue'
import DeleteModalComponent from '@/components/DeleteModalComponent/DeleteModalComponent.vue'
//@ts-expect-error
import {BodyComponent} from 'perform-body-component-lib'
import "perform-body-component-lib/style.css";
import './exercises.css'
import type { Muscle } from '@/types/types'

const muscle_selected: any = ref([])

const showMuscle = ref(false)

const api_url = import.meta.env.VITE_API_URL

const router = useRoute()
const exercise = ref({
  steps_exercise : []
})
const exercise_id = ref(-1)
const videoController = ref(document.createElement('video'))

const back = ref('back')

const alertErr = ref(false)
const error_message = ref('')
const error_title = ref('')

const setAlertValue = (type: string) => {
  if (type === "error") {
    alertErr.value = false
  } else {

  }
}

const getExercises = async () => {
  const id = router.params.exercise_id

  const res = await get('/admin/exercises/' + id + '/')
  if (res.status === 404) {
    error_title.value = 'Erreur à la récupération de l\'exerecice pour id ' + id
    error_message.value = res.data.detail
    alertErr.value = true
  } else {
    exercise.value = await res
    const muscle_res = await res.zone_exercises
    const temp_muscle: Array<Muscle> = [];
    muscle_res.map((muscle: Muscle) => {
      temp_muscle.push(muscle);
    })
    muscle_selected.value = temp_muscle
    showMuscle.value = true;
    videoController.value.load()
  }
}

onMounted(() => {
  if (router.query.edit) {
    back.value = ''
  } else {
    back.value = 'back'
  }
  exercise.value = {
  steps_exercise : []
}
  showMuscle.value = false;
  muscle_selected.value = []
  getExercises()
})
</script>

<template lang="">
  <NavMenu />
  <div class="mainWrapper">
    <AlertComponents
      :message_alert="error_message"
      :type="'error'"
      :title="error_title"
      :alertValue="alertErr"
      :setAlertValue="setAlertValue"
    />
    <div class="headerBtns">
      <NavButton
        class="returnBtn"
        :text="'Retour'"
        :url="'/exercises'"
        :back="back"
        prepend-icon="mdi-arrow-left"
      />
      <div>
        <NavButton
          class="editBtn"
          :text="'Modifier'"
          :url="'/exercises/edit/' + router.params.exercise_id"
          prepend-icon="mdi-pencil"
        />
        <div style="margin-top:10px">
          <DeleteModalComponent
            :item="exercise.name"
            url="/admin/exercises"
            :id="router.params.exercise_id"
            list="exercises"
          />
        </div>
      </div>
    </div>
    <h1>Carte de l'exercise : {{ exercise === undefined ? '' : exercise.name }}</h1>
    <h2 class="showTitle">Titre</h2>
    <p>{{ exercise === undefined ? '' : exercise.name }}</p>

    <h2 class="showTitle">Matériels</h2>
    <div v-for="(element, index) in exercise.material_exercise" :key="index">
      <p>- {{ element.material.name }}</p>
    </div>
    <h2 class="showTitle">Muscles</h2>
    <BodyComponent
        :height="400"
        v-if="showMuscle"
        :muscleSelected="muscle_selected"
        :viewOnly="'show'"
      />
    <h2 class="showTitle">Sports</h2>
    <v-chip-group v-for="(element, index) in exercise.sports_exercise" :key="index">
      <v-chip>{{ element.sport.name }}</v-chip>
    </v-chip-group>
    <h2 class="showTitle">Etapes d'exécution</h2>
    <div v-for="(element, index) in exercise.steps_exercise" :key="index">
      <p>Etape {{ index + 1 }} : {{ element.text }}</p>
    </div>
    <h2 class="showTitle">Vidéo</h2>
    <div class="imageDiv">
      <video
        ref="videoController"
        id="player"
        playsinline
        controls
        data-poster="/path/to/poster.jpg"
      >
        <source :src="api_url + exercise.video" type="video/mp4" />
        <source :src="api_url + exercise.video" type="video/webm" />
      </video>
    </div>
  </div>
</template>