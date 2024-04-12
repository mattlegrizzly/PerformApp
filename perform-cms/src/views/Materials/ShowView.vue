<template lang="">
  <NavMenu />
  <div class="mainWrapper">
    <div class="headerBtns">
      <NavButton class='returnBtn' :text="'Retour'" :url="'/materials'"/>
      <NavButton class='editBtn' :text="'Modifier'" :url="'/materials/edit/'+ material.id"/>
    </div>
    <h1>Carte du matériel : {{ material === undefined ? '': material.name }}</h1>
    <h2 class="showTitle">Titre</h2>
    <p>{{ material === undefined ? '': material.name }}</p>
    <h2 class="showTitle">Description</h2>
    <p>
      {{material.description}}
    </p>
    <h2 class="showTitle">Image</h2>
    <div class="imageDiv">
        <v-img :width="300" aspect-ratio="16/9" cover :src="material.pictures"></v-img>
      </div>
  </div>
</template>
<script setup lang="ts">
import NavMenu from '@/components/NavMenu.vue'
import { ref } from 'vue'
import { get } from '@/lib/callApi'
import { useRoute } from 'vue-router'
import { onMounted } from 'vue'
import NavButton from '@/components/NavButton.vue'
const router = useRoute()
const material = ref('')

const getMaterial = async () => {
 const id = router.params.material_id;
  const res = await get('/admin/materials/'+id+'/')
  material.value = await res;
}

onMounted(() => {
  getMaterial()
})
</script>
<style>
h1, h2 {
  text-align: left !important;
}

.showTitle {
  margin-bottom : 0px !important;
  margin-top : 10px !important;
}

.headerBtns {
  margin-top : 10px;
  display : flex;
  justify-content: space-between;
  padding-right : 10px;
}
</style>
