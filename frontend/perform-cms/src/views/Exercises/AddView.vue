<script setup lang="ts">
import NavMenu from '../../components/NavMenu/NavMenu.vue'
import { ref, onMounted } from 'vue'
import '@/assets/base.css'
import { get, post } from '@/lib/callApi'
import type IERequestOptions from '@/types/request'
import NavButton from '@/components/NavButton/NavButton.vue'
import AlertComponents from '@/components/AlertComponents/AlertComponents.vue'
import { nanoid } from 'nanoid'
import type Muscle from '@/types/types'
//@ts-expect-error
import { BodyComponent } from 'perform-body-component-lib'
import 'perform-body-component-lib/style.css'
import './exercises.css'
import router from '@/router'
import draggable from 'vuedraggable'

const materials = ref([])
const sports = ref([])
const muscles = ref([])
const videoController = ref(document.createElement('video'))

const exercise: any = ref({
  name: ''
})
const steps_exercise: any = ref([])

const adding = ref(false)

const materials_selected = ref([])
const temp_selected = ref([])
const sport_selected = ref([])
const muscle_selected: any = ref([])
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

const setAlertValue = (type: string) => {
  if (type === 'error') {
    alertErr.value = false
  } else {
  }
}


const onChangeInput = (file: Array<File>) => {
  if (file[0]) {
    exercise.value.video = file[0]
    if (file[0] && file[0].type.startsWith('video/')) {
      const videoURL = URL.createObjectURL(file[0]) // Créer un URL pour le fichier vidéo
      video_src.value = videoURL
      videoController.value.load()
    } else {
      console.error('Veuillez sélectionner un fichier vidéo valide.')
    }
  }
}

const updateOrder = () => {
  steps_exercise.value.forEach((step : any, index : number) => {
    step.order = index
  })
}

const moveUp = (index : number) => {
      if (index > 0) {
        const temp = steps_exercise.value[index];
        steps_exercise.value[index] = steps_exercise.value[index - 1];
        steps_exercise.value[index - 1] = temp;
        updateOrder();
      }
    };

    const moveDown = (index : number) => {
      if (index < steps_exercise.value.length - 1) {
        const temp = steps_exercise.value[index];
        steps_exercise.value[index] = steps_exercise.value[index + 1];
        steps_exercise.value[index + 1] = temp;
        updateOrder();
      }
    };

const sendData = async () => {
  adding.value = true
  console.log('adding ', adding.value)

  const option = {
    body: {
      name: exercise.value.name,
      material_ids: materials_selected.value,
      sports_ids: sport_selected.value
    }
  } as IERequestOptions
  if (exercise.value.video) {
    option.body.video = exercise.value.video
  }
  post('/admin/exercises/', option, true, true).then((res) => {
    setTimeout(() => {
      if (res.status > 300) {
        error_message.value = ''
        const keys = Object.keys(res.data)
        for (let i = 0; i < keys.length; i++) {
          error_message.value += keys[i] + ' : ' + res.data[keys[i]] + '\n\n'
        }
        alertErr.value = true
        error_title.value = "Erreur à l'ajout"
        adding.value = false
      } else {
        const id = res.id
        router.push('/exercises/show/' + id + '/')
        steps_exercise.value.map((step: { text: string; id: number, order: number }) => {
          const stepToPush = {
            body: {
              exercise: id,
              text: step.text,
              order: step.order
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

        muscle_selected.value.map((muscle: any) => {
          const sportToPush = {
            body: {
              exercise: id,
              zone: muscle.zone.code
            }
          }
          res = post('/admin/exercisezones/', sportToPush, true)
        })

        router.push('/exercises')
      }
    }, 1000)
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
      if (elem.link.includes('workzones')) {
        let array = [] as any
        res.map((elem: any) => {
          array.push({ zone: elem })
        })
        elem.array.value = array
        console.log(array)
      } else {
        elem.array.value = res
      }
    }
  })
}

const handleChange = (codes: any) => {
  // Mettez à jour temp_selected pour correspondre aux codes
  temp_selected.value = codes

  // Créez une nouvelle sélection en fonction des codes
  const newSelection = codes.map((code: any) =>
    muscles.value.find((muscle: any) => muscle.zone.code === code)
  )

  // Supprimez les muscles non sélectionnés de muscle_selected
  muscle_selected.value = muscle_selected.value.filter((muscle: any) =>
    codes.includes(muscle.zone.code)
  )

  // Ajoutez les nouveaux muscles sélectionnés à muscle_selected
  newSelection.forEach((muscle: any) => {
    if (!muscle_selected.value.some((m: any) => m.zone.code === muscle.zone.code)) {
      muscle_selected.value.push(muscle)
    }
  })
}

const addStep = async () => {
  const id = nanoid()
  const step = {
    id,
    text: ''
  }
  steps_exercise.value.push(step)
  updateOrder()
}

const removeStep = async (id: number) => {
  for (const [index, step] of steps_exercise.value.entries()) {
    if (step.id == id) {
      steps_exercise.value.splice(index, 1)
    }
  }
  updateOrder()

}

const setMuscle = (key: string, action: string) => {
  if (action === 'add') {
    const findKey =
      muscle_selected.value.filter(function (element: any) {
        return element.zone.code === key
      }).length == 0
    if (findKey) {
      muscle_selected.value.push(muscles.value.find((element: any) => element.zone.code == key))
    }
  } else {
    let index = muscle_selected.value.indexOf(key as any)
    muscle_selected.value.map((muscle: any) => {
      if (muscle.zone.code === key) {
        index = muscle_selected.value.indexOf(muscle)
      }
      if (index !== -1) {
        muscle_selected.value.splice(index, 1)
      }
    })
  }

  temp_selected.value = muscle_selected.value
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
      :setAlertValue="setAlertValue"
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
          label="Nom de l'exercice * "
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
      <h2>Zones de travail</h2>
      <BodyComponent
        :height="400"
        :muscleSelected="muscle_selected"
        :setMuscleSelected="setMuscle"
        :viewOnly="'add'"
      />
      <v-select
        v-model="temp_selected"
        :items="muscles"
        hint="Sélectionnez les muscles utilisés"
        item-title="zone.name"
        item-value="zone.code"
        label="Select"
        multiple
        @update:modelValue="handleChange"
      >
      </v-select>
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
      <h2>Instructions</h2>
      <draggable v-model="steps_exercise" item-key="id" @end="updateOrder">
      <template #item="{ element, index }">
        <div id="steps" class="step-item">
          <v-icon class="drag-handle" left>mdi-drag</v-icon>
          <v-text-field
            v-model="element.text"
            :label="'Instruction ' + (index + 1)"
            variant="filled"
          ></v-text-field>
          <v-btn icon="mdi-arrow-up" @click="moveUp(index)" :disabled="index === 0"></v-btn>
          <v-btn icon="mdi-arrow-down" @click="moveDown(index)" :disabled="index === steps_exercise.length - 1"></v-btn>
          <v-btn icon="mdi-delete" @click="removeStep(element.id)"></v-btn>
        </div>
      </template>
    </draggable>
    <v-btn @click="addStep()" prepend-icon="mdi-plus"> Ajouter une instruction</v-btn>
    <div class="buttonWrapper">
      <v-btn @click="sendData(false)" :disabled="adding">{{ adding ? 'Ajout en cours...' : 'Ajouter' }}</v-btn>
    </div>
    </form>
  </div>
</template>
