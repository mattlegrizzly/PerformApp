<template>
    <div class="div_user_info">
        <h3>{{ title }} :</h3>
        <p v-for="(item, index) in infoArray" :key="index">{{ item }}</p>
        <p v-if="infoArray && infoArray.length > 2">...</p>
    </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';
import { computed } from 'vue';

const props = defineProps({
    title: String,
    info: [String, Array]
});

const infoArray = computed(() => {
    if (typeof props.info === 'string') {
        return [props.info];
    }
    return props.info;
});
</script>

<style scoped>
.div_user_info {
    width: 30%;
}


.div_user_info h3 {
    margin-top: 0px;
    text-decoration: underline;
    font-size: 13px;
    text-align: center;
    font-weight: 700;
}

.div_user_info p {
    text-align: center;
}
</style>