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
  /* const searchQuery = navRoute.query.search as string;
  if(pageQuery){
    sea.value = parseInt(pageQuery)
  } */
  getMaterials()
})
</script>
<style lang=""></style>

<template lang="">
  <NavMenu />

  <div class="mainWrapper">
    <h1>Materials</h1>
    <div>
      <NavButton url="/materials/add" text="Ajouter" prepend-icon="mdi-plus" />
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
