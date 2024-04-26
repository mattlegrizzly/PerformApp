<script setup>
import NavMenu from '@/components/NavMenu.vue'
import ListElement from '@/components/ListElement.vue'
import NavButton from '@/components/NavButton.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'
import router from '@/router'

const exercises = ref({})

const getExercises = async () => {
  const res = await get('/exercises');
  exercises.value = await res.results;
}

onMounted(() => {
  getExercises();
})
</script>
<style lang=""></style>

<template lang="">
  <NavMenu />

  <div class="mainWrapper">
    <h1>Exercises</h1>
    <div>
      <NavButton url="/exercises/add" text="Ajouter" prepend-icon="mdi-plus" />
    </div>
    <div>
      <ListElement :headerTable="['id','Nom']" :contentTable="exercises" :limitData="2" nav="exercises"/>
    </div>
  </div>
</template>
