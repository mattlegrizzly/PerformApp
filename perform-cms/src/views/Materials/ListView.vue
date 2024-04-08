<script setup lang="ts">
import NavMenu from '@/components/NavMenu.vue'
import ListElement from '@/components/ListElement.vue'
import NavButton from '@/components/NavButton.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'
import router from '@/router'

const materials = ref({})

const getMaterials = async () => {
  const res = await get('/admin/materials');
  materials.value = await res.results;
  console.log(res)
}

onMounted(() => {
  getMaterials();
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
    </div>
  </div>
</template>
