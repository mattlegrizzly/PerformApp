<template>
    <div class="gauge">
      <div
        class="gauge-fill"
        :style="{ width: `${(value / max) * 100}%`, background: gradient }"
      ></div>
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue';
  
  const props = defineProps({
    value: {
      type: Number,
      required: true,
      validator: val => val >= 0 && val <= 10
    }
  });
  
  const max = 10;
  
  const gradient = computed(() => {
    if (props.value <= 3) return '#71dc23';
    if (props.value <= 6) return '#ecce13';
    return '#E62D1B';
  });
  </script>
  
  <style scoped>
  .gauge {
    width: 100%;
    height: 10px;
    background-color: #e0e0e0;
    border-radius: 5px;
    overflow: hidden;
  }
  
  .gauge-fill {
    height: 100%;
    transition: width 0.3s ease-in-out;
  }
  </style>