<style scoped>
.input-div ion-list {
  width: auto;
  height: 40px;
  display: flex;
  min-height: 40px !important;
  align-items: center;
}

.input-div ion-input {
  padding-left: 20px !important;
  border-radius: 30px;
  border: 1px solid #d4d4d4;
  min-height: 40px !important;
  width: calc(100% - 20px);
  --padding-start: 0px !important;
  --padding-end: 0px !important;
  --border: none;
  --border-color: none;
  --border-width: none;
}

.input-div ion-item {
  border-radius: 30px;
  border: 1px solid #d4d4d4;
  min-height: 40px !important;
  height: 40px;

  width: 100%;
}

.edit_profile_div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-left: 40px;
  padding-right: 40px !important;
  width: auto;
}

.profile_image {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 200px;
  height: 200px;
}


.img_div {
  overflow: hidden;
  border-radius: 200px;

}

.div_pp {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.div_pp ion-label {
  width: 100%;

}

ion-chip {
  padding-left: 10px;
  padding-right: 10px;
  color: white;
  background-color: var(--primary-blue);
}
</style>

<template>
  <ion-page>
    <ion-content>
      <div class="perform-page">
        <div style="display: flex; justify-content: space-between">
          <NavButton url="profile" text="Retour" back="back" />
        </div>
        <h1 style="color: black; margin-top: 5px; margin-bottom: 10px">
          Modifier mes informations
        </h1>
        <div class="edit_profile_div">
          <div class="div_pp">
            <ion-label>Photo de profil : </ion-label>
            <div class="profile_image">
              <div class="img_div">
                <ion-img :src="fileToDisplay" @click="triggerFileInput"></ion-img>
              </div>
              <input type="file" accept="image/*" ref="fileInput" @change="handleFileChange"
                style="display: none"></input>
            </div>

          </div>
          <div class="input-div">
            <ion-label>Nom : </ion-label>
            <ion-input type="text" class="login-input" fill="outline" slot="end" placeholder="Prénom" shape="round"
              @ionInput="handleInput('first_name', $event.detail.value)" :value="user.first_name"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Prénom : </ion-label>
            <ion-input type="text" class="login-input" fill="outline" slot="end" placeholder="Nom" shape="round"
              @ionInput="handleInput('last_name', $event.detail.value)" :value="user.last_name">
            </ion-input>
          </div>
          <div class="input-div">
            <ion-label>Email : </ion-label>
            <ion-input type="email" class="login-input" fill="outline" slot="end" placeholder="email@perform.com"
              shape="round" @ionInput="handleInput('email', $event.detail.value)" :value="user.email"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Âge : </ion-label>
            <ion-input type="number" class="login-input" fill="outline" slot="end" placeholder="20" shape="round"
              @ionInput="handleInput('age', $event.detail.value)" :value="user.age"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Taille : </ion-label>
            <ion-input type="number" class="login-input" fill="outline" slot="end" placeholder="170" shape="round"
              @ionInput="handleInput('size', $event.detail.value)" :value="user.size"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Poids : </ion-label>
            <ion-input type="number" class="login-input" fill="outline" slot="end" placeholder="80" shape="round"
              @ionInput="handleInput('weight', $event.detail.value)" :value="user.weight"></ion-input>
          </div>
          <div class="input-div">
            <ion-label>Sélectionne tes sports : </ion-label>
            <ion-list>
              <ion-item>
                <ion-select @ionChange="updateSelectedSports" class="custom-ion-select" :value="sports_user_temp"
                  aria-label="Fruit" placeholder="Selectionner vos sports" :multiple="true" :compareWith="compareWith">
                  <ion-select-option v-for="(sport, index) in sports" :value="{ id: sport.id, name: sport.name }"
                    :key="sport.id" aria-selected="true">{{ sport.name }}</ion-select-option>
                </ion-select>
              </ion-item>
            </ion-list>
            <div style="margin-top: 10px">
              <ion-chip :icon="close" v-for="sport of sports_user_temp" color="primary">
                <ion-icon :id="sport.id" :icon="close" @click="removeSport"></ion-icon>
                <ion-label>{{ sport.name }}</ion-label>
              </ion-chip>
            </div>
          </div>
          <NavButton text="Enregistrer" @click="editProfile" />
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonContent,
  IonPage,
  IonInput,
  IonLabel,
  IonList,
  IonItem,
  IonSelect,
  IonSelectOption,
  IonImg,
  IonIcon,
  IonChip
} from "@ionic/vue";
import { ref, onMounted, onUpdated } from "vue";
import { close } from "ionicons/icons";
import "@/assets/base.css";
import "@/assets/main.css";
import { store } from "../../store/store";
import router from "../../router";
import { Sport } from "../../types/allType";
import { useRoute } from "vue-router";
import NavButton from "../../components/NavButton/NavButton.vue";
import { get, patch, del, post } from "../../lib/callApi";
import "./index.css";
import ProfilePage from "./ProfilePage.vue";
const routes = useRoute();

