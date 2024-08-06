import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

import ListMaterials from '@/views/Materials/ListView.vue'
import AddMaterial from '@/views/Materials/AddView.vue'
import ShowMaterial from '@/views/Materials/ShowView.vue'
import EditMaterial from '@/views/Materials/EditView.vue'

import ListUsers from '@/views/Users/ListView.vue'
import ShowUsers from '@/views/Users/ShowView.vue'
import AddUser from '@/views/Users/AddView.vue'
import EditUser from '@/views/Users/EditView.vue'

import ListExercises from '@/views/Exercises/ListView.vue'
import AddExercise from '@/views/Exercises/AddView.vue'
import ShowExercise from '@/views/Exercises/ShowView.vue'
import EditExercise from '@/views/Exercises/EditView.vue'

import ListSports from '@/views/Sports/ListView.vue'
import ListRecordsSportsView from '@/views/Sports/ListRecordsSportsView.vue'
import ListRecordsThemeView from '@/views/Sports/ListRecordsThemeView.vue'
import ShowTheme from '@/views/Sports/ShowTheme.vue'
import ShowSport from '@/views/Sports/ShowView.vue'
import EditSport from '@/views/Sports/EditView.vue'
import AddSport from '@/views/Sports/AddView.vue'
import AddTheme from '@/views/Sports/AddTheme.vue'
import AddRecord from '@/views/Sports/AddViewRecord.vue'
import AddThemeRecord from '@/views/Sports/AddThemeRecord.vue'

import PageNotFoundView from '@/views/PageNotFoundView.vue'
import LoginView from '@/views/LoginView.vue'

import { refresh } from '@/lib/callApi'
import { useUserStore } from '@/stores/store'
import { useCookies } from '@vueuse/integrations/useCookies'
import { verifyToken } from '@/lib/callApi'
import { get } from '@/lib/callApi'

const cookies = useCookies(['locale'])

const setUser = (res: any) => {
  const userStore = useUserStore()
  userStore.setUser(res)
  const date = new Date()
  date.setDate(date.getDate() + 7)
  cookies.set('access', res.access, { expires: date })
}

const removeUser = () => {
  const userStore = useUserStore()
  cookies.remove('access')
  userStore.removeUser()
}


const isLoggedIn = async () => {
  try {
    const userStore = useUserStore();
    const access = cookies.get('access');

    if (!access) return false;

    const verifyResponse = await verifyToken();
    if (verifyResponse.status > 300) {
      if (verifyResponse.status === 401) {
        const refreshResponse = await refresh();
        if (refreshResponse.status > 300) {
          removeUser();
          return false;
        } else {
          const newUser = {
            user: userStore.userData, // Assurez-vous que cela contient les données actuelles
            refresh: refreshResponse.refresh,
            access: refreshResponse.access,
          };
          userStore.setUser(newUser);
          return true;
        }
      } else {
        removeUser();
        return false;
      }
    } else {
      const userResponse = await get("/users/me/", { body: {} }, true);
      userStore.setUser(userResponse);
      return true;
    }
  } catch (error) {
    console.error('Erreur lors de la vérification de la connexion:', error);
    return false;
  }
};



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/exercises',
      name: 'exercises',
      component: ListExercises
    },
    {
      path: '/exercises/add',
      name: 'addExercise',
      component: AddExercise
    },

    {
      path: '/exercises/show/:exercise_id',
      name: 'showExercise',
      component: ShowExercise
    },

    {
      path: '/exercises/edit/:exercise_id',
      name: 'editExercise',
      component: EditExercise
    },
    {
      path: '/sports',
      name: 'sport',
      component: ListSports
    },
    {
      path: '/records_sports',
      name: 'records_sports',
      component: ListRecordsSportsView
    },
    {
      path: '/records_theme',
      name: 'records_theme',
      component: ListRecordsThemeView
    },
    {
      path: '/records_theme/add',
      name: 'addTheme',
      component: AddTheme
    },
    {
      path: '/records_theme/show/:sport_id',
      name: 'showTheme',
      component: ShowTheme
    },
    {
      path: '/records_theme/add_record/:sport_id',
      name: 'addThemeRecord',
      component: AddThemeRecord
    },
    {
      path: '/sports/add',
      name: 'addSport',
      component: AddSport
    },
    
    {
      path: '/sports/add_record/:sport_id',
      name: 'addRecord',
      component: AddRecord
    },
    {
      path: '/sports/show/:sport_id',
      name: 'showSport',
      component: ShowSport
    },
    {
      path: '/sports/edit/:sport_id',
      name: 'editSport',
      component: EditSport
    },
    //Users
    {
      path: '/users',
      name: 'users',
      component: ListUsers
    },
    {
      path: '/users/show/:user_id',
      name: 'showUsers',
      component: ShowUsers
    },
    {
      path: '/users/add',
      name: 'addUser',
      component: AddUser
    },
    {
      path: '/users/edit/:user_id',
      name: 'editUser',
      component: EditUser
    },
    //Materials
    {
      path: '/materials',
      name: 'materials',
      component: ListMaterials
    },
    {
      path: '/materials/add',
      name: 'addMaterials',
      component: AddMaterial
    },
    {
      path: '/materials/show/:material_id',
      name: 'showMaterial',
      component: ShowMaterial
    },
    {
      path: '/materials/edit/:material_id',
      name: 'editMaterial',
      component: EditMaterial
    },
    //Login
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not found',
      component: PageNotFoundView
    }
  ]
})

router.beforeEach(async (to, from, next) => {
  // Cette fonction sera appelée avant chaque navigation de route
  // Maintenant, vous pouvez mettre en place votre logique de redirection en fonction de l'état de connexion de l'utilisateur
  const isAuthenticated = await isLoggedIn()
  if (to.name === 'login' && (await isAuthenticated)) {
    // Si l'utilisateur est déjà connecté et qu'il essaie d'accéder à la page de connexion, redirigez-le vers la page d'accueil
    next({ name: 'home' })
  } else if (to.name !== 'login' && (await !isAuthenticated)) {
    // Si la route nécessite une authentification et que l'utilisateur n'est pas authentifié, redirigez-le vers la page de connexion
    next({ name: 'login' })
  } else {
    // Si l'utilisateur est authentifié ou si la route n'exige pas d'authentification, laissez-le continuer
    next()
  }
})

export default router
