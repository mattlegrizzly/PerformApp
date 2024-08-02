<template lang="">
  <NavMenu />
  <div class="mainWrapper">
    <AlertComponents
      :message_alert="error_message"
      :type="'error'"
      :title="error_title"
      :alertValue="alertErr"
      :setAlertValue="setAlertValue"
    />
    <div class="headerBtns">
      <NavButton
        class="returnBtn"
        :text="'Retour'"
        :url="'/records_theme'"
        prepend-icon="mdi-arrow-left"
      />
      <NavButton
        class="editBtn"
        :text="'Ajouter un record'"
        :url="'/records_theme/add_record/' + sport.id"
        prepend-icon="mdi-medal"
      />
    </div>
    <h2 class="showTitle">{{ sport.name }}</h2>
    <div class="recordList">
      <h3>Les records du Theme :</h3>
      <v-list-item v-for="(item, i) in record" :key="i" :value="item" color="primary">
        <template v-slot:append>
          <v-dialog max-width="500">
            <template v-slot:activator="{ props: activatorProps }">
              <v-icon  @click='() => {recordEdit = item}' v-bind="activatorProps" icon="mdi-pencil"></v-icon>
            </template>

            <template v-slot:default="{ isActive }">
              <v-card title="Modifier le nom">
                <v-card-text> </v-card-text>
                <div style="margin-left: 20px; margin-right: 20px">
                  <v-text-field
                    label="Nom du record"
                    v-model="recordEdit.name"
                  ></v-text-field>
                </div>

                <v-card-actions>
                  <v-spacer></v-spacer>

                  <v-btn variant="tonal" text="Annuler" @click="isActive.value = false"></v-btn>
                  <v-btn
                    variant="outlined"
                    text="Modifier"
                    @click="
                      () => {

                        patch(
                          '/admin/records/' + recordEdit.id + '/',
                          {
                            body: {
                              name: recordEdit.name
                            }
                          },
                          true
                        ).then((res) => {
                          console.log(res)
                          if (res.status > 301) {
                            error_title = 'Error while retrieve edit record id ' + id.value
                            error_message = res.data.detail
                            alertErr = true
                          } else {
                            isActive.value = false
                            alertSuc = true
                            success_message = 'Record modifié'
                          }
                        })
                      }
                    "
                  ></v-btn>
                </v-card-actions>
              </v-card>
            </template>
          </v-dialog>
          <DeleteModalComponent
            :item="name"
            url="/admin/records"
            :id="item.id"
            :list="''"
            isIcon="oui"
            @dialogClosed="handleDialogClosed"
          />
        </template>
        <v-list-item-title style="margin-bottom: 10px" v-text="item.name"></v-list-item-title>
        <v-divider></v-divider>
      </v-list-item>
    </div>
  </div>
</template>
<script setup lang="ts">
import NavMenu from '@/components/NavMenu/NavMenu.vue'
import { ref } from 'vue'
import { get, patch} from '@/lib/callApi'
import { useRoute } from 'vue-router'
import { onMounted } from 'vue'
import NavButton from '@/components/NavButton/NavButton.vue'
import AlertComponents from '@/components/AlertComponents/AlertComponents.vue'
import DeleteModalComponent from '@/components/DeleteModalComponent/DeleteModalComponent.vue'

const router = useRoute()
const sport = ref('')
const record = ref([
  {
    name: '',
    title: ''
  }
])

const recordEdit = ref ('')
const back = ref('back')

const alertErr = ref(false)
const error_message = ref('')
const error_title = ref('')

const setAlertValue = (type: string) => {
  if (type === 'error') {
    alertErr.value = false
  } else {
  }
}

const handleDialogClosed = () => {
  console.log('handle close')
  getSport()
}

const getSport = async () => {
  const id = router.params.sport_id
  const res = await get('/admin/sports/' + id + '/')
  if (res.status === 404) {
    error_title.value = 'Erreur à la récupération du Material avec pour id ' + id
    error_message.value = res.data.detail
    alertErr.value = true
  } else {
    sport.value = await res

    const res_record = await get('/admin/records/by-sport?sport_id=' + id)
    if (res_record.status === 404) {
      error_title.value = 'Erreur à la récupération du Material avec pour id ' + id
      error_message.value = res_record.data.detail
      alertErr.value = true
    } else {
      record.value = await res_record
      console.log(record.value)
    }
  }
}

onMounted(() => {
  if (router.query.edit) {
    back.value = ''
  } else {
    back.value = 'back'
  }
  getSport()
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
