// src/i18n.js
import { createI18n } from 'vue-i18n';

const messages = {
  en: {
    monthNames: [
      "January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"
    ],
    monthShortNames: [
      "Jan", "Feb", "Mar", "Apr", "May", "Jun",
      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ],
    dayNames: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
    dayShortNames: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    doneText: "Done",
    cancelText: "Cancel"
  },
  fr: {
    monthNames: [
      "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
      "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ],
    monthShortNames: [
      "Jan", "Fév", "Mar", "Avr", "Mai", "Jun",
      "Jul", "Aoû", "Sep", "Oct", "Nov", "Déc"
    ],
    dayNames: ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"],
    dayShortNames: ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"],
    doneText: "Terminé",
    cancelText: "Annuler"
  }
  // Ajoutez d'autres langues ici...
};

const userLang = navigator.language || navigator.userAgent;
const i18n = createI18n({
  legacy: false,
  locale: userLang.split('-')[0] || 'en', // Définir la langue par défaut
  fallbackLocale: 'en', // Langue de repli
  messages, // Messages de traduction
});

export default i18n;
