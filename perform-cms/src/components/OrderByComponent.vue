<script setup lang="ts">
import router from '@/router'
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'

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

const changeOrder = (e) => {
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

onMounted(() => {
  console.log(props.orderBy)
})
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

<style>

.orderBy {
  width: 400px;
  right: 0px;
}

.orderBy .v-field__field {
  height: 40px;
  display: flex;
  align-items: center;
}


.orderBy .v-field__field .v-field__input {
  padding: 0px !important;
  padding-left: 20px !important;
  font-size: 14px;
}

.orderByParent {
  display: flex;
  justify-content: end;
}

.orderBy .v-input .v-input__details {
  display: none;
}
</style>
