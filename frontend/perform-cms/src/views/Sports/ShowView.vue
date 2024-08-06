<template>
  <NavMenu />
  <div class="mainWrapper">
    <!-- Alert Component -->
    <AlertComponents
      :message_alert="error_message"
      :type="'error'"
      :title="error_title"
      :alertValue="alertErr"
      :setAlertValue="setAlertValue"
    />

    <!-- Navigation Buttons -->
    <div class="headerBtns">
      <NavButton
        class="returnBtn"
        :text="'Retour'"
        :url="'/records_sports'"
        prepend-icon="mdi-arrow-left"
      />
      <NavButton
        class="editBtn"
        :text="'Ajouter un record'"
        :url="'/sports/add_record/' + sport.id"
        prepend-icon="mdi-medal"
      />
    </div>

    <!-- Sport Title -->
    <h2 class="showTitle">{{ sport.name }}</h2>

    <!-- Record List -->
    <div class="recordList">
      <h3>Les records du sport :</h3>
      <div v-for="(items, category) in record" :key="category">
        <div style="display:  flex; justify-content: space-between;">
          <h3 style="margin-top: 0px">{{ showCategoryName(category).name }}</h3>
          {{  console.log (showCategoryName(category)) }}
          <DeleteModalComponent
          v-if="showCategoryName(category).show == true"
                  :item="showCategoryName(category).name"
                  url="/record_group"
                  :id="showCategoryName(category).id"
                  :list="''"
                  isIcon="oui"
                  @dialogClosed="handleDialogClosed"
                />
          </div>
          <v-divider style="margin-bottom: 10px;"></v-divider>
        <draggable :list="items" item-key="id" @end="() => updateOrder(category)">
          <template #item="{ element, index }">
            <div id="record" class="record-item">
              <!-- Record Item -->
              <div style="display: flex">
                <v-icon class="drag-handle" left>mdi-drag</v-icon>
                <v-list-item-title
                  style="margin-bottom: 10px"
                  v-text="element.name"
                ></v-list-item-title>
              </div>
              <div style="display: flex; align-items: center">
                <!-- Edit Dialog -->
                <v-icon
                  @click="() => {
                    showEditName = true;
                    recordEdit = element}"
                  icon="mdi-pencil"
                ></v-icon>
                <v-dialog v-model="showEditName" max-width="500" persistent>
                    <v-card title="Modifier le nom">
                      <v-card-text></v-card-text>
                      <div style="margin-left: 20px; margin-right: 20px">
                        <v-text-field
                          label="Nom du record"
                          v-model="recordEdit.name"
                        ></v-text-field>
                        <v-switch
                        v-model="addToGroup"
                        color="primary"
                        label="Ajouter à un groupe ?"
                        value="yes"
                        hide-details
                      ></v-switch>
                      <div v-if="addToGroup">
                        <div class="inputFormDiv addView">
                          <div style="display: flex; align-items : center; width: 100%">
                            <v-select
                              v-model="group_selected"
                              :items="groups"
                              hint="Sélectionnez le groupe à utiliser"
                              item-title="name"
                              item-value="id"
                              label="Groupe"
                            />
                          </div>
                        </div>
                      </div>
                      </div>
                      
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                          variant="tonal"
                          text="Annuler"
                          @click="showEditName = false"
                        ></v-btn>
                        <v-btn
                          variant="outlined"
                          text="Modifier"
                          @click="updateRecord(recordEdit)"
                        ></v-btn>
                      </v-card-actions>
                    </v-card>
                </v-dialog>

                <!-- Delete Modal Component -->
                <DeleteModalComponent
                  :item="element.name"
                  url="/admin/records"
                  :id="element.id"
                  :list="''"
                  isIcon="oui"
                  @dialogClosed="handleDialogClosed"
                />

                <!-- Move Buttons -->
                <v-btn
                  icon="mdi-arrow-up"
                  @click="moveUp(index, items, category)"
                  :disabled="index === 0"
                ></v-btn>
                <v-btn
                  icon="mdi-arrow-down"
                  @click="moveDown(index, items, category)"
                  :disabled="index === items.length - 1"
                ></v-btn>
              </div>
            </div>
          </template>
        </draggable>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface RecordItem {
  id: number;
  name: string;
  order: number;
  // autres propriétés éventuelles
}

type RecordMap = {
  [category: string]: RecordItem[];
}

import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import NavMenu from '@/components/NavMenu/NavMenu.vue'
import NavButton from '@/components/NavButton/NavButton.vue'
import AlertComponents from '@/components/AlertComponents/AlertComponents.vue'
import DeleteModalComponent from '@/components/DeleteModalComponent/DeleteModalComponent.vue'
import draggable from 'vuedraggable'
import { get, patch } from '@/lib/callApi'

