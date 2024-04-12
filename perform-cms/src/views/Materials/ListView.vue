<script setup lang="ts">
import NavMenu from '@/components/NavMenu.vue'
import ListElement from '@/components/ListElement.vue'
import NavButton from '@/components/NavButton.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'
import router from '@/router'

const materials = ref({})
const materialsCount = ref(0)
const itemsPerPage = ref(10)
const pagination = ref(1)
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
    if(target && target.outerText) {
      page.value = parseInt(target.outerText);
      getMaterials()
    }
}

onMounted(() => {
  getMaterials()
})
</script>
<style lang=""></style>

<template lang="">
  <NavMenu />

  <div class="mainWrapper">
    <h1>Materials</h1>
    <div>
      <NavButton url="/materials/add" text="Ajouter" />
    </div>
    <div>
      <ListElement :headerTable="['Id', 'Nom']" :contentTable="materials" :limitData="2" />
      <v-pagination :length="pagination" @click="setPagination"></v-pagination>
    </div>
  </div>
</template>
