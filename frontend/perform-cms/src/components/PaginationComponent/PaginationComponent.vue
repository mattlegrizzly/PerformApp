<script setup lang="ts">
import { useRoute } from 'vue-router'
import router from '@/router'

const navRoute = useRoute()

const props = defineProps(['setPage', 'page', 'getData', 'pagination'])

const setPagination = async (e: Event) => {
  const target = e.target as HTMLElement

  if (target && target.outerText) {
    const page = parseInt(target.outerText)
    props.setPage(page)
    router.replace({
      path: navRoute.path,
      query: Object.assign({}, navRoute.query, { page: page }) 
    })
    props.getData()
  }
}

const changePagination = async (e: any) => {
  props.setPage(parseInt(e))
  router.replace({
    path: navRoute.path,
    query: { page: e }
  })
  props.getData()
}
</script>

<template>
  <v-pagination
    :model-value="page"
    :length="props.pagination"
    @click="setPagination"
    @next="changePagination"
    @prev="changePagination"
  ></v-pagination>
</template>
