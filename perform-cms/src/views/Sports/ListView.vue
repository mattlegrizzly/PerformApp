<script setup lang="ts">
import NavMenu from '@/components/NavMenu.vue'
import ListElement from '@/components/ListElement.vue'
import NavButton from '@/components/NavButton.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'
import router from '@/router'
import PaginationComponent from '@/components/PaginationComponent.vue'

const sports = ref({})
//Ref pour la pagination
const sportsCount = ref(0)
const itemsPerPage = ref(10)
const pagination = ref(0)
const page = ref(1)

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
  getSports()
})
</script>
<style lang=""></style>

<template lang="">
  <NavMenu />

  <div class="mainWrapper">
    <h1>Sports</h1>
    <div>
      <NavButton url="/sports/add" text="Ajouter" prepend-icon="mdi-plus" />
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
