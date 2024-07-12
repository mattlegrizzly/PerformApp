<script setup lang="ts">
import NavMenu from '@/components/NavMenu/NavMenu.vue'
import ListElement from '@/components/ListElement/ListElement.vue'
import NavButton from '@/components/NavButton/NavButton.vue'
import AlertComponents from '@/components/AlertComponents/AlertComponents.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'
import router from '@/router'
import { useRoute } from 'vue-router'
import PaginationComponent from '@/components/PaginationComponent/PaginationComponent.vue'
import OrderByComponent from '@/components/OrderByComponent/OrderByComponent.vue'
//@ts-expect-error
import {BodyComponent} from 'perform-body-component-lib'
import "perform-body-component-lib/style.css";
import { RouterView } from 'vue-router'
import type { Order, QueryParams } from '@/types/types'
import './exercises.css'
import type IERequestOptions from '@/types/request'

const alertErr = ref(false)
const error_title = ref('')
const error_message = ref('')

const api_url = import.meta.env.VITE_API_URL

const exercises = ref({})

const materials: any = ref({})
const muscles: any = ref({})
const sports: any = ref({})

const showFilter = ref(false)

const materials_id_filter: any = ref([])
const sport_selected: any = ref([])
const muscle_selected: any = ref([])

//Ref pour la pagination
const exercisesCount = ref(0)
const orderBy = ref({ id: 'default', value: 'Par défaut' })
const itemsPerPage = ref(10)
const pagination = ref(0)
const page = ref(1)

const order = [
  { id: 'orderByNameAsc', value: 'Nom (Croissant)' },
  { id: 'orderByNameDesc', value: 'Nom (Décroissant)' },
  { id: 'orderByIdAsc', value: 'Id (Croissant)' },
  { id: 'orderByIdDesc', value: 'Id (Décroissant)' },
  { id: 'orderByDateAsc', value: 'Date (Croissant)' },
  { id: 'orderByDateDesc', value: 'Date (Décroissant)' },
  { id: 'default', value: 'Par défaut' }
]

const params_push = [
  {
    query_key: 'material_id',
    array_name: materials_id_filter
  },
  {
    query_key: 'sport_id',
    array_name: sport_selected
  },
  {
    query_key: 'workzone_code',
    array_name: muscle_selected
  }
]

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

const navRoute = useRoute()
const nameSearch = ref('')

const setAlertValue = (type: string) => {
  if (type === "error") {
    alertErr.value = false
  } else {

  }
}

