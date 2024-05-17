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


/* Theme variables */
//import './theme/variables.css';

const app = createApp(App).use(IonicVue).use(router);

router.isReady().then(() => {
    app.mount('#app');
});