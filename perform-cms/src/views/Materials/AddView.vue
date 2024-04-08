<script setup lang="ts">
import NavMenu from '../../components/NavMenu.vue'
import { ref, onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import '@/assets/base.css'
import { post } from '@/lib/callApi'
import type IERequestOptions from '@/types/request'
import router from '@/router'

const name = ref('');
const description = ref('');

const alertErr = ref(false)
const alertSuc = ref(false)
const error_message = ref('');
const success_message = ref('error');

const closePopup = () => {
  alertErr.value = false
  alertSuc.value = false
}

const sendData = (quitForm : boolean) => {
  const option = {
    body: { 
      name: name.value, 
      description: description.value, 
      pictures:null 
  }
  } as IERequestOptions;
  post('/admin/materials/', option, true).then((res) => {
    error_message.value = ""
    success_message.value = ""
    if(res.status){
      const keys = Object.keys(res.data);
       for(let i = 0; i < keys.length; i ++){
        console.log(keys[i] , ' : ' , res.data[keys[i]])
        error_message.value += keys[i] + ' : ' + res.data[keys[i]] + '\n\n';  
      } 
      throw Error();
    } else {
      name.value = '';
      description.value = '';
      if(quitForm) {
        router.push('/materials')
      } else {
        success_message.value = 'Vous avez ajoutez : ' + res.name;
        alertSuc.value = true;
      }
    }
  }).catch((error) => {
    alertErr.value = true;
    console.log(error)
  });
};
</script>
<style>
.return_btn {
  background-color: white !important;
  color : var(--primary-blue) !important;
  border : 1px solid var(--primary-blue);
  transition: 0.3s;
}

.return_btn:hover {
  transition: 0.3s;
  background-color: var(--primary-blue) !important;
  color : white!important;
}
</style>

<template lang="">
  <NavMenu />
  <v-alert
    :model-value="alertErr"
    border="start"
    close-label="Close Alert"
    color='error'
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
    color= 'success'
    title="Matériel ajouté"
    closable
    @click:close="closePopup"
  >
    {{ success_message }}
  </v-alert>
  <div class="mainWrapper">
    <h1>Ajouter un Matériel</h1>
    <form @submit.prevent="submit">
      <div class="inputFormDiv">
        <span>Nom du matériel * </span>
        <input required v-model="name" placeholder="Box" />
      </div>
      <div class="inputFormDiv">
        <span>Description *</span>
        <input required v-model="description" placeholder="Box" />

      </div>
      <div class="inputFormDiv">
        <span>Photo</span>
        <input type="file" placeholder="*****" />
      </div>
      <div class="buttonWrapper">
        <button @click="sendData(false)">Créer et continuer</button>
        <button class="return_btn" @click="sendData(true)">Créer</button>
      </div>
    </form>
  </div>
  <RouterView />
</template>
