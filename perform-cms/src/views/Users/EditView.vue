<script setup lang="ts">
import NavMenu from '../../components/NavMenu/NavMenu.vue'
import { ref, onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import '@/assets/base.css'
import { patch, get } from '@/lib/callApi'
import type IERequestOptions from '@/types/request'
import router from '@/router'
import NavButton from '@/components/NavButton/NavButton.vue'
import { useRoute } from 'vue-router'

const user : any = ref({})

const navRoute = useRoute()
const alertErr = ref(false)
const alertSuc = ref(false)
const error_message = ref('')
const success_message = ref('error')

const isFormData = ref(false)

const gender = ref([
  { id: 'male', value: 'Homme' },
  { id: 'female', value: 'Femme' },
  { id: 'other', value: 'Autre' }
])
const image_url = ref(new File([], '', undefined))
const image_src = ref('')

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

const sendData = (quitForm: boolean) => {
  const id = navRoute.params.user_id
  const option = {
    body: {
      last_name: user.value.last_name,
      first_name: user.value.first_name,
      gender: user.value.gender,
      age: user.value.age,
      size: user.value.size
    }
  } as IERequestOptions
  if (user.value.profile_picture) {
    const splitUser = user.value.profile_picture.split('/')
    const nameFile = splitUser[splitUser.length - 1]
    if (image_url.value.name !== nameFile) {
      option.body['profile_picture'] = image_url.value
      isFormData.value = true
    } else {
      isFormData.value = false
    }
  } else {
    if(image_url.value) {
      option.body['profile_picture'] = image_url.value
      isFormData.value = true
    } else {
      isFormData.value = false
    }
  }
  patch('/admin/users_all/' + id + '/', option, true, isFormData.value)
    .then((res) => {
      error_message.value = ''
      success_message.value = ''
      if (res.status) {
        const keys = Object.keys(res.data)
        for (let i = 0; i < keys.length; i++) {
          error_message.value += keys[i] + ' : ' + res.data[keys[i]] + '\n\n'
        }
        throw Error()
      } else {
        if (quitForm) {
          router.push('/users/show/' + id + '/?edit=true')
        } else {
          success_message.value = 'Vous avez modifiez : ' + res.first_name + ' ' + res.last_name
          user.value = {}
          image_url.value = new File([], '', undefined)
          image_src.value = ''
          alertSuc.value = true
        }
      }
    })
    .catch((error) => {
      alertErr.value = true
    })
}

const getUser = async () => {
  const id = navRoute.params.user_id
  try {
    const res = await get('/admin/users_all/' + id + '/')
    if (res.status > 300) {
      //error_title.value = 'Error while retrieve sports id ' + id
      error_message.value = res.data.detail
      alertErr.value = true
    } else {
      user.value = res
      image_src.value = await res.profile_picture
      const pictures_array = res.profile_picture.split('/')
      let response = await fetch(image_src.value)
      let data = await response.blob()
      let metadata = {
        type: 'image/' + pictures_array[5].split('.')[1]
      }
      let file = new File([data], pictures_array[5], metadata)
      image_url.value = file
      if (!file) return

      image_url.value = file
      // Convertir l'image en URL de données
      const reader = new FileReader()
      reader.onload = (e) => {
        image_src.value = e.target?.result as string
      }
      reader.readAsDataURL(file)
    }
  } catch (error: any) {
    error_message.value = error.data.status
    alertErr.value = true
  }
}

onMounted(() => {
  getUser()
})
</script>
<style>
.inputFormDiv {
  width: 100% !important;
}
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
    title="Sport ajouté"
    closable
    @click:close="closePopup"
  >
    {{ success_message }}
  </v-alert>
  <div class="mainWrapper">
    <NavButton class="returnBack" :text="'Retour'" :url="'/users'" prepend-icon="mdi-arrow-left" />
    <h1>Editer un Utilisateur</h1>
    <form @submit.prevent="submit">
      <div class="inputFormDiv">
        <v-text-field v-model="user.last_name" label="Nom " variant="filled"></v-text-field>
        <v-text-field v-model="user.first_name" label="Pénom " variant="filled"></v-text-field>
      </div>
      <div class="inputFormDiv">
        <v-text-field v-model="user.size" label="Taille " variant="filled"></v-text-field>
      </div>
      <div class="inputFormDiv">
        <v-text-field label="Poids" v-model="user.weight"></v-text-field>
      </div>
      <div class="inputFormDiv">
        <v-text-field label="Age" v-model="user.age"></v-text-field>
      </div>
      <div class="inputFormDiv">
        <v-select
          label="Select"
          :items="gender"
          v-model="user.gender"
          item-title="value"
          item-value="id"
        ></v-select>
      </div>
      <div class="inputFormDiv">
        <v-file-input
          label="Photo de profil utilisateur"
          prepend-icon="mdi-camera"
          variant="filled"
          v-model="image_url"
          @change="onChangeInput($event)"
        ></v-file-input>
      </div>
      <div class="imageDiv">
        <v-img :height="100" aspect-ratio="16/9" :src="image_src"></v-img>
      </div>
      <div class="buttonWrapper">
        <button class="return_btn" @click="sendData(true)">Modifier</button>
      </div>
    </form>
  </div>
</template>
