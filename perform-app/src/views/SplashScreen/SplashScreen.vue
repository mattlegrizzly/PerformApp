<template>
  <ion-page
    class="splash-ion-page"
    style="padding-top: 0px !important"
    data-page="Splash"
  >
    <ion-content style="padding-top: 0px !important" data-page="Splash" id="splash-ion-page">

      <div class="splash-screen">
        <img
          src="@/assets/logo_perform.png"
          alt="Logo"
          ref="logo"
          class="logo"
          @animationend="handleAnimationEnd"
        />
      </div>
    </ion-content>
  </ion-page> 
</template>

<script setup lang="ts">
import { onMounted, ref, onUnmounted } from "vue";
import { IonContent, onIonViewWillEnter, IonPage } from "@ionic/vue";
import { store } from "../../store/store";
import router from "../../router"
import { App } from '@capacitor/app';  // Import correct

const userLogin = ref("");
const logo = ref<HTMLElement | null>(null);
const topCss = ref("");
const logoWidth = ref("");

const checkUserStatus = async () => {
  await store.set("hasLaunched", true);
  if (userLogin.value !== "") {
    router.push("/home");
  } else {
    router.push("/login");
  }
};

const handleAnimationEnd = () => {
  logo.value!.style.top = topCss.value;
  checkUserStatus();
};

// Gestion de la logique de réinitialisation lors de la fermeture
const resetVariableOnColdStart = () => {
  console.log('local storage ', localStorage.getItem('appInBackground'))
  if (!localStorage.getItem('appInBackground')) {
    store.set("hasLaunched", false);
  }
};

const setAppInBackgroundFlag = () => {
  localStorage.setItem('appInBackground', 'true');
};

const clearAppInBackgroundFlag = () => {
  localStorage.removeItem('appInBackground');
};

onIonViewWillEnter(() => {
  console.log('Page is entering');
});

onMounted(async () => {
  resetVariableOnColdStart(); // Vérifier si c'est un cold start

  const hasLaunched = await store.get("hasLaunched");
  const user = await store.get("user");
  userLogin.value = JSON.stringify(await user);
  console.log(hasLaunched)

  if (userLogin.value == '""' || userLogin.value == "null") {
    topCss.value = "8%";
    logoWidth.value = "250px";
  } else {
    topCss.value = "50px";
    logoWidth.value = "200px";
  }
  document.documentElement.style.setProperty("--topCss", topCss.value);
  document.documentElement.style.setProperty("--logoWidth", logoWidth.value);

  if (!hasLaunched) {
    await store.set("hasLaunched", false);
  } else {
    checkUserStatus(); // Sauter le splash screen si l'app a déjà été lancée
  }

  // Écoute des événements pause et resume
  App.addListener('pause', setAppInBackgroundFlag);
  App.addListener('resume', clearAppInBackgroundFlag);
});

onUnmounted(() => {
  // Retirer les écouteurs pour éviter les fuites de mémoire
  App.removeAllListeners();
});
</script>

<style scoped>
.splash-screen {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: white;
}

.logo {
  width: var(--logoWidth);
  animation: fadeInSlideUp 2s ease-in-out;
  position: absolute;
  top: 50vh;
}

@keyframes fadeInSlideUp {
  0% {
    opacity: 0;
    top: 50vh;
  }
  100% {
    opacity: 1;
    top: var(--topCss);
  }
}
</style>
