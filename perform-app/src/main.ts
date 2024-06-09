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

import { createAnimation } from '@ionic/core';

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

// Définir les animations
const slideAnimation = (baseEl, opts) => {
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
const slideLeftAnimation = (baseEl, opts) => {
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
const slideRightAnimation = (baseEl, opts) => {
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

const fadeAnimation = (baseEl, opts) => {
    const enteringEl = opts.enteringEl;
    const leavingEl = opts.leavingEl;

    const animation = createAnimation()
        .addElement(enteringEl)
        .duration(100)
        .fromTo('opacity', 0, 1);

    if (leavingEl) {
        animation.addElement(leavingEl)
            .duration(100)
            .fromTo('opacity', 1, 0);
    }

    return animation;
};

const app = createApp(App).use(vuetify).use(router);

app.use(IonicVue, {
    animated: true,
    navAnimation: (baseEl, opts) => {
        console.log('entering ', opts.enteringEl.getAttribute('data-page'))
        console.log('leaving ', opts.leavingEl.getAttribute('data-page'))
        // Utiliser des animations conditionnelles selon l'attribut data-page
        if (opts.enteringEl.getAttribute('data-page') === 'Home') {
            return slideAnimation(baseEl, opts);
        } else if (opts.enteringEl.getAttribute('data-page') === "ExerciseView" && opts.leavingEl.getAttribute('data-page') === "Exercises") {
            return slideLeftAnimation(baseEl, opts);
        } else if (opts.leavingEl.getAttribute('data-page') === "ExerciseView" && opts.enteringEl.getAttribute('data-page') === "Exercises") {
            return slideRightAnimation(baseEl, opts);
        } else {
            return slideAnimation(baseEl, opts)
        }
    }
});

router.isReady().then(() => {
    app.mount('#app');
});