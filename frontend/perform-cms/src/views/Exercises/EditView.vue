<script setup lang="ts">
import NavMenu from '../../components/NavMenu/NavMenu.vue'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import '@/assets/base.css'
import { get, post, put, patch, del } from '@/lib/callApi'
import type IERequestOptions from '@/types/request'
import NavButton from '@/components/NavButton/NavButton.vue'
import AlertComponents from '@/components/AlertComponents/AlertComponents.vue'
import router from '@/router'
import { nanoid } from 'nanoid'
import BodyComponent from '@/components/BodyComponent/BodyComponent.vue'
import './exercises.css'
import type { Step, Muscle } from '@/types/types'
import DeleteModalComponent from '@/components/DeleteModalComponent/DeleteModalComponent.vue'
const routerNav = useRoute()

//Data qui vont être utilisé dans les menus déroulants
const muscles = ref([])
const materials = ref([])
const sports = ref([])

const api_url = import.meta.env.VITE_API_URL

const videoController = ref(document.createElement('video'))

const const_exercice: any = ref()
const exercise: any = ref({})

const muscle_selected: any = ref([])
const file = ref()
const materials_selected = ref([])
const sport_selected = ref([])
const video_url = ref('')
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
  let isFormData = false
  const option = {
    body: {
      name: exercise.value.name,
      material_ids: materials_selected.value,
      sports_ids: sport_selected.value,
      muscles_id: muscle_selected.value
    }
  } as IERequestOptions
  if (const_exercice.value.video !== exercise.value.video) {
    option.body['video'] = exercise.value.video
    isFormData = true
  }
  patch('/admin/exercises/' + id + '/', option, true, isFormData).then((res) => {
    if (res.status > 300) {
      const keys = Object.keys(res.data)
      for (let i = 0; i < keys.length; i++) {
        error_message.value += keys[i] + ' : ' + res.data[keys[i]] + '\n\n'
      }
      alertErr.value = true
      error_title.value = 'Modification Error'
    } else {
      //router.push('/exercises/show/' + id + '/')
      let startStep = const_exercice.value.steps_exercise
      let endStep = exercise.value.steps_exercise
      const newStep = endStep.filter(
        (step: Step) => !startStep.find((step_: Step) => step_.id === step.id)
      )
      const modified = startStep.filter((step: Step) =>
        endStep.find((step_: Step) => step_.id === step.id)
      )
      const deleted = startStep.filter(
        (step: Step) => !endStep.find((step_: Step) => step_.id === step.id)
      )

      newStep.map((step: Step) => {
        const stepToPush = {
          body: {
            exercise: id,
            text: step.text
          }
        }
        res = post('/admin/steps/', stepToPush, true)
      })

      deleted.map((step: Step) => {
        res = del('/admin/steps/' + step.id + '')
      })

      modified.map((step: Step) => {
        const elem = endStep.find((step_: Step) => step_.id == step.id)
        if (elem.text !== step.text) {
          const options = {
            body: {
              text: elem.text
            }
          }
          res = patch('/admin/steps/' + elem.id + '/', options, true)
        }
      })

      router.push('/exercises/show/' + id + '/?edit=true')
    }
  })
}

const setMuscleSelected = (key: string, action: string) => {
  if (action === 'add') {
    const findKey =
      muscle_selected.value.filter(function (element: string) {
        return element === key
      }).length == 0
    if (findKey) {
      muscle_selected.value.push(key)
    }
  } else {
    // Trouver l'index de la valeur à supprimer
    var index = muscle_selected.value.indexOf(key)

    if (index !== -1) {
      // Supprimer la valeur à l'index trouvé
      muscle_selected.value.splice(index, 1)
    }
  }
}

