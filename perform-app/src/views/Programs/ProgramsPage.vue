<style scoped>
.program_page {
  margin-left: var(--pd-l);
    margin-right: var(--pd-r);
}

.program_page h2 {
  font-size: 18px;
  font-weight: 800;
  margin-top: 0px;
  margin-bottom: 0px;
}

.sports_chip ion-chip {
        padding-left: 5px;
        padding-right: 5px;
        height: 25px !important;
        min-height: 0px;
        color: white;
        font-size: 10px;
        background-color: var(--secondary-blue);
        pointer-events: none;
        margin-right : 5px
}

.sports_chip {
  padding-top: 5px;
  padding-bottom: 10px;
}
</style>

<template>
  <ion-page>
    <ion-content>
      <div class="perform-page">
        <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
         Nos programmes
        </h1>
      </div>
      <div class="program_page">
        <h2>Catégories</h2>
        <div class="sports_chip">
          <ion-chip v-for="sport of sports">{{ sport }}</ion-chip>
        </div>
        <h2>Nos meilleurs programmes</h2>
        </div>
        
        <SliderComponents :programs="programs" />
        <div class="program_page">
        <h2>Les programmes recommandés pour vous</h2>
      </div>

        <SliderComponents :programs="programs2" />

    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonContent, IonPage } from  "@ionic/vue";
import "@/assets/base.css";
import "@/assets/main.css";
import { ref } from "vue";
import SliderComponents from "../../components/SliderComponents/SliderComponents.vue";

import { useRouter } from "vue-router";

const sports = ref(['CrossFit', 'Pilate', 'Fitness', 'Boxe'])

const programs = ref([
  {
    "title": "Bootcamp Énergie",
    'sport' : 'Renforcement',
    "description": "Un programme intense qui combine des exercices de cardio, de renforcement musculaire et de haute intensité. Idéal pour ceux qui cherchent à repousser leurs limites.",
    "duration": "4 semaines",
    "price": "120€",
    "photo_url": "https://images.unsplash.com/photo-1534258936925-c58bed479fcb?q=80&w=1931&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  },
  {
    "title": "Yoga Relaxation",
    'sport' : 'Yoga',

    "description": "Un programme de yoga conçu pour améliorer la flexibilité, réduire le stress et renforcer la connexion corps-esprit. Parfait pour débutants et intermédiaires.",
    "duration": "6 semaines",
    "price": "90€",
    "photo_url": "https://images.unsplash.com/photo-1560233075-4c1e2007908e?q=80&w=1915&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  },
  {
    "title": "Fit & Sculpt",
    'sport' : 'Fitness',

    "description": "Ce programme combine des exercices de musculation et de cardio pour sculpter le corps, tonifier les muscles et améliorer l'endurance.",
    "duration": "8 semaines",
    "price": "150€",
    "photo_url": "https://images.unsplash.com/photo-1627483298606-cf54c61779a9?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  },
  {
    "title": "CrossFit Challenge",
    'sport' : 'CrossFit',

    "description": "Un programme de CrossFit pour développer force, agilité et endurance. Idéal pour ceux qui aiment les défis et les entraînements variés.",
    "duration": "5 semaines",
    "price": "130€",
    "photo_url": "https://images.unsplash.com/photo-1536922246289-88c42f957773?q=80&w=2104&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  },
  {
    "title": "Pilates Reforme",
    'sport' : 'Pilate',

    "description": "Un programme de Pilates utilisant des appareils pour un entraînement ciblé et efficace, parfait pour renforcer les muscles profonds et améliorer la posture.",
    "duration": "7 semaines",
    "price": "110€",
    "photo_url": "https://images.unsplash.com/photo-1717500251646-3e661a2ee7e1?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  },
  {
    "title": "Cardio Boxing",
    'sport' : 'Boxe',

    "description": "Un programme de cardio boxing qui mélange techniques de boxe et exercices cardiovasculaires pour brûler des calories et améliorer la coordination.",
    "duration": "6 semaines",
    "price": "100€",
    "photo_url": "https://images.unsplash.com/photo-1606045486656-13a37890dc90?q=80&w=1984&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  }
]
)

const programs2 = ref(
  [
  {
    "titre": "Circuit Training Dynamique",
    "description": "Un programme combinant des exercices de haute intensité et de renforcement musculaire, parfait pour brûler des calories rapidement.",
    "durée": "4 semaines",
    "prix": "130€",
    "photo_url": "https://images.unsplash.com/photo-1516481265257-97e5f4bc50d5?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "sport": "Circuit Training"
  },
  {
    "titre": "Running Endurance",
    "description": "Un programme de course à pied conçu pour améliorer l'endurance et la vitesse, idéal pour les amateurs de running.",
    "durée": "6 semaines",
    "prix": "100€",
    "photo_url": "https://images.unsplash.com/photo-1596460456678-760115935178?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "sport": "Running"
  },
  {
    "titre": "HIIT Fat Burner",
    "description": "Un programme d'entraînement par intervalles de haute intensité pour brûler des graisses et améliorer la condition physique.",
    "durée": "4 semaines",
    "prix": "140€",
    "photo_url": "https://images.unsplash.com/photo-1500468756762-a401b6f17b46?q=80&w=1888&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "sport": "HIIT"
  },
  {
    "titre": "Cyclisme de Montagne",
    "description": "Un programme d'entraînement intensif pour les passionnés de vélo, ciblant la force des jambes et l'endurance.",
    "durée": "8 semaines",
    "prix": "160€",
    "photo_url": "https://images.unsplash.com/photo-1615845522846-02f89af04c2e?q=80&w=1938&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "sport": "Cyclisme"
  },
  {
    "titre": "Danse Fitness",
    "description": "Un programme fun et dynamique mélangeant des mouvements de danse et des exercices de cardio, parfait pour s'amuser tout en restant en forme.",
    "durée": "6 semaines",
    "prix": "90€",
    "photo_url": "https://images.unsplash.com/photo-1611077094726-11cf1f992009?q=80&w=2069&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "sport": "Danse"
  },
  {
    "titre": "Entraînement en Piscine",
    "description": "Un programme complet de natation pour améliorer la technique, l'endurance et la force musculaire.",
    "durée": "7 semaines",
    "prix": "150€",
    "photo_url": "https://images.unsplash.com/photo-1519315901367-f34ff9154487?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "sport": "Natation"
  }
]

)

const router = useRouter()

const goBack = () => router.push('/exercises')

</script>
