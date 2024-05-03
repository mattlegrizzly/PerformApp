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
      <NavButton
        class="returnBtn"
        :text="'Retour'"
        :url="'/materials'"
        :back="back"
        prepend-icon="mdi-arrow-left"
      />
      <NavButton
        class="editBtn"
        :text="'Modifier'"
        :url="'/materials/edit/' + material.id"
        prepend-icon="mdi-pencil"
      />
    </div>
    <h1>Carte du matériel : {{ material === undefined ? '' : material.name }}</h1>
    <h2 class="showTitle">Titre</h2>
    <p>{{ material === undefined ? '' : material.name }}</p>
    <h2 class="showTitle">Image</h2>
    <div class="imageDiv">
      <v-img :width="300" aspect-ratio="16/9" cover :src="material.pictures"></v-img>
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
const material = ref('')

const back = ref('')

const alertErr = ref(false)
const error_message = ref('')
const error_title = ref('')

const getMaterial = async () => {
  const id = router.params.material_id
  const res = await get('/admin/materials/' + id + '/')
  if (res.status === 404) {
    error_title.value = 'Error while retrieve Material id ' + id
    error_message.value = res.data.detail
    alertErr.value = true
  } else {
    material.value = await res
  }
}

onMounted(() => {
  if (router.query.edit) {
    back.value = ''
  } else {
    back.value = 'back'
  }
  getMaterial()
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