const showEditName = ref(false)
const router = useRoute()
const sport = ref({
  name:'', 
  id:0
})
const record = ref<RecordMap>({});
const recordConst = ref<RecordMap>({});
const recordEdit = ref({
  name: '',
  id: 0,
  order: 0
})
const alertErr = ref(false)
const error_message = ref('')
const error_title = ref('')
const groups = ref('') as any
const group_selected = ref(null)
const addToGroup = ref(false)

// Fonction pour définir l'état d'alerte
const setAlertValue = (type: string) => {
  if (type === 'error') {
    alertErr.value = false
  }
}

// Fonction pour gérer la fermeture du dialogue de suppression
const handleDialogClosed = () => {
  getSport()
}

const getGroups = async () => {
  await get('/record_group/by-sport/?sport_id=' + sport.value.id).then((res) => {
    if (res.status > 300) {
      error_title.value = 'Erreur à la récupération des groupes'
      error_message.value = res.data.detail
      alertErr.value = true
    } else {
      groups.value = res
      console.log(res)
      console.log(group_selected.value)
      if(group_selected.value == null && res.length > 0){
        group_selected.value = res[0].id
      }
    }
  })
}

// Fonction pour mettre à jour l'ordre des éléments après drag-and-drop
const updateOrder = (category: string | number) => {
  if (!record.value[category] || !recordConst.value[category]) return

  const modifiedRecords = [] as any;

  // Comparer et mettre à jour l'ordre
  record.value[category].forEach((rec: any, index: number) => {
    const original = recordConst.value[category].find((r: any) => r.id === rec.id)
    // Ajuster l'ordre : rec.order (basé sur 1) doit être index + 1 (si les index sont basés sur 0)
    if (original && original.order !== index + 1) {
      rec.order = index + 1
      modifiedRecords.push(rec)
    }
  })

  // Mise à jour des éléments modifiés
  modifiedRecords.forEach(async (rec: any) => {
    const res = await patch(`/admin/records/${rec.id}/`, { body: { order: rec.order } }, true)
    console.log(res)
  })
}

const showCategoryName = (category : any) => {
  let cat = category as string;
  let catSplit = cat.split('_');
  return (catSplit.length > 1 ? {name : catSplit[0], show: true, id: Number(catSplit[1])} : {name : cat, show :false})
} 

// Nouvelle fonction pour mettre à jour un enregistrement spécifique
const updateRecord = async (record: RecordItem ) => {
  const option = {
    name: record.name
  } as any
  if(addToGroup.value){
    option['groups'] = group_selected.value;
  }
  try {
    patch(`/admin/records/${record.id}/`, { body: option}, true).then((res)=> {
      console.log(res)
      if (!res.status) {
        console.log('Record updated successfully:', res)
        showEditName.value = false;
        getSport()
      } else {
        console.error('Failed to update record:', res)
      }
    })
  } catch (error) {
    console.error('Error updating record:', error)
  }
}

// Fonction pour déplacer un élément vers le haut
const moveUp = (index: number, items: any[], category: string | number) => {
  const cat = category as string;
  if (index > 0) {
    const temp = items[index]
    items.splice(index, 1)
    items.splice(index - 1, 0, temp)
    updateOrder(cat)
  }
}

// Fonction pour déplacer un élément vers le bas
const moveDown = (index: number, items: any[], category: string | number) => {
  const cat = category as string;
  if (index < items.length - 1) {
    const temp = items[index]
    items.splice(index, 1)
    items.splice(index + 1, 0, temp)
    updateOrder(cat)
  }
}

// Fonction pour récupérer les données du sport et des records
const getSport = async () => {
  try {
    const id = router.params.sport_id
    const res = await get(`/admin/sports/${id}/`)
    if (res.status === 404) {
      error_title.value = `Erreur à la récupération du sport avec l'id ${id}`
      error_message.value = res.detail
      alertErr.value = true
      return
    }

    sport.value = res

    const res_record = await get(`/admin/records/by-sport?sport_id=${id}`)
    if (res_record.status > 300) {
      error_title.value = `Erreur à la récupération des records pour le sport avec l'id ${id}`
      error_message.value = res_record.detail
      alertErr.value = true
    } else {
      record.value = res_record || {}
      recordConst.value = JSON.parse(JSON.stringify(res_record || {}))
      getGroups();
    }
  } catch (error) {
    console.error('Erreur lors de la récupération des données:', error)
    alertErr.value = true
    error_title.value = 'Erreur à la récupération des données'
    error_message.value = 'Une erreur inconnue est survenue'
  }
}

// Appel de la fonction getSport au montage du composant
onMounted(() => {
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

.mainWrapper {
  padding: 20px;
}

.recordList {
  margin-top: 20px;
}

.v-overlay__scrim {
  background-color: rgba(0, 0, 0, 0.5) !important; /* Noir à 50% de transparence */
}

.v-dialog__content {
  background-color: rgba(255, 255, 255, 0.9); /* Blanc à 90% de transparence pour le contenu du dialogue */
}
</style>
