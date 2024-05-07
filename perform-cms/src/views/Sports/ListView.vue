<script setup lang="ts">
import NavMenu from '@/components/NavMenu/NavMenu.vue'
import ListElement from '@/components/ListElement/ListElement.vue'
import NavButton from '@/components/NavButton/NavButton.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'
import router from '@/router'
import PaginationComponent from '@/components/PaginationComponent/PaginationComponent.vue'
import { useRoute } from 'vue-router'
import OrderByComponent from '@/components/OrderByComponent/OrderByComponent.vue'

const navRoute = useRoute()

const sports = ref({})
//Ref pour la pagination
const sportsCount = ref(0)
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

const setOrderBy = (value) => {
  orderBy.value = value
  getSports()
}

const changeInput = async () => {
  const res = await get('/admin/sports', {
    body: {},
    itemsPerPage: itemsPerPage.value,
    page: page.value,
    search: {
      name: nameSearch.value
    }
  })

  router.replace({
    path: navRoute.path,
    query: Object.assign({}, navRoute.query, { search: nameSearch.value })
  })
  sports.value = await res.results
  sportsCount.value = res.count
  pagination.value = Math.ceil(sportsCount.value / itemsPerPage.value)
}

const setPage = (value: number) => {
  page.value = value
}

const getSports = async () => {
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
  const res = await get('/admin/sports', option)
  sports.value = await res.results
  sportsCount.value = res.count
  pagination.value = Math.ceil(sportsCount.value / itemsPerPage.value)
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
  getSports()
})
</script>
<style lang=""></style>

<template lang="">
  <NavMenu />

  <div class="mainWrapper">
    <h1 class="listTitle">Sports ({{ sportsCount }})</h1>
    <h5 class="underTitle">Retrouvez la liste de tous vos Sports</h5>
    <div class="headerList">
      <NavButton url="/sports/add" text="Ajouter" prepend-icon="mdi-plus" />
      <div class="searchBar">
        <v-text-field
          placeholder="Chercher un sport"
          prepend-inner-icon="mdi-magnify"
          v-model="nameSearch"
          variant="filled"
          @update:modelValue="changeInput"
        ></v-text-field>
      </div>
    </div>
    <OrderByComponent :orderBy="orderBy" :setOrderBy="setOrderBy" />
    <div>
      <ListElement
        :headerTable="['Id', 'Nom']"
        :contentTable="sports"
        :limitData="2"
        nav="sports"
      />
      <PaginationComponent
        :setPage="setPage"
        :page="page"
        :getData="getSports"
        :pagination="pagination"
      />
    </div>
  </div>
</template>
