<script setup>
import router from '@/router';
import { defineProps } from 'vue';
import { onMounted } from 'vue';

const props = defineProps(['headerTable', 'contentTable', 'limitData', 'nav'])

const navigate = (index) => {
  console.log(index)
  router.push('/'+props.nav+'/show/' + index)
}

</script>

<template>
    <v-table>
        <thead>
        <tr class="table-head-template" >
            <th class="text-left" v-for="(item, index) in props.headerTable" :key="item.name" >
                {{headerTable[index]}}
            </th>
        </tr>
        </thead>
        <tbody>
            <tr class="item-table" v-for="(row, index) in props.contentTable" :key="index" >
              <template v-for="(value, key, i) in row" >
                    <td @click="navigate(row.id)" v-if="i < props.limitData" :key="key">{{ value }}</td>
                </template>
            </tr>
        </tbody>
    </v-table>
</template>

<style>
.item-table {
  transition: 0.3s;
}

.item-table:hover {
  transition: 0.3s;
  background-color: rgb(246, 246, 246);
}


.item-table{ 
  transition: 0.3s;
}

.item-table:hover td{ 
  text-decoration: underline;
  transition: 0.3s;
  color: var(--primary-blue);
}


</style>