const addMaterialFilter = (id: any) => {
  const findKey =
    materials_id_filter.value.filter(function (element: any) {
      return element === id
    }).length == 0
  if (findKey) {
    materials_id_filter.value.push(id)
  } else {
    const index = materials_id_filter.value.indexOf(id)
    materials_id_filter.value.splice(index, 1)
  }
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

const changeInput = async () => {
  const option = {
    body: {},
    itemsPerPage: itemsPerPage.value.toString(),
    page: page.value.toString(),
    search: {
      name: nameSearch.value
    },
    orderBy: { id: 'default', value: 'Par défaut' }
  } as IERequestOptions
  if (orderBy.value) {
    option.orderBy = orderBy.value
  }
  if (materials_id_filter.value.length > 0) {
    option.material_id = materials_id_filter.value
  }
  if (muscle_selected.value.length > 0) {
    option.workzone_code = muscle_selected.value
  }
  if (sport_selected.value.length > 0) {
    option.sport_id = sport_selected.value
  }

  const res = await get('/admin/exercises', option)

  router.replace({
    path: navRoute.path,
    query: Object.assign({}, navRoute.query, { search: nameSearch.value })
  })
  exercises.value = await res.results
  exercisesCount.value = res.count
  pagination.value = Math.ceil(exercisesCount.value / itemsPerPage.value)
}

const filterExercice = () => {
  showFilter.value = false
  const option = {} as IERequestOptions
  if (materials_id_filter.value.length > 0) {
    option.material_id = jointByComa(materials_id_filter.value)
  }
  if (muscle_selected.value.length > 0) {
    option.workzone_code = jointByComa(muscle_selected.value)
  }
  if (sport_selected.value.length > 0) {
    option.sport_id = jointByComa(sport_selected.value)
  }
  router.replace({
    path: navRoute.path,
    query: Object.assign({}, navRoute.query, option)
  })
  getExercises()
}

const getExercises = async () => {
  const option = {
    body: {},
    itemsPerPage: itemsPerPage.value.toString(),
    page: page.value.toString(),
    search: {
      name: ''
    },
    orderBy: { id: 'default', value: 'Par défaut' }
  } as IERequestOptions
  if (orderBy.value) {
    option.orderBy = orderBy.value
  }
  if (nameSearch.value !== '') {
    option.search = {
      name: nameSearch.value
    }
  }

  if (materials_id_filter.value.length > 0) {
    option.material_id = jointByComa(materials_id_filter.value)
  }

  if (sport_selected.value.length > 0) {
    option.sport_id = jointByComa(sport_selected.value)
  }

  if (muscle_selected.value.length > 0) {
    option.workzone_code = jointByComa(muscle_selected.value)
  }

  get('/admin/exercises', option).then((res) => {
    if (res.status > 300) {
      error_message.value = res.data
      alertErr.value = true
      error_title.value = 'Erreur à la récupération des messages'
    } else {
      exercises.value = res.results
      exercisesCount.value = res.count
      pagination.value = Math.ceil(exercisesCount.value / itemsPerPage.value)
    }
  })
}

const pushData = (params_push: any) => {
  params_push.map((elem: any) => {
    const ids = navRoute.query[elem.query_key] as any
    if (ids) {
      const array = ids.split(',')
      array.map((id: any) => {
        if (elem.query_key != 'workzone_code') elem.array_name.value.push(parseInt(id))
        else elem.array_name.value.push(id)
      })
    }
  })
}

const jointByComa = (array: Array<string>) => {
  let stringWithCommas = ''
  for (let i = 0; i < array.length; i++) {
    stringWithCommas += array[i]
    if (i < array.length - 1) {
      stringWithCommas += ', '
    }
  }
  return stringWithCommas
}

const setPage = (value: number) => {
  page.value = value
}

const setOrderBy = (value: Order) => {
  orderBy.value = value
  getExercises()
}

onMounted(async () => {
  const pageQuery = navRoute.query.page as string
  if (pageQuery) {
    page.value = parseInt(pageQuery)
  }
  const orderByQuery = navRoute.query.orderBy
  if (orderByQuery) {
    order.map((order) => {
      if (order.id === orderByQuery) {
        orderBy.value = order
      }
    })
  }
  const searchQuery = navRoute.query.search as string
  if (searchQuery) {
    nameSearch.value = searchQuery
  }

  pushData(params_push)

  dataToRetrieve.map(async (elem) => {
    const res = await get(elem.link, { body: {} }, true)
    if (res.status === 404) {
      error_title.value = 'Erreur à la récupération des exercices'
      error_message.value = res.data.detail
      alertErr.value = true
    } else {
      elem.array.value = res
    }
  })

  getExercises()
})
</script>

<template lang="">
  <NavMenu />
  <AlertComponents
    :title="error_title"
    :type="'error'"
    :alertValue="alertErr"
    :message_alert="error_message"
    :setAlertValue="setAlertValue"
  />
  <router-view>
    <div class="mainWrapper">
      <h1 class="listTitle">Exercices ({{ exercisesCount }})</h1>
      <h5 class="underTitle">Retrouvez la liste de tous vos exercices</h5>
      <div class="headerList">
        <NavButton url="/exercises/add" text="Ajouter" prepend-icon="mdi-plus" />
        <div class="searchBar">
          <v-text-field
            placeholder="Chercher un exercice, un sport, un matériel."
            prepend-inner-icon="mdi-magnify"
            v-model="nameSearch"
            variant="filled"
            @update:modelValue="changeInput"
          ></v-text-field>
        </div>
      </div>
      <OrderByComponent :orderBy="orderBy" :setOrderBy="setOrderBy" />
      <div class="filterDiv">
        <v-btn @click="showFilter = true" text="Filtres" variant="elevated"></v-btn>
        <v-dialog v-model="showFilter" max-width="500">
          <v-card
            title="Filtrer les exercices"
            subtitle="Sélectionnez les filtres que vous souhaitez appliquer aux exercices"
            class="mx-auto"
            max-width="700"
          >
            <v-card-item title="Matériels">
              <v-row dense>
                <v-col v-for="material in materials" :key="material.id" cols="12" sm="4">
                  <v-card @click="addMaterialFilter(material.id)">
                    <v-img
                      :src="api_url + material.pictures"
                      class="align-end"
                      :gradient="
                        materials_id_filter.includes(material.id)
                          ? 'to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)'
                          : 'to bottom, rgba(0,0,0,.05), rgba(0,0,0,.1'
                      "
                      height="100px"
                      cover
                      aspect-ratio="1"
                    >
                      <v-icon
                        :icon="materials_id_filter.includes(material.id) ? 'mdi-check' : ''"
                      ></v-icon>
                      <v-card-title class="textTitleCard">{{ material.name }}</v-card-title>
                    </v-img>
                  </v-card>
                </v-col>
              </v-row>
            </v-card-item>
            <v-card-item title="Sports">
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
            </v-card-item>
            <v-card-item title="Zones de travail">
              <BodyComponent
                :height="300"
                :width="'50%'"
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
              >
              </v-select>
            </v-card-item>
            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn text="Filtrer" variant="elevated" @click="filterExercice"></v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
      <div>
        <ListElement
          :headerTable="['id', 'Nom']"
          :contentTable="exercises"
          :limitData="2"
          nav="exercises"
        />
        <PaginationComponent
          :setPage="setPage"
          :page="page"
          :getData="getExercises"
          :pagination="pagination"
        />
      </div>
    </div>
  </router-view>
</template>
