<template>
  <div>
    <v-icon v-if='props.isIcon' @click="dialog = true"  icon="mdi-delete"></v-icon>
    <v-btn v-else @click="dialog = true" prepend-icon="mdi-delete"> Delete </v-btn>
    <v-dialog v-model="dialog" max-width="400" persistent>
      <v-card class="delete_modal">
        <v-card-title>Vous allez supprimer : {{ props.item }}</v-card-title>
        <v-card-text>Êtes vous sûre de vouloir supprimer cet élément ?</v-card-text>
        <template v-slot:actions>
          <v-spacer></v-spacer>

          <v-btn variant="outlined" @click="dialog = false"> Annuler </v-btn>

          <v-btn id="delete_btn" @click="deleteElement"> Supprimer </v-btn>
        </template>
      </v-card>
    </v-dialog>
  </div>
</template>
<script setup lang="ts">
import { ref, defineEmits} from 'vue'
import { del } from '@/lib/callApi'
import router from '@/router'
const props = defineProps(['url', 'item', 'id', 'list', 'isIcon'])
const emit = defineEmits(['dialogClosed']);
const dialog = ref(false)

const deleteElement = () => {
  const url = props.url + '/' + props.id + '/'
  del(url, true).then((res) => {
    if (res.status > 301) {
      throw Error
    } else {
      if(props.list !="") { 
        router.push('/' + props.list)
      } else {
        dialog.value = false
        emit('dialogClosed');
      }
    }
  })
}
</script>

<style scoped>
.v-card-title {
  white-space: normal !important;
}

#delete_btn {
  background-color: var(--primary-red);
  color: #ffffff;
}
</style>