const fileInput = ref(null);

const handleInput = (key: string, value: string) => {
  user.value[key] = value;
};

const compareWith = (o1, o2) => {
  return o1 && o2 ? o1.id === o2.id : o1 === o2;
};

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
  sports_user: [] as Sport[],
});


const fileToDisplay = ref('');
const fileToSend = ref(null);


function findById(array, id) {
  console.log(array)
  return array.find(item => item.id === id);
}


const editProfile = () => {
  const userEdit = {
    age: user.value.age,
    weight: user.value.weight,
    size: user.value.size,
    email: user.value.email,
    last_name: user.value.last_name,
    first_name: user.value.first_name,

  };
  if (fileToSend.value) {
    userEdit['profile_picture'] = fileToSend.value;
  }
  const inPlus = [];
  const inMinus = [];
  const equivalent = [];
  // Vérifier les éléments en plus dans newArray
  for (const newItem of sports_user_temp.value) {
    const matchInBase = findById(user.value.sports_user, newItem.id);
    if (!matchInBase) {
      inPlus.push(newItem);
    } else {
      equivalent.push(newItem);
    }
  }

  // Vérifier les éléments en moins dans baseArray
  for (const baseItem of user.value.sports_user) {
    const matchInNew = findById(sports_user_temp.value, baseItem.sport.id);
    if (!matchInNew) {
      inMinus.push(baseItem);
    }
  }

  for (const sport of inPlus) {
    post("/admin/sports_user/", { body: { user: user.value.id, sport: sport.id } }, true, true).then((res) => {
      if (res.status > 300) {
      } else {
      }
    });
  }
  for (const sport of inMinus) {
    del("/admin/sports_user/" + sport.id + "/").then((res) => {
      if (res.status > 300) {
      } else {

      }
    });

  }
  patch("/users/" + user.value.id + "/", { body: userEdit }, true, true).then((res) => {
    if (res.status > 300) {
    } else {
      router.push('/profile');
    }
  });
};

const api = import.meta.env.VITE_API_URL;

const triggerFileInput = () => {
  fileInput.value.click();
};
const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      fileToDisplay.value = e.target.result as string;
      fileToSend.value = file;
    };
    reader.readAsDataURL(file);
  }
};

const removeSport = (event) => {
  sports_user_temp.value = sports_user_temp.value.filter(
    (sport) => sport.id !== Number(event.target.id)
  );

};

const updateSelectedSports = (change) => {
  sports_user_temp.value = change.detail.value;
};

const sports_user_temp = ref([] as Sport[]);
const sports = ref([] as Sport[]);

onMounted(async () => {
  let storeUser = await store.get("user");
  if (storeUser !== "") {
    user.value = JSON.parse(storeUser).user;
    user.value.sports_user.map((sport) => {
      sports_user_temp.value.push(sport.sport);
    });
  }
  get("/sports", { body: {} }, false).then((res) => {
    if (res.status > 300) {
    } else {
      sports.value = res.results;
    }
  });
  const ionSelect = document.querySelectorAll(".custom-ion-select");
  if (ionSelect === null) return;
  for (const elem of ionSelect) {
    const shadowRoot = elem.shadowRoot;
    if (shadowRoot === null) return;
    const style = document.createElement("style");
    style.textContent = `
        .select-wrapper-inner {
        width: 100%; /* Ajustez cette valeur selon vos besoins */
        justify-content: space-between;
      }
    `;
    shadowRoot.appendChild(style);
  }
});

const load = () => {
  store.get("user").then((res) => {
    const json = JSON.parse(res);
    user.value = json.user;
    fileToDisplay.value = api + user.value.profile_picture;
  });
  get("/sports", { body: {} }, false).then((res) => {
    if (res.status > 300) {
    } else {
      sports.value = res.results;
    }
  });
};

onUpdated(() => {
  if (routes.name == "EditProfile") {
    load();
  }
});
</script>
