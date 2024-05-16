<script setup lang="ts">
import NavMenu from '@/components/NavMenu/NavMenu.vue'
import ListElement from '@/components/ListElement/ListElement.vue'
import NavButton from '@/components/NavButton/NavButton.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'
import router from '@/router'
import { useRoute } from 'vue-router'
import PaginationComponent from '@/components/PaginationComponent/PaginationComponent.vue'
import OrderByComponent from '@/components/OrderByComponent/OrderByComponent.vue'
import type { Order } from '@/types/types'
import type IERequestOptions from '@/types/request'

const navRoute = useRoute()
const materials = ref({})
const materialsCount = ref(0)
const itemsPerPage = ref(10)
const pagination = ref(0)
const page = ref(1)
const nameSearch = ref('')
const orderBy = ref({ id: 'default', value: 'Par défaut'})
const order = [
  { id: 'orderByNameAsc', value: 'Nom (Croissant)' },
  { id: 'orderByNameDesc', value: 'Nom (Décroissant)' },
  { id: 'orderByIdAsc', value: 'Id (Croissant)' },
  { id: 'orderByIdDesc', value: 'Id (Décroissant)' },
  { id: 'orderByDateAsc', value: 'Date (Croissant)' },
  { id: 'orderByDateDesc', value: 'Date (Décroissant)' },
  { id: 'default', value: 'Par défaut'}
]

const setOrderBy = (value : Order) => {
  orderBy.value = value
  getMaterials()
}

const changeInput = async () => {
  const res = await get('/admin/materials', {
    body: {},
    itemsPerPage: itemsPerPage.value.toString(),
    page: page.value.toString(),
    search: {
      name: nameSearch.value
    }
  })

  router.replace({
    path: navRoute.path,
    query: Object.assign({}, navRoute.query, { search: nameSearch.value })
  })
  materials.value = await res.results
  materialsCount.value = res.count
  pagination.value = Math.ceil(materialsCount.value / itemsPerPage.value)
}

const setPage = (value: number) => {
  page.value = value
}

const getMaterials = async () => {
  const option = {
    body: {},
    itemsPerPage: itemsPerPage.value.toString(),
    page: page.value.toString(),
    search : {
      name : '',
    },
    orderBy : { id: 'default', value: 'Par défaut'}
  }
  if (orderBy.value) {
    option.orderBy = orderBy.value
  }
  if (nameSearch.value !== '') {
    option.search = {
      name: nameSearch.value
    }
  }

  const res = await get('/admin/materials', option)
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
  }
  const orderByQuery = navRoute.query.orderBy
  if (orderByQuery) {
    order.map((order) => {
      if (order.id === orderByQuery) {
        orderBy.value = order
      }
    })
  }
  getMaterials()
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
    <OrderByComponent :orderBy="orderBy" :setOrderBy="setOrderBy" />
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
