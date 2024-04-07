<script setup lang="ts">
import NavMenu from '@/components/NavMenu.vue'
import ListElement from '@/components/ListElement.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'

const materials = ref({})

const getMaterials = async () => {
  const res = await get('/admin/materials');
  materials.value = await res;
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
      <v-btn prepend-icon="mdi-add">
        <template v-slot:prepend>
          <v-icon color="success"></v-icon>
        </template>

        Ajouter
      </v-btn>
    </div>
    <div>
      <ListElement :headerTable="['Id', 'Nom']" :contentTable="materials" :limitData="2" />
    </div>
  </div>
</template>
