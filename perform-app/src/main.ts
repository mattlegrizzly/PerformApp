import { createApp } from 'vue';
import { IonicVue } from '@ionic/vue';

import App from './App.vue';
import router from './router';

/* Core CSS required for Ionic components to work properly */
import '@ionic/vue/css/core.css';

/* Basic CSS for apps built with Ionic */
import '@ionic/vue/css/normalize.css';
import '@ionic/vue/css/structure.css';
import '@ionic/vue/css/typography.css';

/* Optional CSS utils that can be commented out */
import '@ionic/vue/css/padding.css';
import '@ionic/vue/css/float-elements.css';
import '@ionic/vue/css/text-alignment.css';
import '@ionic/vue/css/text-transformation.css';
import '@ionic/vue/css/flex-utils.css';
import '@ionic/vue/css/display.css';
import './assets/base.css';
import './assets/main.css';

import { addIcons } from 'ionicons';

// Importation de votre icône personnalisée
import profile from './assets/icons/Profile.svg';
import profileSelected from './assets/icons/ProfileSelected.svg';
import home from './assets/icons/Home.svg';
import homeSelected from './assets/icons/HomeSelected.svg';
import exercise from './assets/icons/Exercices.svg';
import exerciseSelected from './assets/icons/ExercicesSelected.svg';
import trainer from './assets/icons/Personal Trainer.svg'
import program from './assets/icons/Programs.svg'

//Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { aliases, mdi } from 'vuetify/iconsets/mdi'

// Enregistrement de l'icône
addIcons({
    'profile': profile,
    'home': home,
    'exercise': exercise,
    'profile-selected': profileSelected,
    'home-selected': homeSelected,
    'exercise-selected': exerciseSelected,
    'trainer': trainer,
    'program': program,
});

export default createVuetify({
    icons: {
        defaultSet: 'mdi', // This is already the default value - only for display purposes
    },
})

const vuetify = createVuetify({
    components,
    directives,
    icons: {
        defaultSet: 'mdi',
        aliases,
        sets: {
            mdi,
        },
    },
})

const app = createApp(App).use(IonicVue).use(vuetify).use(router);

router.isReady().then(() => {
    app.mount('#app');
});