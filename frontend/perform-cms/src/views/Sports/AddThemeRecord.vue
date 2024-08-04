<script setup lang="ts">
import NavMenu from '../../components/NavMenu/NavMenu.vue'
import { ref, onMounted, watch } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import '@/assets/base.css'
import { post, get } from '@/lib/callApi'
import type IERequestOptions from '@/types/request'
import { useRoute, useRouter } from 'vue-router'
import NavButton from '@/components/NavButton/NavButton.vue'
const route = useRoute()
const router = useRouter()

const unit_selected = ref('time')

watch(
  () => unit_selected,
  () => {
    console.log(unit_selected)
  }
)

const name = ref('')
const group_name = ref('')
const description = ref('')

const id = ref(0)
const alertErr = ref(false)
const alertSuc = ref(false)
const error_message = ref('')
const error_title = ref('')
const success_message = ref('error')
const dialog = ref(false)
const sport = ref('')
const groups = ref('')
const group_selected = ref(null)
const addToGroup = ref(false)

const closePopup = () => {
  alertErr.value = false
  alertSuc.value = false
}

const sendGroup = () => {
  const option = {
    name: group_name.value,
    sport: id.value
  }
  post('/record_group/', { body: option }, true).then((res) => {
    if (res.status > 300) {
      ;(error_title.value = 'Erreur de la création du Groupe, réessayez'),
        (error_message.value = res.data.detail)
      alertErr.value = true
    } else {
      dialog.value = false
      group_name.value = ''
      getGroups()
    }
  })
}

const sendData = (quitForm: boolean) => {
  const option = {
    body: {
      name: name.value,
      units: unit_selected.value,
      sport: id.value,
      general: true
    }
  } as IERequestOptions
  if(addToGroup && groups.value.length > 0){
    option.body['groups'] = group_selected.value
  }
  post('/admin/records/', option, true)
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
        name.value = ''
        description.value = ''
        if (quitForm) {
          router.push('/sports')
        } else {
          success_message.value = 'Vous avez ajoutez : ' + res.name
          alertSuc.value = true
        }
      }
    })
    .catch((error) => {
      alertErr.value = true
    })
  console.log(unit_selected.value)
}

const getSport = async () => {
  id.value = Number(route.params.sport_id)
  const res = await get('/admin/sports/' + id.value + '/')
  if (res.status > 300) {
    error_title.value = 'Erreur à la récupération du Sport avec pour id ' + id.value
    error_message.value = res.data.detail
    alertErr.value = true
  } else {
    sport.value = await res
    getGroups()
  }
}

const getGroups = async () => {
  await get('/record_group/by-sport/?sport_id=' + id.value).then((res) => {
    if (res.status > 300) {
      error_title.value = 'Erreur à la récupération des groupes'
      error_message.value = res.data.detail
      alertErr.value = true
    } else {
      groups.value = res
      console.log(res)
      console.log(group_selected.value)
      if(group_selected.value == null && res.length > 0){
        group_selected.value = res[0].id
      }
    }
  })
}
const units = [
  {
    name: 'Temps',
    value: 'time'
  },
  {
    name: 'Poids',
    value: 'weight'
  },
  {
    name: 'Distance (en km)',
    value: 'distance_km'
  },
  {
    name: 'Distance (en m)',
    value: 'distance_m'
  },
  {
    name: 'Points',
    value: 'points'
  },
  {
    name: 'Personnalisé',
    value: 'free'
  }
]

onMounted(() => {
  getSport()
})
</script>
<style>
.addView {
  margin-bottom: 20px;
}

.addView .v-btn__overlay {
  margin: 0px;
}
.addView .v-input__details {
  display :none;
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
    title="Erreur à l'ajout"
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
    title="Record ajouté"
    closable
    @click:close="closePopup"
  >
    {{ success_message }}
  </v-alert>
  <div class="mainWrapper">
    <NavButton
      class="returnBack"
      :text="'Retour'"
      :url="'/sports/show/' + id"
      prepend-icon="mdi-arrow-left"
    />
    <h1>Ajouter un Record à : {{ sport.name }}</h1>
    <form @submit.prevent="submit">
      <div class="inputFormDiv">
        <v-text-field v-model="name" label="Nom du record * " variant="filled"></v-text-field>
      </div>
      <div>
        <v-switch
          v-model="addToGroup"
          color="primary"
          label="Ajouter à un groupe ?"
          value="yes"
          hide-details
        ></v-switch>
        <div v-if="addToGroup">
          <div class="inputFormDiv addView">
            <div style="display: flex; align-items : center; width: 100%">
              <v-select
                v-model="group_selected"
                :items="groups"
                hint="Sélectionnez le groupe à utiliser"
                item-title="name"
                item-value="id"
                label="Groupe"
              />
              <v-btn @click="dialog = true" prepend-icon="mdi-plus" style="height:50px"></v-btn>
            </div>
            <v-dialog v-model="dialog" max-width="400" persistent>
              <v-card class="delete_modal">
                <v-card-title>Ajouter un groupe à : {{ sport.name }}</v-card-title>
                <div class="inputFormDiv">
                  <v-text-field
                    v-model="group_name"
                    label="Nom du groupe * "
                    variant="filled"
                  ></v-text-field>
                </div>
                <template v-slot:actions>
                  <v-spacer></v-spacer>

                  <v-btn variant="outlined" @click="dialog = false"> Annuler </v-btn>

                  <v-btn id="delete_btn" @click="sendGroup"> Ajouter </v-btn>
                </template>
              </v-card>
            </v-dialog>
          </div>
        </div>
      </div>
      <div class="inputFormDiv">
        <v-select
          v-model="unit_selected"
          :items="units"
          hint="Sélectionnez l'unité à utiliser"
          item-title="name"
          item-value="value"
          label="Unité"
        />
      </div>
      <div class="buttonWrapper">
        <button @click="sendData(false)">Créer et continuer</button>
        <button class="return_btn" @click="sendData(true)">Créer</button>
      </div>
    </form>
  </div>
</template>
