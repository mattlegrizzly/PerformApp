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
const navRoute = useRoute()

const users = ref({})
//Refs pour la pagination
const usersCount = ref(0)
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
  getUsers()
}

const changeInput = async () => {
  const res = await get('/admin/users_all', {
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
  users.value = await res.results
  usersCount.value = res.count
  pagination.value = Math.ceil(usersCount.value / itemsPerPage.value)
}

const getUsers = async () => {
  const res = await get('/admin/users_all', {
    body: {},
    itemsPerPage: itemsPerPage.value.toString(),
    page: page.value.toString()
  })
  users.value = await res.results
  usersCount.value = res.count
  pagination.value = Math.ceil(usersCount.value / itemsPerPage.value)
}

const setPage = (value: number) => {
  page.value = value
}

onMounted(() => {
  const pageQuery = navRoute.query.page
  if (pageQuery) {
    page.value = parseInt(pageQuery.toString())
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
    nameSearch.value = searchQuery.toString()
  }
  getUsers()
})
</script>
<style lang=""></style>

<template lang="">
  <NavMenu />

  <div class="mainWrapper">
    <h1 class="listTitle">Tous les utilisateurs ({{usersCount}})</h1>
    <h5 class="underTitle">Retrouvez la liste de tous vos Utilisateurs</h5>
    <div class="headerList">
      <NavButton url="/users/add" text="Ajouter" prepend-icon="mdi-plus" />
      <div class="searchBar">
        <v-text-field
        placeholder="Chercher un utilisateur"
        prepend-inner-icon='mdi-magnify'
        v-model="nameSearch"
        variant="filled"
        @update:modelValue="changeInput"
      ></v-text-field>
      </div>
    </div>
    <OrderByComponent :orderBy="orderBy" :setOrderBy="setOrderBy" />
    <div>
      <ListElement :headerTable="['Id', 'Email', 'Nom', 'Prénom']" :contentTable="users" :limitData="4" nav="users" />
      <PaginationComponent
        :setPage="setPage"
        :page="page"
        :getData="getUsers"
        :pagination="pagination"
      />
    </div>
  </div>
</template>
