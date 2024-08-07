import { createApp } from 'vue';
import { IonicVue } from '@ionic/vue';

import App from './App.vue';
import router from './router';

import i18n from './i18n';

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
import trainerSelected from './assets/icons/PersonalTrainerFill.svg'
import program from './assets/icons/Programs.svg'
import programSelected from './assets/icons/ProgramsFill.svg'

//Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { aliases, mdi } from 'vuetify/iconsets/mdi'

import { createAnimation } from '@ionic/core';

import { ScreenOrientation } from '@ionic-native/screen-orientation';

// Enregistrement de l'icône
addIcons({
    'profile': profile,
    'home': home,
    'exercise': exercise,
    'profile-selected': profileSelected,
    'home-selected': homeSelected,
    'exercise-selected': exerciseSelected,
    'trainer': trainer,
    'trainer-selected': trainerSelected,
    'program': program,
    'program-selected': programSelected,
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

// Définir les animations
//@ts-expect-error
const slideAnimation = (baseEl: any, opts: any) => {

    const enteringEl = opts.enteringEl;
    const leavingEl = opts.leavingEl;

    const animation = createAnimation()
        .addElement(enteringEl)
        .duration(200)
        .fromTo('transform', 'translateY(100%)', 'translateY(0)');

    if (leavingEl) {
        animation.addElement(leavingEl)
            .duration(200)
            .fromTo('transform', 'translateY(0)', 'translateY(-100%)');
    }

    return animation;
};

// Définir les animations
//@ts-expect-error
const slideLeftAnimation = (baseEl: any, opts: any) => {
    const enteringEl = opts.enteringEl;
    const leavingEl = opts.leavingEl;

    const animation = createAnimation()
        .addElement(enteringEl)
        .duration(200)
        .fromTo('transform', 'translateX(100%)', 'translateX(0)');

    if (leavingEl) {
        animation.addElement(leavingEl)
            .duration(200)
            .fromTo('transform', 'translateX(0)', 'translateX(-100%)');
    }

    return animation;
};

// Définir les animations
//@ts-expect-error
const slideRightAnimation = (baseEl: any, opts: any) => {
    const enteringEl = opts.enteringEl;
    const leavingEl = opts.leavingEl;

    const animation = createAnimation()
        .addElement(enteringEl)
        .duration(100)
        .fromTo('transform', 'translateX(-100%)', 'translateX(0)');

    if (leavingEl) {
        animation.addElement(leavingEl)
            .duration(100)
            .fromTo('transform', 'translateX(0)', 'translateX(100%)');
    }

    return animation;
};

//@ts-expect-error
const fadeAnimation = (baseEl: any, opts: any) => {
    const enteringEl = opts.enteringEl;
    const leavingEl = opts.leavingEl;
  
    const animation = createAnimation()
      .addElement(enteringEl)
      .duration(300)
      .fromTo('opacity', '0', '1');
  
    if (leavingEl) {
      const leavingAnimation = createAnimation()
        .addElement(leavingEl)
        .duration(300)
        .fromTo('opacity', '1', '0');
  
      animation.addAnimation([leavingAnimation]);
    }
  
    return animation;
  };

//@ts-expect-error
const userLang = navigator.language || navigator.userLanguage

const app = createApp(App).use(vuetify).use(router);

//Cet objet va permettre de définir les différentes animations en fonction de l'entrée (gauche) et la page de sortie (droite)
const pageTransitions = {
    'Home': slideAnimation,
    'Login': fadeAnimation,
    'ExerciseView|Exercises': slideLeftAnimation,
    'Exercises|ExerciseView': slideRightAnimation,
    'list-injuries|profile': slideLeftAnimation,
    'profile|list-injuries': slideRightAnimation,
    'add-injuries|list-injuries': slideLeftAnimation,
    'list-injuries|add-injuries': slideRightAnimation,
    'show-injuries|list-injuries': slideLeftAnimation,
    'list-injuries|show-injuries': slideRightAnimation,
    'edit-injuries|show-injuries': slideLeftAnimation,
    'show-injuries|edit-injuries': slideRightAnimation,
    'profile|show-injuries': slideRightAnimation,
    'show-injuries|profile': slideLeftAnimation,
    'edit-profile|profile': slideLeftAnimation,
    'profile|edit-profile': slideRightAnimation,
    'Splash': fadeAnimation,
    'Home|Splash': fadeAnimation,
    'Records|profile': slideLeftAnimation,
    'profile|Records': slideRightAnimation,
    'Records|ShowRecords': slideRightAnimation,
    'ShowRecords|Records': slideLeftAnimation,
    'Coaching|AddWorkout': slideRightAnimation,
    'AddWorkout|Coaching': slideLeftAnimation,
    'Coaching|ShowWorkout': slideRightAnimation,
    'ShowWorkout|Coaching': slideLeftAnimation,
    'ShowWorkout|EditWorkout': slideRightAnimation,
    'EditWorkout|ShowWorkout': slideLeftAnimation
};


app.use(IonicVue, {
    animated: true,
    navAnimation: (baseEl: any, opts: any) => {
        // Utiliser des animations conditionnelles selon l'attribut data-page
        const enteringPage = opts.enteringEl.getAttribute('data-page');
        const leavingPage = opts.leavingEl?.getAttribute('data-page') || '';
        const transitionKey = `${enteringPage}|${leavingPage}`;
        //@ts-expect-error
        const animationFunction = pageTransitions[transitionKey] || slideAnimation;

        return animationFunction(baseEl, opts);
    }
});

app.use(i18n)

app.config.globalProperties.$locale = userLang

router.isReady().then(() => {
    app.mount('#app');
});

document.addEventListener('deviceready', () => {
    ScreenOrientation.lock(ScreenOrientation.ORIENTATIONS.PORTRAIT);
  }, false);