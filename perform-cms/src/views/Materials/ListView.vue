<script setup lang="ts">
import NavMenu from '@/components/NavMenu.vue'
import ListElement from '@/components/ListElement.vue'
import NavButton from '@/components/NavButton.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'
import router from '@/router'
import { useRoute } from 'vue-router'
import PaginationComponent from '@/components/PaginationComponent.vue'

const navRoute = useRoute()
const materials = ref({})
const materialsCount = ref(0)
const itemsPerPage = ref(10)
const pagination = ref(0)
const page = ref(1)
const nameSearch = ref('')

const changeInput = async () => {
  const res = await get('/admin/materials', {
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
  materials.value = await res.results
  materialsCount.value = res.count
  pagination.value = Math.ceil(materialsCount.value / itemsPerPage.value)
}

const setPage = (value: number) => {
  page.value = value
}

const getMaterials = async () => {
  const res = await get('/admin/materials', {
    body: {},
    itemsPerPage: itemsPerPage.value,
    page: page.value
  })
  materials.value = await res.results
  materialsCount.value = res.count
  pagination.value = Math.ceil(materialsCount.value / itemsPerPage.value)
}

onMounted(() => {
  const pageQuery = navRoute.query.page as string
  if (pageQuery) {
    page.value = parseInt(pageQuery)
  }
  const searchQuery = navRoute.query.search as string
  if (searchQuery) {
    nameSearch.value = searchQuery
    changeInput()
  } else {
    getMaterials()
  }
})
</script>
<style lang=""></style>

<template lang="">
  <NavMenu />

  <div class="mainWrapper">
    <h1 class="listTitle">Materiels ({{materialsCount}})</h1>
    <h5 class="underTitle">Retrouvez la liste de tous vos Matériels</h5>
    <div class="headerList">
      <NavButton url="/materials/add" text="Ajouter" prepend-icon="mdi-plus" />
      <div class="searchBar">
        <div class="searchBar">
        <v-text-field
        placeholder="Chercher un matériel"
        prepend-inner-icon='mdi-magnify'
          v-model="nameSearch"
          @update:modelValue="changeInput"
          variant="filled"
        ></v-text-field>
        </div>
      </div>
    </div>
    <div>
      <ListElement
        :headerTable="['Id', 'Nom', 'Image']"
        :contentTable="materials"
        :limitData="3"
        nav="materials"
      />
      <PaginationComponent
        :setPage="setPage"
        :page="page"
        :getData="getMaterials"
        :pagination="pagination"
      />
    </div>
  </div>
</template>
