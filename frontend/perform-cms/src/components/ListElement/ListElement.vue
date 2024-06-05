<script setup>
import router from '@/router'
import { defineProps } from 'vue'
import { onMounted } from 'vue'
import './index.css'
const props = defineProps(['headerTable', 'contentTable', 'limitData', 'nav'])

const navigate = (index) => {
  router.push('/' + props.nav + '/show/' + index)
}
</script>

<template>
  <v-table>
    <thead>
      <tr class="table-head-template">
        <th class="text-left" v-for="(item, index) in props.headerTable" :key="item.name">
          {{ headerTable[index] }}
        </th>
      </tr>
    </thead>
    <tbody>
      <tr class="item-table" v-for="(row, index) in props.contentTable" :key="index">
        <template v-for="(value, key, i) in row">
          <td @click="navigate(row.id)" v-if="i < props.limitData" :key="key">
            <v-img
              v-if="key === 'pictures'"
              :width="60"
              aspect-ratio="16/9"
              cover
              :src="value"
            ></v-img>

            <div v-else>
              <div v-if="i == 0">
                {{ index + 1 }}
              </div>
              <div v-else>
                {{ value }}
              </div>
            </div>
          </td>
        </template>
      </tr>
    </tbody>
  </v-table>
</template>
