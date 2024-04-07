<script setup>
import { defineProps } from 'vue';
import { onMounted } from 'vue';

const props = defineProps(['headerTable', 'contentTable', 'limitData'])

onMounted(() => {
  console.log(props.contentTable);
})
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
            <tr class="item-table" v-for="(row, index) in props.contentTable" :key="index">
              <template v-for="(value, key, i) in row">
                    <td v-if="i < props.limitData" :key="key">{{ value }}</td>
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
  box-shadow: 0px 0px 3px gray;
  transition: 0.3s;
  font-size: 15px;
}
</style>