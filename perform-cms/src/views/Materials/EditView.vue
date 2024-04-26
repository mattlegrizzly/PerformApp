<script setup lang="ts">
import NavMenu from '../../components/NavMenu.vue'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import '@/assets/base.css'
import { get, put } from '@/lib/callApi'
import type IERequestOptions from '@/types/request'
import NavButton from '@/components/NavButton.vue'
import AlertComponents from '@/components/AlertComponents.vue'
import router from '@/router'
const routerNav = useRoute()

const name = ref('')
const description = ref('')
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
  const id = routerNav.params.material_id;
  const option = {
    body: {
      name: name.value,
      description: description.value,
      pictures: image_url.value
    }
  } as IERequestOptions
  put('/admin/materials/' + id + '/', option, true, true).then((res) => {
    if(res.status > 300) {
      const keys = Object.keys(res.data)
        for (let i = 0; i < keys.length; i++) {
          error_message.value += keys[i] + ' : ' + res.data[keys[i]] + '\n\n'
        }
        alertErr.value = true;
        error_title.value = "Modification Error"
    } else {
      router.push('/materials/show/' + id+ '/')
    }
  })
}

const getMaterial = async () => {
    const id = routerNav.params.material_id
    const res = await get('/admin/materials/' + id + '/')
    if(res.status === 404) {
        error_title.value = 'Error while retrieve sports id ' + id
        error_message.value = res.data.detail
        alertErr.value = true
      } else {
        name.value = await res.name
        description.value = await res.description
        image_src.value = await res.pictures
        const pictures_array = res.pictures.split('/')
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
  <div class="mainWrapper">
    <AlertComponents :message_alert='error_message' :type='"error"' :title='error_title' :alertValue="alertErr"/>
    <NavButton class="returnBack" :text="'Retour'" :url="'/materials'" :back='"back"' />
    <h1>Editer un Matériel</h1>
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
