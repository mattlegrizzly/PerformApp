<template>
    <div :id="id">
        <div class="range_div">
            <ion-label class="title_range">{{ title }}</ion-label>
            <div class="range_container">
                <p>{{ descriptionStart }}</p>
                <p>{{ descriptionEnd }}</p>
            </div>
        </div>
        <div class="range_inner">
            <ion-range :value="value" :aria-label="title" :ticks="true" :snaps="true" :min="min" :max="max"
                :disabled="disabled" @ionChange="handleChange"></ion-range>
        </div>
    </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from 'vue';
import { IonLabel, IonRange } from '@ionic/vue';

//@ts-expect-error
const props = defineProps({
    id: {
        type: String,
        default: ''
    },
    title: {
        type: String,
        required: true
    },
    value: {
        type: Number,
        required: true
    },
    min: {
        type: Number,
        default: 0
    },
    max: {
        type: Number,
        default: 10
    },
    disabled: {
        type: Boolean,
        default: false
    },
    descriptionStart: {
        type: String,
        required: true
    },
    descriptionEnd: {
        type: String,
        required: true
    }
});

const emits = defineEmits(['change']);

const handleChange = (event: any) => {
    emits('change', event);
};
</script>

<style scoped>
.range_div {
    margin-bottom: 10px;
}

.range_container {
    display: flex;
    justify-content: space-between;
}

.range_inner {
    margin-top: 5px;
}
</style>
