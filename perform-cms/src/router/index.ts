import { createRouter, createWebHistory } from '@ionic/vue-router'
import HomeView from '@/views/HomeView.vue'

import ListMaterials from '@/views/Materials/ListView.vue'
import AddMaterial from '@/views/Materials/AddView.vue'
import ShowMaterial from '@/views/Materials/ShowView.vue'
import EditMaterial from '@/views/Materials/EditView.vue'

import ListUsers from '@/views/Users/ListView.vue'
import ShowUsers from '@/views/Users/ShowView.vue'

import ListExercises from '@/views/Exercises/ListView.vue'
import AddExercise from '@/views/Exercises/AddView.vue'
import ShowExercise from '@/views/Exercises/ShowView.vue'
import EditExercise from '@/views/Exercises/EditView.vue'

import ListSports from '@/views/Sports/ListView.vue'
import ShowSport from '@/views/Sports/ShowView.vue'
import EditSport from '@/views/Sports/EditView.vue'
import AddSport from '@/views/Sports/AddView.vue'

import PageNotFoundView from '@/views/PageNotFoundView.vue'
import LoginView from '@/views/LoginView.vue'

import { refresh } from '@/lib/callApi'
import { useUserStore } from '@/stores/store'
import { useCookies } from '@vueuse/integrations/useCookies'
import { verifyToken } from '@/lib/callApi'
import { get } from '@/lib/callApi'

const cookies = useCookies(['locale'])

const setUser = (res : any) => {
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
  const access = cookies.get('access');
  if (!access) return false;

  try {
    const tokenResponse = await verifyToken();
    console.log('token response ', tokenResponse)    
    if (tokenResponse.status > 300) {
      if (tokenResponse.status === 401) {
        const refreshResponse = await refresh();
      console.log('refresh response ', refreshResponse)    

        if (refreshResponse.status > 300) {
          return false;
        }
      }
      removeUser();
      return false;
    }

    const userResponse = await get('/admin/users_all/me/', { body: {} }, true);
    setUser(await userResponse);
    return true;
  } catch (error) {
    removeUser();
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
      path: '/sports/add',
      name: 'addSport',
      component: AddSport
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

  // Exécutez votre fonction isLoggedIn pour vérifier si l'utilisateur est connecté
  

  // Maintenant, vous pouvez mettre en place votre logique de redirection en fonction de l'état de connexion de l'utilisateur
  const isAuthenticated = await isLoggedIn();
  console.log(await isAuthenticated)

  if (to.name === 'login' && await isAuthenticated) {
    // Si l'utilisateur est déjà connecté et qu'il essaie d'accéder à la page de connexion, redirigez-le vers la page d'accueil
    next({ name: 'home' });
  } else if (to.name !== "login" && await !isAuthenticated) {
    // Si la route nécessite une authentification et que l'utilisateur n'est pas authentifié, redirigez-le vers la page de connexion
    next({ name: 'login' });
  } else {
    // Si l'utilisateur est authentifié ou si la route n'exige pas d'authentification, laissez-le continuer
    next();
  }
});

export default router
