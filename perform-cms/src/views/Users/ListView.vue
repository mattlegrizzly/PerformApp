<script setup lang="ts">
import NavMenu from '@/components/NavMenu.vue'
import ListElement from '@/components/ListElement.vue'
import NavButton from '@/components/NavButton.vue'
import { ref, onMounted } from 'vue'
import { get } from '@/lib/callApi'
import router from '@/router'
import { useRoute } from 'vue-router'
import PaginationComponent from '@/components/PaginationComponent.vue'

const users = ref({})
//Refs pour la pagination
const usersCount = ref(0)
const itemsPerPage = ref(10)
const pagination = ref(0)
const page = ref(1)


const getUsers = async () => {
  const res = await get('/admin/users_all', {
    body: {},
    itemsPerPage: itemsPerPage.value,
    page: page.value
  })
  users.value = await res.results
  usersCount.value = res.count
  pagination.value = Math.ceil(usersCount.value / itemsPerPage.value)
}

const setPage = (value : number) => {
  page.value = value;
}

onMounted(() => {
  getUsers();
})

</script>
<style lang=""></style>

<template lang="">
  <NavMenu />

  <div class="mainWrapper">
    <h1>Users</h1>
    <div>
      <NavButton url="/users/add" text="Ajouter" />
     
    </div>
    <div>
      <ListElement :headerTable="['Id', 'Nom']" :contentTable="users" :limitData="2" nav="users"/>
      <PaginationComponent :setPage='setPage' :page='page' :getData='getUsers' :pagination='pagination' />

    </div>
  </div>
</template>
