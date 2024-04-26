<script setup>
import router from '@/router'

const props = defineProps ([
    'url',
    'text',
    'back'
])
const nav = () => {
  if(props.back) {
    router.back(props.url);
  } else {
    router.push(props.url);
  }
}
</script>
<style lang=""></style>

<template lang="">
      <v-btn @click='nav'>
        <template v-slot:prepend>
          <v-icon></v-icon>
        </template>

        {{props.text}}
      </v-btn>
</template>
