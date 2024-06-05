<script setup lang="ts">
import NavMenu from '@/components/NavMenu/NavMenu.vue'
import { ref } from 'vue'
import { get, patch } from '@/lib/callApi'
import { useRoute } from 'vue-router'
import { onMounted } from 'vue'
import NavButton from '@/components/NavButton/NavButton.vue'
import AlertComponents from '@/components/AlertComponents/AlertComponents.vue'

const router = useRoute()
const user: any = ref({})
const gender = ref([
  { id: 'male', value: 'Homme' },
  { id: 'female', value: 'Femme' },
  { id: 'other', value: 'Autre' }
])
const back = ref('back')

const show2 = ref(false)
const password_edit = ref('')

const userGender = ref('')
const alertErr = ref(false)
const error_message = ref('')
const error_title = ref('')
const id = ref(0)

const alertSuc = ref(false)
const success_message = ref('error')

const getUser = async () => {
  id.value = Number(router.params.user_id)
  const res = await get('/admin/users_all/' + id.value + '/')
  if (res.status === 404) {
    error_title.value = 'Error while retrieve Material id ' + id.value
    error_message.value = res.data.detail
    alertErr.value = true
  } else {
    user.value = await res
    gender.value.map((gender) => {
      if (user.value.gender === gender.id) {
        userGender.value = gender.value
      }
    })
  }
}

onMounted(() => {
  if (router.query.edit) {
    back.value = ''
  } else {
    back.value = 'back'
  }
  getUser()
})
</script>

<template lang="">
  <NavMenu />
  <div class="mainWrapper">
    <AlertComponents
      :message_alert="error_message"
      :type="'error'"
      :title="error_title"
      :alertValue="alertErr"
    />
    <v-alert
      :model-value="alertSuc"
      border="start"
      close-label="Close Alert"
      color="success"
      title="Modification effectuée"
      closable
      @click:close="closePopup"
    >
      {{ success_message }}
    </v-alert>
    <div class="headerBtns">
      <NavButton
        class="returnBtn"
        :text="'Retour'"
        :url="'/users'"
        :back="back"
        prepend-icon="mdi-arrow-left"
      />
      <div style="display: flex; flex-wrap: wrap; width: 300px; justify-content: flex-end">
        <NavButton
          class="editBtn"
          :text="'Modifier'"
          :url="'/users/edit/' + user.id"
          prepend-icon="mdi-pencil"
        />
        <v-dialog max-width="500">
          <template v-slot:activator="{ props: activatorProps }">
            <v-btn
              style="margin-top: 10px"
              v-bind="activatorProps"
              text="Modifier le mot de passe"
              variant="outlined"
            ></v-btn>
          </template>

          <template v-slot:default="{ isActive }">
            <v-card title="Modifier le mot de passe utilisateur">
              <v-card-text> </v-card-text>
              <div style="margin-left: 20px; margin-right: 20px">
                <v-text-field
                  label="Nouveau mot de passe"
                  @click:append-inner="show2 = !show2"
                  :append-inner-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="show2 === true ? 'text' : 'password'"
                  v-model="password_edit"
                ></v-text-field>
              </div>

              <v-card-actions>
                <v-spacer></v-spacer>

                <v-btn variant="tonal" text="Annuler" @click="isActive.value = false"></v-btn>
                <v-btn
                  variant="outlined"
                  text="Modifier"
                  @click="
                    () => {
                      patch(
                        '/users/' + id + '/set_password/',
                        {
                          body: {
                            password: password_edit
                          }
                        },
                        true
                      ).then((res) => {
                        console.log(res)
                        if (res.status > 301) {
                          error_title = 'Error while retrieve Material id ' + id.value
                          error_message = res.data.detail
                          alertErr = true
                        } else {
                          isActive.value = false
                          alertSuc = true
                          success_message = 'Mot de passe modifié'
                        }
                      })
                    }
                  "
                ></v-btn>
              </v-card-actions>
            </v-card>
          </template>
        </v-dialog>
      </div>
    </div>
    <h1>Carte de l'utilisateur : {{ user === undefined ? '' : user.email }}</h1>
    <h3 class="showTitle">Nom et prénom</h3>
    <p>
      {{ user.last_name + ' ' + user.first_name }}
    </p>
    <h3 class="showTitle">Email</h3>
    <p>
      {{ user.email }}
    </p>
    <h3 class="showTitle">Age</h3>
    <p>
      {{ user.age }}
    </p>
    <h3 class="showTitle">Taille</h3>
    <p>
      {{ user.size }}
    </p>
    <h3 class="showTitle">Poids</h3>
    <p>
      {{ user.weight }}
    </p>
    <h3 class="showTitle">Genre</h3>
    <p>
      {{ userGender }}
    </p>
    <h2 class="showTitle">Photo de profil</h2>
    <v-chip-group v-for="(element, index) in user.sports_user" :key="index">
      <v-chip>{{ element.sport.name }}</v-chip>
    </v-chip-group>
    <div class="imageDiv">
      <v-img :width="300" aspect-ratio="16/9" cover :src="user.profile_picture"></v-img>
    </div>
  </div>
</template>

<style>
.showTitle {
  text-align: left !important;
  margin-bottom: 0px !important;
  margin-top: 10px !important;
}

.headerBtns {
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
  padding-right: 10px;
}
</style>
