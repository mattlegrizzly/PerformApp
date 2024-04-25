<script setup lang="ts">
import NavMenu from '../../components/NavMenu.vue'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import '@/assets/base.css'
import { get, post, put, del } from '@/lib/callApi'
import type IERequestOptions from '@/types/request'
import NavButton from '@/components/NavButton.vue'
import AlertComponents from '@/components/AlertComponents.vue'
import router from '@/router'
const routerNav = useRoute()

const materials = ref([])
const sports = ref([])

//Old Value
const name = ref('')
const description = ref('')
const steps = ref([])
const materials_selected = ref([])
const init_materials = ref([])
const sport_selected = ref([])
const inis_sports = ref([])
const image_url = ref(new File([], '', undefined))
const image_src = ref('')

const alertErr = ref(false)
const error_message = ref('')
const error_title = ref('')

const onChangeInput = (e: any) => {
  const file = e.target.files[0]
  if (!file) return

  image_url.value = file
  // Convertir l'image en URL de données
  const reader = new FileReader()
  reader.onload = (e) => {
    image_src.value = e.target?.result as string
  }
  reader.readAsDataURL(file)
}

const sendData = async () => {
  const id = routerNav.params.exercise_id
  const option = {
    body: {
      id: id,
      name: name.value,
      description: description.value,
      video: 'zqdz',
      material_ids: [materials_selected.value],
      sports_ids: [sport_selected.value]
    }
  } as IERequestOptions
  put('/admin/exercises/' + id + '/', option, true, true).then((res) => {
    if (res.status > 300) {
      const keys = Object.keys(res.data)
      for (let i = 0; i < keys.length; i++) {
        error_message.value += keys[i] + ' : ' + res.data[keys[i]] + '\n\n'
      }
      alertErr.value = true
      error_title.value = 'Modification Error'
    } else {
      router.push('/exercises/show/' + id + '/')
    }
  })

  for (const step of steps.value) {
    const option = {
      body : {
        text : step.text,
        exercise : id
       }
    }
    put('/admin/steps/'+step.id +'/', option, true, false)
  }
}

const getMaterial = async () => {
  const id = routerNav.params.exercise_id
  const res = await get('/admin/exercises/' + id + '/')
  if (res.status === 404) {
    error_title.value = 'Error while retrieve exercises id ' + id
    error_message.value = res.data.detail
    alertErr.value = true
  } else {
    name.value = await res.name
    description.value = await res.description
    image_src.value = await res.pictures
    init_materials.value = await res.material_exercise
    inis_sports.value = await res.sports_exercise
    steps.value = await res.steps_exercise
    for (let elem of init_materials.value) {
      //@ts-expect-error
      materials_selected.value.push(elem.material.id)
    }
    for (let elem of inis_sports.value) {
      //@ts-expect-error
      sport_selected.value.push(elem.sport.id)
    }
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
  const id = routerNav.params.exercise_id
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
    if (steps_res.status === 404) {
      error_title.value = 'Error while retrieve sports'
      error_message.value = add_res.data.detail
      alertErr.value = true
    } else {
      steps.value = steps_res
      console.log(steps.value)
    }
  }
}

onMounted(() => {
  getMaterial()
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
        <v-text-field v-model="name" label="Nom du matériel * " variant="filled"></v-text-field>
      </div>
      <div class="inputFormDiv">
        <v-textarea
          label="Description *"
          name="input-7-1"
          v-model="description"
          variant="filled"
          auto-grow
        ></v-textarea>
      </div>
      <div class="inputFormDiv">
        <v-file-input
          label="Photo du matériel"
          prepend-icon="mdi-camera"
          variant="filled"
          v-model="image_url"
          @change="onChangeInput($event)"
        ></v-file-input>
      </div>
      <div class="imageDiv">
        <v-img :width="300" aspect-ratio="16/9" cover :src="image_src"></v-img>
      </div>
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
      <div id="steps" v-for="(element, index) in steps" :key="index">
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
