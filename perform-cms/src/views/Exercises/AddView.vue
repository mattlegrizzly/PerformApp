<script setup lang="ts">
import NavMenu from '../../components/NavMenu/NavMenu.vue'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import '@/assets/base.css'
import { get, post, put, patch, del } from '@/lib/callApi'
import type IERequestOptions from '@/types/request'
import type Step from '@/types/types'
import NavButton from '@/components/NavButton/NavButton.vue'
import AlertComponents from '@/components/AlertComponents/AlertComponents.vue'
import router from '@/router'
import { nanoid } from 'nanoid'
import BodyComponent from '@/components/BodyComponent/BodyComponent.vue'
import './exercises.css'
const routerNav = useRoute()

const materials = ref([])
const sports = ref([])
const muscles = ref([])
const videoController = ref(document.createElement('video'))

const exercise: any = ref({})
const steps_exercise: any = ref([])

const materials_selected = ref([])
const sport_selected = ref([])
const muscle_selected = ref([])
const video_src = ref('')

const alertErr = ref(false)
const error_message = ref('')
const error_title = ref('')

const dataToRetrieve = [
  {
    link: '/admin/materials/all/',
    array: materials
  },
  {
    link: '/admin/sports/all/',
    array: sports
  },
  {
    link: '/admin/workzones/all/',
    array: muscles
  }
]

const onChangeInput = (file: File) => {
  exercise.value.video = file
  video_src.value = URL.createObjectURL(file)
  videoController.value.load()
}

const sendData = async () => {
  const id = routerNav.params.exercise_id
  const option = {
    body: {
      name: exercise.value.name,
      description: exercise.value.description,
      material_ids: materials_selected.value,
      sports_ids: sport_selected.value
    }
  } as IERequestOptions
  if (exercise.value.video) {
    option.body.video = exercise.value.video
  }
  post('/admin/exercises/', option, true, true).then((res) => {
    if (res.status > 300) {
      const keys = Object.keys(res.data)
      for (let i = 0; i < keys.length; i++) {
        error_message.value += keys[i] + ' : ' + res.data[keys[i]] + '\n\n'
      }
      alertErr.value = true
      error_title.value = 'Modification Error'
    } else {
      const id = res.id
      //router.push('/exercises/show/' + id + '/')
      steps_exercise.value.map((step : {
        text : string,
        id : number
      }) => {
        const stepToPush = {
          body: {
            exercise: id,
            text: step.text
          }
        }
        res = post('/admin/steps/', stepToPush, true)
      })

      materials_selected.value.map((material) => {
        const materialToPush = {
          body: {
            exercise: id,
            material: material
          }
        }
        res = post('/admin/exercisematerials/', materialToPush, true)
      })

      sport_selected.value.map((sport) => {
        const sportToPush = {
          body: {
            exercise: id,
            sport: sport
          }
        }
        res = post('/admin/exercisesports/', sportToPush, true)
      })

      muscle_selected.value.map((muscle) => {
        console.log(muscle)
        const sportToPush = {
          body: {
            exercise: id,
            zone: muscle
          }
        }
        res = post('/admin/exercisezones/', sportToPush, true)
      })

      router.push('/exercises/show/' + id + '/?edit=true')
    }
  })
}

const getExercise = async () => {
  dataToRetrieve.map(async (elem) => {
    const res = await get(elem.link, { body: {} }, true)
    if (res.status === 404) {
      error_title.value = 'Error while retrieve materials'
      error_message.value = res.data.detail
      alertErr.value = true
    } else {
      elem.array.value = res
    }
  })
}

const addStep = async () => {
  const id = nanoid()
  const step = {
    id,
    text: 'Saisissez une étape'
  }
  steps_exercise.value.push(step)
}

const removeStep = async (id: number) => {
  for (const [index, step] of steps_exercise.value.entries()) {
    if (step.id == id) {
      steps_exercise.value.splice(index, 1)
    }
  }
}

const setMuscle = (key: string, action: string, muscle_selected : any) => {
    if (action === 'add') {
      const findKey =
        muscle_selected.filter(function (element : any) {
          return element === key
        }).length == 0
      console.log(findKey)
      if (findKey) {
        muscle_selected.push(key)
      }
    } else {
      // Trouver l'index de la valeur à supprimer
      const index = muscle_selected.indexOf(key)
  
      if (index !== -1) {
        // Supprimer la valeur à l'index trouvé
        muscle_selected.splice(index, 1)
      }
    }
  }

onMounted(() => {
  getExercise()
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
    />
    <NavButton
      class="returnBack"
      :text="'Retour'"
      :url="'/exercises'"
      :back="'back'"
      prepend-icon="mdi-arrow-left"
    />
    <h1>Ajouter un Exercise</h1>
    <form @submit.prevent="submit">
      <div class="inputFormDiv">
        <v-text-field
          v-model="exercise.name"
          label="Nom du matériel * "
          variant="filled"
        ></v-text-field>
      </div>
      <div class="inputFormDiv">
        <v-textarea
          label="Description *"
          name="input-7-1"
          v-model="exercise.description"
          variant="filled"
          auto-grow
        ></v-textarea>
      </div>
      <div class="inputFormDiv">
        <v-file-input
          label="Video d'execution"
          prepend-icon="mdi-video"
          variant="filled"
          type="file"
          accept="video/*"
          v-model="video_url"
          @update:modelValue="onChangeInput($event)"
        ></v-file-input>
      </div>
      <video
        ref="videoController"
        id="player"
        playsinline
        controls
        data-poster="/path/to/poster.jpg"
      >
        <source :src="video_src" type="video/mp4" />
      </video>
      <h2>Zones de travail</h2>
      <BodyComponent
        :height="400"
        :muscleSelected="muscle_selected"
        :setMuscleSelected="setMuscle"
        :viewOnly="'add'"
      />
      <MultiSelectComponent
        :models="muscle_selected"
        :items="muscles"
        hint="Sélectionnez les muscles utilisés"
        value="code"
        title="name"
      />
      <h2>Sports</h2>
      <MultiSelectComponent
        :models="sport_selected"
        :items="sports"
        hint="Sélectionnez le sport utilisé"
        value="id"
        title="name"
      />
      <h2>Matériels</h2>
      <MultiSelectComponent
        :models="materials_selected"
        :items="materials"
        hint="Sélectionnez le matériel utilisé"
        value="id"
        title="name"
      />
      <h2>Instructions</h2>
      <div id="steps" v-for="(element, index) in steps_exercise" :key="index">
        <v-text-field
          v-model="element.text"
          :label="'Instruction ' + (index + 1)"
          variant="filled"
        ></v-text-field>
        <v-btn icon="mdi-delete" @click="removeStep(element.id)"> </v-btn>
      </div>
      <v-btn @click="addStep()" prepend-icon="mdi-plus"> Ajouter une instruction</v-btn>
      <div class="buttonWrapper">
        <button @click="sendData(false)">Ajouter</button>
      </div>
    </form>
  </div>
</template>
