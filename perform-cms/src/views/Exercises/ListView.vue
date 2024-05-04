<script setup>
import NavMenu from '@/components/NavMenu.vue'
import ListElement from '@/components/ListElement.vue'
import NavButton from '@/components/NavButton.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'
import router from '@/router'
import { useRoute } from 'vue-router'
import PaginationComponent from '@/components/PaginationComponent.vue'
import OrderByComponent from '@/components/OrderByComponent.vue'

const exercises = ref({})
//Ref pour la pagination
const exercisesCount = ref(0)
const orderBy = ref("")
const itemsPerPage = ref(10)
const pagination = ref(0)
const page = ref(1)

const order = [
  { id: 'orderByNameAsc', value: 'Nom (Croissant)' },
  { id: 'orderByNameDesc', value: 'Nom (Décroissant)' },
  { id: 'orderByIdAsc', value: 'Id (Croissant)' },
  { id: 'orderByIdDesc', value: 'Id (Décroissant)' },
  { id: 'orderByDateAsc', value: 'Date (Croissant)' },
  { id: 'orderByDateDesc', value: 'Date (Décroissant)' }
]

const navRoute = useRoute()
const nameSearch = ref('')

const changeInput = async () => {
  const res = await get('/admin/exercises', {
    body: {},
    itemsPerPage: itemsPerPage.value,
    page: page.value,
    search: {
      name: nameSearch.value
    }
  })

  router.replace({
    path: navRoute.path,
    query: { search: nameSearch.value }
  })
  exercises.value = await res.results
  exercisesCount.value = res.count
  pagination.value = Math.ceil(exercisesCount.value / itemsPerPage.value)
}

const getExercises = async () => {
  const res = await get('/exercises', {
    body: {},
    itemsPerPage: itemsPerPage.value,
    page: page.value
  })
  exercises.value = await res.results
  exercisesCount.value = res.count
  pagination.value = Math.ceil(exercisesCount.value / itemsPerPage.value)
}

const setPage = (value) => {
  page.value = value
  console.log(page.value)
}

const setOrderBy = (value) =>{
    orderBy.value = value
  }


onMounted(() => {
  const pageQuery = navRoute.query.page
  if (pageQuery) {
    page.value = parseInt(pageQuery)
  }
  const orderByQuery = navRoute.query.orderBy
  if (pageQuery) {
    order.map((order) => {
      if(order.id === orderByQuery){
        orderBy.value = order
      }
    })
    console.log(orderBy.value)
  } 
  const searchQuery = navRoute.query.search
  if (searchQuery) {
    nameSearch.value = searchQuery
    changeInput()
  } else {
    getExercises()
  }
})
</script>
<style lang=""></style>

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
    <OrderByComponent :orderBy='orderBy' :setOrderBy='setOrderBy' />
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
