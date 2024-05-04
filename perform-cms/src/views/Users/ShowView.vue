<template lang="">
  <NavMenu />
  <div class="mainWrapper">
    <AlertComponents
      :message_alert="error_message"
      :type="'error'"
      :title="error_title"
      :alertValue="alertErr"
    />
    <div class="headerBtns">
      <NavButton class="returnBtn" :text="'Retour'" :url="'/users'" :back="back" prepend-icon="mdi-arrow-left" />
      <NavButton class="editBtn" :text="'Modifier'" :url="'/users/edit/' + user.id" prepend-icon="mdi-pencil" />
    </div>
    <h1>Carte de l'utilisateur : {{ user === undefined ? '' : user.email }}</h1>
    <h3 class="showTitle">Nom et prénom</h3>
    <p>
      {{ user.last_name + ' ' + user.first_name }}
    </p>
    <h3 class="showTitle">Email</h3>
    <p>
      {{ user.email }}
    </p>
    <h3 class="showTitle">Age</h3>
    <p>
      {{ user.age }}
    </p>
    <h3 class="showTitle">Taille</h3>
    <p>
      {{ user.size }}
    </p>
    <h3 class="showTitle">Poids</h3>
    <p>
      {{ user.weight }}
    </p>
    <h3 class="showTitle">Genre</h3>
    <p>
      {{ userGender }}
    </p>
    <h2 class="showTitle">Sports</h2>
    <v-chip-group v-for="(element, index) in user.sports_user" :key="index">
      <v-chip>{{ element.sport.name }}</v-chip>
    </v-chip-group>
    <div class="imageDiv">
      <v-img :width="300" aspect-ratio="16/9" cover :src="user.profile_picture"></v-img>
    </div>
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
const user = ref({})
const gender = ref([
  { id: 'male', value: 'Homme' },
  { id: 'female', value: 'Femme' },
  { id: 'other', value: 'Autre' }
])
const back = ref('back')

const userGender = ref('')
const alertErr = ref(false)
const error_message = ref('')
const error_title = ref('')

const getUser = async () => {
  const id = router.params.user_id
  const res = await get('/admin/users_all/' + id + '/')
  if (res.status === 404) {
    error_title.value = 'Error while retrieve Material id ' + id
    error_message.value = res.data.detail
    alertErr.value = true
  } else {
    user.value = await res
    gender.value.map((gender) => {
      if (user.value.gender === gender.id) {
        userGender.value = gender.value
      }
    })
  }
}

onMounted(() => {
  if (router.query.edit) {
    back.value = ''
  } else {
    back.value = 'back'
  }
  getUser()
})
</script>
<style>
.showTitle {
  text-align: left !important;
  margin-bottom: 0px !important;
  margin-top: 10px !important;
}

.headerBtns {
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
  padding-right: 10px;
}
</style>
