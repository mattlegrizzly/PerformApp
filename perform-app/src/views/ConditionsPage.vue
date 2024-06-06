<template>
  <ion-page>
    <ion-content>
      <section>
        <NavButton text="Retour" url="profile" back="back" />
        <h1>Introduction</h1>
        <p>
          Bienvenue sur notre application. En utilisant notre service, vous
          acceptez les conditions générales suivantes.
        </p>
      </section>

      <section>
        <h1>Utilisation du Service</h1>
        <p>
          Vous vous engagez à utiliser notre service conformément à la loi et à
          respecter les droits des autres utilisateurs.
        </p>
      </section>

      <section>
        <h1>Propriété Intellectuelle</h1>
        <p>
          Tout le contenu présent sur notre application est protégé par des
          droits d'auteur et ne peut être utilisé sans autorisation préalable.
        </p>
      </section>

      <section>
        <h1>Responsabilité</h1>
        <p>
          Nous déclinons toute responsabilité en cas de dommages résultant de
          l'utilisation de notre service.
        </p>
      </section>

      <section>
        <h1>Modifications</h1>
        <p>
          Nous nous réservons le droit de modifier ces conditions à tout moment.
          Les modifications seront effectives dès leur publication sur notre
          application.
        </p>
      </section>

      <section>
        <h1>Contact</h1>
        <p>
          Si vous avez des questions concernant ces conditions générales,
          veuillez nous contacter à l'adresse suivante : contact@notreapp.com.
        </p>
      </section>
    </ion-content>
  </ion-page>
</template>

<script lang="ts" setup>
import NavButton from "../components/NavButton/NavButton.vue";
import {
  IonPage,
  IonContent,
} from "@ionic/vue";
</script>

<style scoped>
ion-card {
  margin: 16px;
}
</style>
