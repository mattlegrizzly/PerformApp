<script setup>
import NavMenu from '../../components/NavMenu.vue'
import ListElement from '../../components/ListElement.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'
import router from '@/router'

const exercises = ref({})

const getExercises = async () => {
  const res = await get('/admin/exercises');
  exercises.value = await res;
}


const nav = () => {
  router.push('/exercises/add');
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
      <v-btn prepend-icon="mdi-add" @click='nav'>
        <template v-slot:prepend>
          <v-icon color="success"></v-icon>
        </template>

        Ajouter
      </v-btn>
    </div>
    <div>
      <ListElement :headerTable="['Nom']" :contentTable="exercises" :limitData="1" />
    </div>
  </div>
</template>
