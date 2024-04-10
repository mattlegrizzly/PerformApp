<template lang="">
  <NavMenu />
  <div class="mainWrapper">
    <h1>{{ material === undefined ? '': material.name }}</h1>
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

const router = useRoute()
const material = ref('')

const getMaterial = async () => {
 const id = router.params.material_id;
  const res = await get('/admin/materials/'+id+'/')
  material.value = await res
  console.log(material)
}

onMounted(() => {
  getMaterial()
})
</script>
<style lang=""></style>