const getExercise = async () => {
  const id = routerNav.params.exercise_id
  const res = await get('/admin/exercises/' + id + '/')
  if (res.status === 404) {
    error_title.value = 'Error while retrieve exercises id ' + id
    error_message.value = res.data.detail
    alertErr.value = true
  } else {
    const_exercice.value = JSON.parse(JSON.stringify(await res))
    exercise.value = JSON.parse(JSON.stringify(await res))
    const temp_muscle: Array<string> = []
    exercise.value.zone_exercises.map((muscle: Muscle) => {
      temp_muscle.push(muscle.zone.code)
    })
    muscle_selected.value = temp_muscle
    for (let elem of exercise.value.material_exercise) {
      //@ts-expect-error
      materials_selected.value.push(elem.material.id)
    }
    for (let elem of exercise.value.sports_exercise) {
      //@ts-expect-error
      sport_selected.value.push(elem.sport.id)
    }
    video_url.value = await exercise.value.video
    if (res.video) {
      const video_array = res.video.split('/')
      await fetch(video_url.value).then((response) => {
        response.blob().then((data) => {
          if (video_array[1] == '') {
            let metadata = {
              type: 'video/' + video_array[3].split('.')[1]
            }
            file.value = new File([data], video_array[3], metadata)
            video_url.value = file.value
          }
          video_src.value = api_url + exercise.value.video
          videoController.value.load()
        })
      })
    }
  }
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
    text: ''
  }
  exercise.value.steps_exercise.push(step)
}

const removeStep = async (id: number) => {
  for (const [index, step] of exercise.value.steps_exercise.entries()) {
    if (step.id == id) {
      exercise.value.steps_exercise.splice(index, 1)
    }
  }
}

onMounted(() => {
  getExercise()
})
</script>
<style></style>

<template lang="">
  <NavMenu />
  <div class="mainWrapper">
    <AlertComponents
      :message_alert="error_message"
      :type="'error'"
      :title="error_title"
      :alertValue="alertErr"
    />
    <div class="headerBtns">
      <NavButton
        class="returnBack"
        :text="'Retour'"
        :url="'/exercises'"
        :back="'back'"
        prepend-icon="mdi-arrow-left"
      />
      <DeleteModalComponent
        :item="exercise.name"
        url="/admin/exercises"
        :id="routerNav.params.exercise_id"
        list="exercises"
      />
    </div>
    <h1>Editer un Exercise</h1>
    <form @submit.prevent="submit">
      <div class="inputFormDiv">
        <v-text-field
          v-model="exercise.name"
          label="Nom du matériel * "
          variant="filled"
        ></v-text-field>
      </div>
      <div class="inputFormDiv">
        <v-file-input
          label="Video d'execution"
          prepend-icon="mdi-video"
          variant="filled"
          type="file"
          accept="video/mp4"
          v-model="video_url"
          multiple
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
      <h2>Sports</h2>
      <v-select
        v-model="sport_selected"
        :items="sports"
        hint="Sélectionnez le sport utilisé"
        item-title="name"
        item-value="id"
        label="Select"
        multiple
        persistent-hint
        single-line
      >
      </v-select>
      <h2>Matériels</h2>
      <v-select
        v-model="materials_selected"
        :items="materials"
        hint="Sélectionnez le matériel utilisé"
        item-title="name"
        item-value="id"
        label="Select"
        multiple
        persistent-hint
        single-line
      >
      </v-select>
      <h2 class="showTitle">Muscles</h2>
      <BodyComponent
        :height="400"
        :muscleSelected="muscle_selected"
        :setMuscleSelected="setMuscleSelected"
        :viewOnly="'edit'"
      />
      <v-select
        v-model="muscle_selected"
        :items="muscles"
        hint="Sélectionnez les muscles utilisés"
        item-title="name"
        item-value="code"
        label="Select"
        multiple
        persistent-hint
        single-line
      ></v-select>
      <h2>Etapes</h2>
      <div id="steps" v-for="(element, index) in exercise.steps_exercise" :key="index">
        <v-text-field
          v-model="element.text"
          :label="'Etape ' + (index + 1)"
          variant="filled"
        ></v-text-field>
        <v-btn icon="mdi-delete" @click="removeStep(element.id)"> </v-btn>
      </div>
      <v-btn @click="addStep()" prepend-icon="mdi-plus"> Ajouter une étape </v-btn>
      <div class="buttonWrapper">
        <button @click="sendData(false)">Modifier</button>
      </div>
    </form>
  </div>
</template>
