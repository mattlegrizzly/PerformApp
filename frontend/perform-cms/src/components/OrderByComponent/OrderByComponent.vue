<script setup lang="ts">
import router from '@/router'
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import './index.css'
const navRoute = useRoute()

const props = defineProps(['setOrderBy', 'orderBy'])

const order = [
  { id: 'default', value: 'Par défaut'},
  { id: 'orderByNameAsc', value: 'Nom (Croissant)' },
  { id: 'orderByNameDesc', value: 'Nom (Décroissant)' },
  { id: 'orderByIdAsc', value: 'Id (Croissant)' },
  { id: 'orderByIdDesc', value: 'Id (Décroissant)' },
  { id: 'orderByDateAsc', value: 'Date (Croissant)' },
  { id: 'orderByDateDesc', value: 'Date (Décroissant)' }
]

const changeOrder = (e : any) => {
  console.log('Change ', e)
  let find = false;
  order.map((order) => {
    if (order.id === e) {
      props.setOrderBy(order)
      find = true;
    }
  })
  if (!find){
    props.setOrderBy({ id: 'default', value: 'Par défaut'})
  }
  router.replace({
    path: navRoute.path,
    query: Object.assign({}, navRoute.query, { orderBy: e })
  })
}

</script>

<template>
  <div class="orderByParent">
    <div class="orderBy">
      <label>Trier par:</label>
      <v-select
        :items="order"
        :model-value="props.orderBy"
        item-title="value"
        item-value="id"
        @update:modelValue="changeOrder($event)"
      ></v-select>
    </div>
  </div>
</template>