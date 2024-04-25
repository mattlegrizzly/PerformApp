<script setup lang="ts">
import NavMenu from '@/components/NavMenu.vue'
import ListElement from '@/components/ListElement.vue'
import NavButton from '@/components/NavButton.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'
import router from '@/router'
import { useRoute } from 'vue-router'

const navRoute = useRoute()
const materials = ref({})
const materialsCount = ref(0)
const itemsPerPage = ref(10)
const pagination = ref(0)
const page = ref(1)

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
const setPagination = async (e: Event) => {
  const target = e.target as HTMLElement

  if (target && target.outerText) {
    page.value = parseInt(target.outerText)
    router.replace({
      path: navRoute.path,
      query: { page: page.value }
    })
    getMaterials()
  }
}

const changePagination = async (e : any) => {
  page.value = parseInt(e)
  router.replace({
    path: navRoute.path,
      query: { page: e}
    })
    getMaterials()
}

onMounted(() => {
  const pageQuery = navRoute.query.page as string;
  if(pageQuery){
    page.value = parseInt(pageQuery)
  }
  getMaterials();
})
</script>
<style lang=""></style>

<template lang="">
  <NavMenu />

  <div class="mainWrapper">
    <h1>Materials</h1>
    <div>
      <NavButton url="/materials/add" text="Ajouter" prepend-icon="mdi-plus"/>
    </div>
    <div>
      <ListElement :headerTable="['Id', 'Nom']" :contentTable="materials" :limitData="2" nav="materials" />
      <v-pagination :model-value='page' :length="pagination" @click="setPagination" @next="changePagination" @prev="changePagination"></v-pagination>
    </div>
  </div>
</template>
