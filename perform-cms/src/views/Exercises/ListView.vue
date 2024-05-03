<script setup>
import NavMenu from '@/components/NavMenu.vue'
import ListElement from '@/components/ListElement.vue'
import NavButton from '@/components/NavButton.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'
import router from '@/router'
import { useRoute } from 'vue-router'
import PaginationComponent from '@/components/PaginationComponent.vue'

const exercises = ref({})
//Ref pour la pagination
const exercisesCount = ref(0)
const itemsPerPage = ref(10)
const pagination = ref(0)
const page = ref(1)

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
}

onMounted(() => {
  const pageQuery = navRoute.query.page
  if (pageQuery) {
    page.value = parseInt(pageQuery)
  }
  const searchQuery = navRoute.query.search
  console.log(searchQuery)
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
    <h1>Exercises</h1>
    <div>
      <NavButton url="/exercises/add" text="Ajouter" prepend-icon="mdi-plus" />
      <v-text-field
        v-model="nameSearch"
        label="Chercher un exercice, un sport, un matériel.."
        variant="filled"
        @update:modelValue="changeInput"
      ></v-text-field>
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
