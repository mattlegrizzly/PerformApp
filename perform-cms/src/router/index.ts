import { createRouter, createWebHistory } from '@ionic/vue-router'
import HomeView from '@/views/HomeView.vue'
import MaterialsView from '@/views/MaterialsView.vue'
import UsersView from '@/views/UsersView.vue'
import ExercicesView from '@/views/ExercicesView.vue'
import PageNotFoundView from '@/views/PageNotFoundView.vue'
import LoginView from '@/views/LoginView.vue'
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
      component: ExercicesView
    },
    {
      path: '/users',
      name: 'users',
      component: UsersView
    },
    {
      path: '/materials',
      name: 'materials',
      component: MaterialsView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/*',
      name: 'not found',
      component: PageNotFoundView
    }
  ]
})

router.beforeEach(async (to, from) => {
  if (localStorage.getItem('user') === null && to.name !== 'login') {
    // redirect the user to the login page
    return { name: 'login' }
  } else if (localStorage.getItem('user') !== null && to.name === 'login') {
    return { name: 'home' }
  }
})

export default router
