<style scoped>
.example-content {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
</style>

<template>
  <ion-page data-page="profile">
    <ion-content>
      <div class="container_home">
        <div class="profile_picture_div">
          <div class="img_container">
            <div
              style="
                display: flex;
                justify-content: center;
                align-items: center;
                font-size: 2rem;
                font-weight: bold;
                color: var(--primary-blue);
                background-color: white;
                border-radius: 50%;
                width: 100%;
                height: 100%;
                text-transform: capitalize;
              "
              v-if="profilePicture == ''"
            >
              {{ user.first_name[0] }}
            </div>

            <img v-else :src="profilePicture" alt="profile" />
          </div>
        </div>
        <div class="profile_container_div">
          <h1>
            {{ user.first_name + " " + user.last_name }}
          </h1>
        </div>
        <div class="profile_container_div">
          <div class="div_container_info">
            <h2>Mes infos</h2>
            <div class="users_infos">
              <div class="div_user_info">
                <h3>Âge :</h3>
                <p>{{ user.age }}</p>
              </div>

              <div class="div_user_info">
                <h3>Poids :</h3>
                <p>{{ user.weight }} kg</p>
              </div>

              <div class="div_user_info">
                <h3>Taille :</h3>
                <p>{{ user.size }} cm</p>
              </div>
            </div>
          </div>
        </div>
        <div class="profile_container_div">
          <div class="div_container_info">
            <h2 >Mes disciplines</h2>
            <ion-chip style="margin-right: 5px; margin-bottom: 5px;" class="ion-chip-user" v-for="sport of user.sports_user" color="primary">{{
              sport.sport.name
            }}</ion-chip>
          </div>
        </div>
        <div class="profile_container_div">
          <div @click="() => router.push('records')" class="div_container_info" style="display: flex; align-items: center; justify-content: space-between;">
            <h2 style="margin-bottom: 0px  !important;">Mes records</h2>
            <ion-icon :icon="chevronForwardOutline"></ion-icon>
          </div>
        </div>
        
        <div class="profile_container_div">
          <div
            class="div_container_info"
            style="display: flex; justify-content: center; flex-wrap: wrap"
          >
            <h2 style="text-align: left; width: 100%">Mes blessures</h2>
            <NavButton
              v-if="user.user_injuries.length == 0"
              url="add_injurie"
              text="Ajouter une blessure"
              :noIcon="true"
            />
            <ion-list class="injurie_list" style="width: 100%">
              <div
                class="injurie_div"
                @click="router.push('/view_injuries/' + injurie.id)"
                v-for="injurie of limitedItems()"
              >
                <ion-label
                  style="
                    width: 20%;
                    text-wrap: nowrap;
                    text-overflow: ellipsis;
                    overflow: hidden;
                  "
                  >{{ injurie.zone.name }}</ion-label
                >
                <ion-label>|</ion-label>
                <ion-label>
                  {{
                    new Date(injurie.date).toLocaleString("fr").split(" ")[0]
                  }}</ion-label
                >
                <ion-label>|</ion-label>
                <ion-label
                  :class="stateSetClass(injurie.state)"
                  class="injurie_state"
                  >{{ stateSet(injurie.state) }}
                </ion-label>
                <ion-icon :icon="chevronForwardOutline"></ion-icon>
              </div>
              <ion-label
                style="width: 100%; text-align: center; display: block"
                v-if="user.user_injuries.length > 2"
                >...</ion-label
              >
            </ion-list>
            <NavButton
              class="custom_nav"
              v-if="user.user_injuries.length > 0"
              url="list_injuries"
              text="Voir toutes mes blessures"
              :noIcon="true"
            />
          </div>
          <v-divider :thickness="3"></v-divider>
          <div class="buttons_user">
            <NavButton
              class="custom_nav"
              url="edit_profile"
              text="Editer mon profil"
              :icon="pencil"
            />
            <NavButton
              class="custom_nav"
              url="edit_password"
              text="Editer mon mot de passe"
              :icon="lockClosedOutline"
            />
            <NavButton
              class="custom_nav"
              href="mailto:contact@performapp.com"
              text="Nous contacter"
              :icon="mail"
            />
            <NavButton
              class="custom_nav"
              url="conditions"
              text="Nos conditions générales d'utilisations"
              :icon="documentText"
            />
            <NavButton
              class="custom_nav"
              @click="disconnect"
              text="Déconnexion"
              :icon="logOut"
              :color="'light'"
            />
          </div>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script lang="ts" setup>
import {
  IonContent,
  IonPage,
  IonChip,
  IonList,
  IonIcon,
  IonLabel,
  onIonViewWillEnter,
} from "@ionic/vue";
import { store } from "../../store/store";
import router from "../../router";
import { ref, computed } from "vue";
import "./index.css";
import NavButton from "../../components/NavButton/NavButton.vue";
import { stateSet, stateSetClass } from "../../lib/injurie";
import {
  chevronForwardOutline,
  pencil,
  mail,
  documentText,
  logOut,
  lockClosedOutline
} from "ionicons/icons";


const api = import.meta.env.VITE_API_URL;
const user = ref({
  age: 0,
  weight: 0,
  size: 0,
  email: "",
  first_name: "",
  gender: "",
  id: 1,
  last_name: "",
  profile_picture: "",
  sports_user: [] as any,
  user_injuries: [],
  users_wellness: [],
});
/**
 * Retourne les deux premières blessures de l'utilisateur.
 * @returns {any} - Les deux premières blessures de l'utilisateur.
 */
function limitedItems(): any {
  const injuries = user.value.user_injuries.sort(function(a : any, b : any){
    const start = new Date(a.date) as Date
    const end = new Date(b.date) as Date
    //@ts-expect-error
    return end - start;
});

  return injuries.slice(0, 2);
}

/**
 * Calcule l'URL de l'image de profil de l'utilisateur.
 * @returns {string} - L'URL de l'image de profil, modifiée pour utiliser HTTPS si nécessaire.
 */
const profilePicture = computed((): string => {
  if (
    user.value.profile_picture &&
    user.value.profile_picture.includes(api.split("//")[1])
  ) {
    return user.value.profile_picture.replace("http", "https");
  } else {
    if (
      user.value.profile_picture === null ||
      user.value.profile_picture === ""
    ) {
      return "";
    } else {
      return api + user.value.profile_picture;
    }
  }
});

/**
 * Déconnecte l'utilisateur et le redirige vers la page de connexion.
 */
const disconnect = (): void => {
  store.set("user", "").then(() => {
    router.push("login");
  });
};

/**
 * Exécute les actions nécessaires lors de l'entrée dans la vue.
 */
onIonViewWillEnter(async () => {
  let storeUser = await store.get("user");
  if (storeUser !== "") {
    user.value = JSON.parse(storeUser).user;
  }

  const ionSelect = document.querySelectorAll(".custom_nav");
  if (ionSelect === null) return;
  for (const elem of ionSelect) {
    const shadowRoot = elem.shadowRoot;
    if (shadowRoot === null) return;
    const style = document.createElement("style");
    style.textContent = `
        .button-inner {
        justify-content: flex-start !important;
        }
    `;
    shadowRoot.appendChild(style);
  }
});
</script>
