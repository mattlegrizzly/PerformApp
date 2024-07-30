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
import { onMounted, ref } from "vue";
import { IonContent, onIonViewWillEnter, IonPage } from "@ionic/vue";
import { store } from "../../store/store";
import router from "../../router"

const userLogin = ref("");

const logo = <any|HTMLElement>ref(null);

const topCss = ref("");
const logoWidth = ref("");

const checkUserStatus = async () => {
  //const isLoggedIn = store.state.isLoggedIn; // Exemple de vérification de l'état de connexion
  await store.set("hasLaunched", true);

  if (userLogin.value !== "") {
    router.push("/home");
  } else {
    router.push("/login");
  }
};

const handleAnimationEnd = () => {
  logo.value.style.top = topCss.value;
  console.log(logo.value.style)
  checkUserStatus();
};

onIonViewWillEnter(() => {
  console.log('oui ')
})

onMounted(async () => {
  const hasLaunched = await store.get("hasLaunched");
  const user = await store.get("user");
  userLogin.value = JSON.stringify(await user);
  console.log(hasLaunched)
  if (userLogin.value == '""' || userLogin.value == "null") {
    topCss.value = "8%";
    logoWidth.value = "250px";
    console.log(topCss.value);
  } else {
    topCss.value = "50px";
    logoWidth.value = "200px";
    console.log(topCss.value);
  }
  // Mettre à jour la variable CSS
  document.documentElement.style.setProperty("--topCss", topCss.value);
  document.documentElement.style.setProperty("--logoWidth", logoWidth.value);
  if (!hasLaunched) {
    await store.set("hasLaunched", false);
    // Afficher le splash screen seulement lors du premier lancement
  } else {
    checkUserStatus(); // Sauter le splash screen si l'app a déjà été lancée
  }
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
