<template lang="">
  <NavMenu />
  <div class="mainWrapper">
    <AlertComponents :message_alert='error_message' :type='"error"' :title='error_title' :alertValue="alertErr"/>
    <div class="headerBtns">
      <NavButton class='returnBtn' :text="'Retour'" :url="'/sports'" :back='"back"'/>
      <NavButton class='editBtn' :text="'Modifier'" :url="'/sports/edit/'+ sport.id"/>
    </div>
    <h1>Carte de l'utilisateur : {{ sport === undefined ? '': sport.email }}</h1>
    <h2 class="showTitle">Titre</h2>
    <p>
      {{sport.name}}
    </p>
  </div>
</template>
<script setup lang="ts">

import NavMenu from '@/components/NavMenu.vue'
import { ref } from 'vue'
import { get } from '@/lib/callApi'
import { useRoute } from 'vue-router'
import { onMounted } from 'vue'
import NavButton from '@/components/NavButton.vue'
import AlertComponents from '@/components/AlertComponents.vue'

const router = useRoute()
const sport = ref('')

const alertErr = ref(false)
const error_message = ref('')
const error_title = ref('')

const getUser = async () => {
 const id = router.params.sport_id;
  const res = await get('/admin/users_all/1')
  if(res.status === 404) {
    error_title.value = 'Error while retrieve Material id ' + id
    error_message.value = res.data.detail
    alertErr.value = true
  } else {
    sport.value = await res;
  }
}

onMounted(() => {
  getUser()
})
</script>
<style>

.showTitle {
  text-align: left !important;
  margin-bottom : 0px !important;
  margin-top : 10px !important;
}

.headerBtns {
  margin-top : 10px;
  display : flex;
  justify-content: space-between;
  padding-right : 10px;
}
</style>
