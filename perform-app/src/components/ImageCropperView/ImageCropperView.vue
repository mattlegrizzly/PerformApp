<template>
  <ion-modal id="cropImage" :is-open="isOpen" @ionModalDidDismiss="dismiss">
    <div class="modal-content">
      <h2>Recadrer votre photo</h2>
        <img v-if="imageSrc" :src="imageSrc" ref="image" class="cropper-image" />
      <ion-button style="margin-top: 20px" @click="cropAndCompressImage">Recadrer et Compresser</ion-button>
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
      disableTransitions();
    });
})

function initializeCropper() {
  if (cropper.value) {
    cropper.value.destroy();
  }
  const imageElement = image.value;
  if (imageElement) {
    cropper.value = new Cropper(imageElement, {
      aspectRatio: 1,
      guides: false,
      center: true,
      highlight: false,
      toggleDragModeOnDblclick: false,
      background: false,
      zoomOnTouch: true,
      zoomOnWheel: true,
      checkCrossOrigin: true,
      movable: true,
      responsive: true,
      transition: false,
      cropBoxResizable: true, // Désactive le redimensionnement en cliquant
  cropBoxMovable: true,    // Permet de déplacer la cropper box
  zoomable: false,          // Permet de zoomer
  scalable: true,          // Permet de redimensionner
  viewMode: 1,             // Ajustez selon vos besoins
  autoCropArea: 1,         // Ajustez selon vos besoins
  minContainerHeight: 500,
  minContainerHeight: 300,
  dragMode: 'move'         // Permet de déplacer l'image
    });
  }
}

async function cropAndCompressImage() {
  if (cropper.value) {
    const croppedCanvas = cropper.value.getCroppedCanvas({
      width: 300,
      height: 300,
      imageSmoothingQuality: 'high',
    });
    croppedCanvas.toBlob(async (blob) => {
      const compressedBlob = await imageCompression(blob, {
        maxSizeMB: 1,
        maxWidthOrHeight: 300,
        useWebWorker: true,
      });
      const file = new File([compressedBlob], 'croppedImage.jpg', { type: 'image/jpeg' });
      var sizeInMB = (file.size / (1024*1024)).toFixed(2);
      emit('image-cropped', { file, url: URL.createObjectURL(compressedBlob) });
      dismiss();
    }, 'image/jpeg');
  }
}

function disableTransitions() {
  setTimeout(() => {
    const modalContent = document.querySelector('.cropper-container');
    if (modalContent) {
      const cropperElements = modalContent.querySelectorAll('.cropper-container *');
      cropperElements.forEach(el => {
        el.style.transition = 'none';
      });
    }
  }, 200)
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
#cropImage {
  --max-height : 70%;
}

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