<script setup>
import NavMenu from '@/components/NavMenu/NavMenu.vue'
import ListElement from '@/components/ListElement/ListElement.vue'
import NavButton from '@/components/NavButton/NavButton.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'
import router from '@/router'
import { useRoute } from 'vue-router'
import PaginationComponent from '@/components/PaginationComponent/PaginationComponent.vue'
import OrderByComponent from '@/components/OrderByComponent/OrderByComponent.vue'
import BodyComponent from '@/components/BodyComponent/BodyComponent.vue'

const exercises = ref({})

const materials = ref({})
const muscles = ref({})
const sports = ref({})

const showFilter = ref(false)

const materials_id_filter = ref([])
const sport_selected = ref([])

//Ref pour la pagination
const exercisesCount = ref(0)
const orderBy = ref({ id: 'default', value: 'Par défaut' })
const itemsPerPage = ref(10)
const pagination = ref(0)
const page = ref(1)
const muscle_selected = ref([])

const order = [
  { id: 'orderByNameAsc', value: 'Nom (Croissant)' },
  { id: 'orderByNameDesc', value: 'Nom (Décroissant)' },
  { id: 'orderByIdAsc', value: 'Id (Croissant)' },
  { id: 'orderByIdDesc', value: 'Id (Décroissant)' },
  { id: 'orderByDateAsc', value: 'Date (Croissant)' },
  { id: 'orderByDateDesc', value: 'Date (Décroissant)' },
  { id: 'default', value: 'Par défaut' }
]

const navRoute = useRoute()
const nameSearch = ref('')

const addMaterialFilter = (id) => {
  const findKey =
    materials_id_filter.value.filter(function (element) {
      return element === id
    }).length == 0
  if (findKey) {
    materials_id_filter.value.push(id)
  } else {
    const index = materials_id_filter.value.indexOf(id)
    materials_id_filter.value.splice(index)
  }
}

const setMuscleSelected = (key , action) => {
  if (action === 'add') {
    const findKey =
      muscle_selected.value.filter(function (element) {
        return element === key
      }).length == 0
    console.log(findKey)
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
    itemsPerPage: itemsPerPage.value,
    page: page.value,
    search: {
      name: nameSearch.value
    }
  }
  if (orderBy.value !== '') {
    option['orderBy'] = orderBy.value.id
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
  console.log(jointByComa(materials_id_filter.value))
  const option = {}
  if(materials_id_filter.value.length > 0) 
  {
    option['material_id'] = jointByComa(materials_id_filter.value)
  }
  if(muscle_selected.value.length > 0) 
  {
    option['workzone_code'] = jointByComa(muscle_selected.value)
  }
  if(sport_selected.value.length > 0) 
  {
    option['sport_id'] = jointByComa(sport_selected.value)
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
    itemsPerPage: itemsPerPage.value,
    page: page.value
  }
  if (orderBy.value !== '') {
    option['orderBy'] = orderBy.value.id
  }
  if (nameSearch.value !== '') {
    option['search'] = {
      name: nameSearch.value
    }
  }

  if (materials_id_filter.value.length > 0) {
    option['material_id'] = jointByComa(materials_id_filter.value)
  }

  if (sport_selected.value.length > 0) {
    option['sport_id'] = jointByComa(sport_selected.value)
  }

  if (muscle_selected.value.length > 0) {
    option['workzone_code'] = jointByComa(muscle_selected.value)
  }

  const res = await get('/admin/exercises', option)
  exercises.value = await res.results
  exercisesCount.value = res.count
  pagination.value = Math.ceil(exercisesCount.value / itemsPerPage.value)
}

const jointByComa = (array) => {
  let stringWithCommas = ''
  for (let i = 0; i < array.length; i++) {
    stringWithCommas += array[i]
    if (i < array.length - 1) {
      stringWithCommas += ', '
    }
  }
  return stringWithCommas
}

const setPage = (value) => {
  page.value = value
}

const setOrderBy = (value) => {
  orderBy.value = value
  getExercises()
}

onMounted(async () => {
  const pageQuery = navRoute.query.page
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
  const searchQuery = navRoute.query.search
  if (searchQuery) {
    nameSearch.value = searchQuery
  }

  const material_id = navRoute.query.material_id
  if (material_id) {
    const array = material_id.split(',')
    array.map((id) => {
      materials_id_filter.value.push(id)
    })
  }

  const sport_id = navRoute.query.sport_id
  if (sport_id) {
    const array = sport_id.split(',')
    array.map((id) => {
      sport_selected.value.push(id)
    })
  }

  const muscle_zone = navRoute.query.workzone_code
  if (muscle_zone) {
    const array = muscle_zone.split(',')
    array.map((id) => {
      muscle_selected.value.push(id)
    })
  }

  const res_materials = await get('/admin/materials/all/', { body: {} }, true)
  if (res_materials.status === 404) {
    error_title.value = 'Error while retrieve materials'
    error_message.value = res_materials.data.detail
    alertErr.value = true
  } else {
    materials.value = res_materials
    materials.value.map((material, index) => {
      materials.value[index].pictures = 'http://localhost:8000' + material.pictures
    })
  }
  const res_sports = await get('/admin/sports/all/', { body: {} }, true)
  if (res_sports.status === 404) {
    error_title.value = 'Error while retrieve sports'
    error_message.value = res_sports.data.detail
    alertErr.value = true
  } else {
    sports.value = res_sports
  }

  const res_muscles = await get('/admin/workzones/all/', { body: {} }, true)
  if (res_muscles.status > 300) {
    error_title.value = 'Error while retrieve muscles'
    error_message.value = res_muscles.data.detail
    alertErr.value = true
  } else {
    muscles.value = res_muscles
  }

  getExercises('')
})
</script>
<style>
.filterDiv {
  display: flex;
  justify-content: end;
  padding-top: 15px;
}

.textTitleCard {
  color: var(--primary-blue);
  text-align: center;
  font-size: 14px !important;
}
</style>

<template lang="">
  <NavMenu />

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
                    :src="material.pictures"
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
                    <v-card-title
                      class="textTitleCard"
                      v-text="material.name + ' ' + material.id"
                    ></v-card-title>
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
              :viewOnly="'add'"
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
</template>
