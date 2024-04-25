<script setup lang="ts">
import NavMenu from '@/components/NavMenu.vue'
import ListElement from '@/components/ListElement.vue'
import NavButton from '@/components/NavButton.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'
import router from '@/router'

const sports = ref({})

const getSports = async () => {
  const res = await get('/admin/sports');
  sports.value = await res.results;
}

onMounted(() => {
  getSports();
})

</script>
<style lang=""></style>

<template lang="">
  <NavMenu />

  <div class="mainWrapper">
    <h1>Sports</h1>
    <div>
      <NavButton url="/sports/add" text="Ajouter" />
    </div>
    <div>
      <ListElement :headerTable="['Id', 'Nom']" :contentTable="sports" :limitData="2" nav="sports"/>
    </div>
  </div>
</template>
