<script setup lang="ts">
import NavMenu from '../../components/NavMenu.vue'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import '@/assets/base.css'
import { get, put } from '@/lib/callApi'
import type IERequestOptions from '@/types/request'
import NavButton from '@/components/NavButton.vue'

const router = useRoute()

const name = ref('')
const description = ref('')
const image_url = ref(new File([], '', undefined))
const image_src = ref('')

const alertErr = ref(false)
const alertSuc = ref(false)
const error_message = ref('')
const success_message = ref('error')

const closePopup = () => {
  alertErr.value = false
  alertSuc.value = false
}

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
  const id = router.params.material_id;
  const option = {
    body: {
      name: name.value,
      description: description.value,
      pictures: image_url.value
    }
  } as IERequestOptions
  const res = await put('/admin/materials/' + id + '/', option, true, true);
  console.log(res);
}

const getMaterial = async () => {
    const id = router.params.material_id
    const res = await get('/admin/materials/' + id + '/')
    console.log(res)
    name.value = await res.name
    description.value = await res.description
    image_src.value = await res.pictures
    const pictures_array = res.pictures.split('/')
    console.log()
    let response = await fetch(image_src.value);
    let data = await response.blob();
    let metadata = {
      type: 'image/'+pictures_array[5].split('.')[1]
    };
    let file = new File([data], pictures_array[5], metadata);
    image_url.value = file;
    if (!file) return

    image_url.value = file
    // Convertir l'image en URL de données
    const reader = new FileReader()
    reader.onload = (e) => {
      image_src.value = e.target?.result as string
    }
    reader.readAsDataURL(file)
  }

onMounted(() => {
  getMaterial();
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
</style>

<template lang="">
  <NavMenu />
  <v-alert
    :model-value="alertErr"
    border="start"
    close-label="Close Alert"
    color="error"
    title="Erreur de connexion"
    closable
    @click:close="closePopup"
  >
    {{ error_message }}
  </v-alert>
  <v-alert
    :model-value="alertSuc"
    border="start"
    close-label="Close Alert"
    color="success"
    title="Matériel ajouté"
    closable
    @click:close="closePopup"
  >
    {{ success_message }}
  </v-alert>
  <div class="mainWrapper">
    <NavButton class="returnBack" :text="'Retour'" :url="'/materials'" />
    <h1>Ajouter un Matériel</h1>
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

      <div class="buttonWrapper">
        <button @click="sendData(false)">Modifier</button>
      </div>
    </form>
  </div>
  <RouterView />
</template>
