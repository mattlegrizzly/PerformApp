<script setup lang="ts">
import NavMenu from '../../components/NavMenu/NavMenu.vue'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import '@/assets/base.css'
import { get, put } from '@/lib/callApi'
import type IERequestOptions from '@/types/request'
import NavButton from '@/components/NavButton/NavButton.vue'
import AlertComponents from '@/components/AlertComponents/AlertComponents.vue'
import DeleteModalComponent from '@/components/DeleteModalComponent/DeleteModalComponent.vue'
import router from '@/router'

const routerNav = useRoute()

const name = ref('')

const alertErr = ref(false)
const error_message = ref('')
const error_title = ref('')

const setAlertValue = (type: string) => {
  if (type === "error") {
    alertErr.value = false
  } else {

  }
}

const sendData = async () => {
  const id = routerNav.params.sport_id
  const option = {
    body: {
      name: name.value
    }
  } as IERequestOptions
  put('/admin/sports/' + id + '/', option, true, true).then((res) => {
    if (res.status > 300) {
      const keys = Object.keys(res.data)
      for (let i = 0; i < keys.length; i++) {
        error_message.value += keys[i] + ' : ' + res.data[keys[i]] + '\n\n'
      }
      alertErr.value = true
      error_title.value = "Erreur à la modification"
    } else {
      router.push('/sports/show/' + id + '/?edit=true')
    }
  })
}

const getSport = async () => {
  const id = routerNav.params.sport_id
  try {
    const res = await get('/admin/sports/' + id + '/')
    if (res.status === 404) {
      error_title.value = 'Erreur à la récupération du sport avec id ' + id
      error_message.value = res.data.detail
      alertErr.value = true
    }
    name.value = await res.name
  } catch (error: any) {
    error_message.value = error.data.status
    alertErr.value = true
  }
}

onMounted(() => {
  getSport()
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
    <AlertComponents
      :message_alert="error_message"
      :type="'error'"
      :title="error_title"
      :alertValue="alertErr"
      :setAlertValue="setAlertValue"
    />
    <div class="headerBtns">
      <NavButton class="returnBack" :text="'Retour'" :url="'/sports'" :back="'back'" />

      <DeleteModalComponent
        :item="name"
        url="/admin/sports"
        :id="routerNav.params.sport_id"
        list="sports"
      />
    </div>
    <h1>Editer un sport</h1>
    <form @submit.prevent="submit">
      <div class="inputFormDiv">
        <v-text-field v-model="name" label="Nom du sport * " variant="filled"></v-text-field>
      </div>

      <div class="buttonWrapper">
        <button @click="sendData(false)">Modifier</button>
      </div>
    </form>
  </div>
</template>
