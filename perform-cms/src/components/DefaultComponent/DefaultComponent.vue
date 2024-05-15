<script setup>
const props = defineProps(['hint', 'items', 'model', 'title', 'value'])
</script>
<style lang=""></style>

<template lang="">
    <v-select
                :v-model="props.model"
                :items="props.items"
                :hint="props.hint"
                :item-title="props.title"
                :item-value="props.value"
                label="Select"
                multiple
                persistent-hint
                single-line
              >
              </v-select>
</template>
