<script setup lang="ts">
import NavMenu from '../../components/NavMenu.vue'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import '@/assets/base.css'
import { get, post, put, patch, del } from '@/lib/callApi'
import type IERequestOptions from '@/types/request'
import NavButton from '@/components/NavButton.vue'
import AlertComponents from '@/components/AlertComponents.vue'
import router from '@/router'
import { nanoid } from 'nanoid'

const routerNav = useRoute()

const materials = ref([])
const sports = ref([])
const videoController = ref(document.createElement('video'))

const const_exercice: any = ref()
const exercise: any = ref({})

const file = ref()
const materials_selected = ref([])
const sport_selected = ref([])
const video_url = ref('')
const video_src = ref('')

const alertErr = ref(false)
const error_message = ref('')
const error_title = ref('')

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
  if (const_exercice.value.video !== exercise.value.video) {
    option.body['video'] = exercise.value.video
  }
  patch('/admin/exercises/' + id + '/', option, true, true).then((res) => {
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
      const newStep = endStep.filter((step) => !startStep.find((step_) => step_.id === step.id))
      const modified = startStep.filter((step) => endStep.find((step_) => step_.id === step.id))
      const deleted = startStep.filter((step) => !endStep.find((step_) => step_.id === step.id))

      console.log(modified)
      newStep.map((step) => {
        const stepToPush = {
          body: {
            exercise: id,
            text: step.text
          }
        }
        res = post('/admin/steps/', stepToPush, true)
      })

      deleted.map((step) => {
        res = del('/admin/steps/' + step.id + '')
      })

      modified.map((step) => {
        const elem = endStep.find((step_) => step_.id == step.id)
        if(elem.text !== step.text){
          const options = {
            body : {
              text: elem.text
            }
          }
          res = patch('/admin/steps/'+elem.id+'/',options , true)
        }
      })
    }
  })
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
    for (let elem of exercise.value.material_exercise) {
      //@ts-expect-error
      materials_selected.value.push(elem.material.id)
    }
    for (let elem of exercise.value.sports_exercise) {
      //@ts-expect-error
      sport_selected.value.push(elem.sport.id)
    }
    video_url.value = await exercise.value.video
    const video_array = res.video.split('/')
    console.log(video_array)
    await fetch(video_url.value).then((response) => {
      response.blob().then((data) => {
        if (video_array[1] == '') {
          let metadata = {
            type: 'video/' + video_array[3].split('.')[1]
          }
          file.value = new File([data], video_array[3], metadata)
          video_url.value = file.value
        }
        video_src.value = 'http://127.0.0.1:8000' + exercise.value.video
        videoController.value.load()
      })
    })
  }
  const res_materials = await get('/materials')
  if (res_materials.status === 404) {
    error_title.value = 'Error while retrieve materials'
    error_message.value = res.data.detail
    alertErr.value = true
  } else {
    materials.value = res_materials.results
  }
  const res_sports = await get('/sports')
  if (res_materials.status === 404) {
    error_title.value = 'Error while retrieve sports'
    error_message.value = res.data.detail
    alertErr.value = true
  } else {
    sports.value = res_sports.results
  }
}

const addStep = async () => {
  const id = nanoid()
  const step = {
    id,
    text: ''
  }
  exercise.value.steps_exercise.push(step)

  /* const id = routerNav.params.exercise_id
  const option = {
    body: {
      exercise: id,
      text: 'text'
    }
  }
  const add_res = await post('/admin/steps/', option, true, false)
  if (add_res.status === 404) {
    error_title.value = 'Error while retrieve sports'
    error_message.value = add_res.data.detail
    alertErr.value = true
  } else {
    const steps_res = await get('/admin/steps/exercise/' + id + '/')
    if (steps_res.status > 300) {
      error_title.value = 'Error while retrieve sports'
      error_message.value = add_res.data.detail
      alertErr.value = true
    } else {
      steps.value = steps_res
    }
  } */
}

//LISTER ICI POUR SUPPRIMER
const removeStep = async (id: number) => {
  console.log(id)
  for (const [index, step] of exercise.value.steps_exercise.entries()) {
    if (step.id == id) {
      exercise.value.steps_exercise.splice(index, 1)
    }
  }
  /* const id_exercise = routerNav.params.exercise_id

  const res_delet = await del('/admin/steps/' + id + '/')
  if (res_delet.status > 300) {
    error_title.value = 'Error while delete step'
    error_message.value = 'Not deleted'
    alertErr.value = true
  } else {
    const steps_res = await get('/admin/steps/exercise/' + id_exercise + '/')
    steps.value = steps_res
  } */
}

onMounted(() => {
  getExercise()
})
</script>
<style>
.return_btn {
  background-color: white !important;
  color: var(--primary-blue) !important;
  border: 1px solid var(--primary-blue);
  transition: 0.3s;
}

.return_btn:hover {
  transition: 0.3s;
  background-color: var(--primary-blue) !important;
  color: white !important;
}

.returnBack {
  margin-top: 10px;
}

#steps {
  display: flex;
}

#steps button {
  margin-left: 10px;
}
</style>

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
      <h2>Sports</h2>
      <v-select
        v-model="sport_selected"
        :items="sports"
        hint="Sélectionnez le sport utilisé"
        item-title="name"
        item-value="id"
        mulitple
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
        mulitple
        label="Select"
        multiple
        persistent-hint
        single-line
      >
      </v-select>
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
  <RouterView />
</template>
