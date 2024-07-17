<template>
  <ion-modal :is-open="isOpen" @ionModalDidDismiss="dismiss">
    <div class="modal-content">
      <h2>Recadrer votre photo</h2>
        <img v-if="imageSrc" :src="imageSrc" ref="image" class="cropper-image" />
      <ion-button @click="cropAndCompressImage">Recadrer et Compresser</ion-button>
    </div>
  </ion-modal>
</template>

<script setup>
import { ref, watch, nextTick, onUnmounted } from 'vue';
import Cropper from 'cropperjs';
import imageCompression from 'browser-image-compression';
import { IonModal, IonButton } from '@ionic/vue';
import 'cropperjs/dist/cropper.css'

const props = defineProps({
  isOpen: Boolean,
  imageSrc: String,
});

const emit = defineEmits(['update:isOpen', 'image-cropped']);
const image = ref(null);
const cropper = ref(null);

watch(() => image.value, (newValue) => {
  nextTick(() => {
      initializeCropper();
    });
})

function initializeCropper() {
  if (cropper.value) {
    cropper.value.destroy();
  }
  console.log(image.value)
  const imageElement = image.value;
  if (imageElement) {
    cropper.value = new Cropper(imageElement, {
      aspectRatio: 1,
      viewMode: 1,
      dragMode: 'move',
      guides: true,
      center: true,
      highlight: false,
      scalable: true,
      cropBoxResizable: false,
      toggleDragModeOnDblclick: true,
      background: false,
      zoomOnTouch: true,
      zoomOnWheel: true,
      checkCrossOrigin: true,
      cropBoxMovable: true,
      zoomable: true,
      movable: true,
      responsive: true,
      scalable: true,
    });
  }
}

async function cropAndCompressImage() {
  console.log(cropper.value)
  if (cropper.value) {
    const croppedCanvas = cropper.value.getCroppedCanvas({
      width: 300,
      height: 300,
      imageSmoothingQuality: 'high',
    });
    console.log('croppedCanvas 2 ' , croppedCanvas)
    croppedCanvas.toBlob(async (blob) => {
      const compressedBlob = await imageCompression(blob, {
        maxSizeMB: 1,
        maxWidthOrHeight: 300,
        useWebWorker: true,
      });
      console.log("blob ", blob)
      emit('image-cropped', { blob: compressedBlob, url: URL.createObjectURL(compressedBlob) });
      console.log('emit ', blob)
      dismiss();
    }, 'image/jpeg');
  }
}

function dismiss() {
  if (cropper.value) {
    cropper.value.destroy();
  }
  emit('update:isOpen', false);
}

onUnmounted(() => {
  if (cropper.value) {
    cropper.value.destroy();
  }
});
</script>

<style scoped>
.modal-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.cropper-image {
  display: block;
  max-width: 100%;
  height: 300px !important;
}
</style>