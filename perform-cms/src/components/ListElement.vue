<script lang="ts">
import { defineProps } from 'vue';

export default {
  props: [
    'headerTable',
    'contentTable',
  ],
}

    const props = defineProps({
        
    })
</script>

<template>
    <v-table>
        <thead>
        <tr v-for="item in headerTable" :key="item.name">
            <th class="text-left">
                {{item.name }}
            </th>
        </tr>
        </thead>
        <tbody>
            <tr v-for="(row, index) in contentTable" :key="index">
              <td v-for="(value, key) in row" :key="key">{{ value }}</td>
            </tr>
        </tbody>
    </v-table>
</template>

<style>
</style>