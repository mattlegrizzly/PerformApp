<template>
  <div class="gauge">
    <div class="gauge-fill"></div>
    <div v-for="i in max-1" :key="i" class="gauge-tick" :style="{ left: `${(i / max) * 100}%` }"></div>
    <div class="gauge-indicator" :style="{ left: `${(value / max) * 100}%` }"></div>
  </div>
</template>

<script setup>
const props = defineProps({
  value: {
    type: Number,
    required: true,
    validator: val => val >= 0 && val <= 10
  }
});

const max = 10;
</script>

<style scoped>
.gauge {
  position: relative;
  width: 100%;
  height: 5px;
  background-color: #e0e0e0;
  margin-top: 5px;
}

.gauge-fill {
  position: absolute;
  border-radius: 15px;
  width: 100%;
  height: 100%;
  background: linear-gradient(to right, green, yellow, red);
  z-index: 1;
}

.gauge-tick {
  position: absolute;
  top: -1px; /* Légèrement au-dessus de la jauge */
  bottom: -1px; /* Légèrement en dessous de la jauge */
  width: 1px;
  background-color: rgb(254, 254, 254);
  z-index: 2;
}

.gauge-indicator {
  position: absolute;
  top: -3px; /* Légèrement au-dessus de la jauge */
  bottom: -3px; /* Légèrement en dessous de la jauge */
  width: 11px;
  box-shadow: 0px 0px 10px rgb(179, 179, 179);
  background-color: white;
  border-radius: 50%;
  transform: translateX(-50%);
  z-index: 3;
}
</style>
