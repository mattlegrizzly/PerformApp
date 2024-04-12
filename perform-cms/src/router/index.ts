import { createRouter, createWebHistory } from '@ionic/vue-router'
import HomeView from '@/views/HomeView.vue'

import ListMaterials from '@/views/Materials/ListView.vue'
import AddMaterial from '@/views/Materials/AddView.vue'
import ShowMaterial from '@/views/Materials/ShowView.vue'

import UsersView from '@/views/UsersView.vue'

import ListExercises from '@/views/Exercises/ListView.vue'
import AddExercise from '@/views/Exercises/AddView.vue'

import ListSports from '@/views/Sports/ListView.vue'
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
  if (!access) return;

  try {
    console.log('yes');
    const tokenResponse = await verifyToken();

    if (tokenResponse.status > 300) {
      if (tokenResponse.status === 401) {
        const refreshResponse = await refresh();

        if (refreshResponse.status > 300) {
          removeUser();
          return;
        }
      }
      removeUser();
      return;
    }

    const userResponse = await get('/admin/users_all/me/', { body: {} }, true);
    setUser(userResponse);
    return;
  } catch (error) {
    return;
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
      path: '/users',
      name: 'users',
      component: UsersView
    },
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

router.beforeEach(async (to, from) => {
  const userStore = useUserStore()
  console.log(userStore.access)
  if (userStore.access == '' && cookies.get('access') !== ' ') {
    isLoggedIn().then(() =>{
      if (userStore.access !== '') {
        return { name: 'home' }
      } else {
        return { name: 'login' }
      }
    })
  }
  else if (userStore.access !== '' && to.name === 'login') {
    return { name: 'home' }
  }
  else if (userStore.access === '' && to.name !== 'login') {
    return { name: 'login' }
  }
})

export default router
