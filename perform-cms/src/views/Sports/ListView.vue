<script setup lang="ts">
import NavMenu from '@/components/NavMenu.vue'
import ListElement from '@/components/ListElement.vue'
import NavButton from '@/components/NavButton.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'
import router from '@/router'
import PaginationComponent from '@/components/PaginationComponent.vue'
import { useRoute } from 'vue-router'

const navRoute = useRoute()

const sports = ref({})
//Ref pour la pagination
const sportsCount = ref(0)
const itemsPerPage = ref(10)
const pagination = ref(0)
const page = ref(1)
const nameSearch = ref('')

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
    query: { search: nameSearch.value }
  })
  sports.value = await res.results
  sportsCount.value = res.count
  pagination.value = Math.ceil(sportsCount.value / itemsPerPage.value)
}

const setPage = (value: number) => {
  page.value = value
}

const getSports = async () => {
  const res = await get('/admin/sports', {
    body: {},
    itemsPerPage: itemsPerPage.value,
    page: page.value
  })
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
    changeInput()
  } else {
    getSports()
  }
})
</script>
<style lang=""></style>

<template lang="">
  <NavMenu />

  <div class="mainWrapper">
    <h1 class="listTitle">Sports ({{sportsCount}})</h1>
    <h5 class="underTitle">Retrouvez la liste de tous vos Sports</h5>
    <div class="headerList">
      <NavButton url="/sports/add" text="Ajouter" prepend-icon="mdi-plus" />
      <div class="searchBar">
        <v-text-field
        placeholder="Chercher un sport"
        prepend-inner-icon='mdi-magnify'
        v-model="nameSearch"
        variant="filled"
        @update:modelValue="changeInput"
      ></v-text-field>
      </div>
    </div>
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
