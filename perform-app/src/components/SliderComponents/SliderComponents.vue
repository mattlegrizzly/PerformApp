<template>
    <div class="sport-programs">
      <swiper style="    padding: 20px 10px 20px 10px;;" :slides-per-view="2.2" :space-between="5"  pagination>
        <swiper-slide v-for="(program, index) in props.programs" :key="index">
            <SquareProgam :program="program" />
        </swiper-slide>
      </swiper>
    </div>
  </template>
  
  <script setup>
  import { ref, defineProps } from 'vue';
  import { Swiper, SwiperSlide } from 'swiper/vue';
import SquareProgam from '../SquareProgram/SquareProgam.vue';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
  const props = defineProps(["programs"]);

  </script>

  <style scoped>
.sport-programs {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;

}

.program-card {
  text-align: center;
  padding: 20px;
  background-color: #f7f7f7;
  border-radius: 10px;
}

.program-photo {
  width: 100%;
  height: auto;
  border-radius: 10px;
}

h3 {
  margin-top: 10px;
  font-size: 1.5em;
}

p {
  margin: 5px 0;
}
</style>