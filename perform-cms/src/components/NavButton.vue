<script setup>
import router from '@/router'

const props = defineProps ([
    'url',
    'text'
])
const nav = () => {
  router.push(props.url);
}
</script>
<style lang=""></style>

<template lang="">
      <v-btn prepend-icon="mdi-add" @click='nav'>
        <template v-slot:prepend>
          <v-icon color="success"></v-icon>
        </template>

        {{props.text}}
      </v-btn>
</template>
