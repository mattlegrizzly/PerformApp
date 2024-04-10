import { createRouter, createWebHistory } from '@ionic/vue-router'
import HomeView from '@/views/HomeView.vue'

import ListMaterials from '@/views/Materials/ListView.vue'
import AddMaterial from '@/views/Materials/AddView.vue';
import ShowMaterial from '@/views/Materials/ShowView.vue'

import UsersView from '@/views/UsersView.vue'

import ListExercises from '@/views/Exercises/ListView.vue';
import AddExercise from '@/views/Exercises/AddView.vue';

import ListSports from '@/views/Sports/ListView.vue';
import AddSport from '@/views/Sports/AddView.vue';

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
      component: ListExercises,
    },
    {
      path: '/exercises/add',
      name:'addExercise',
      component : AddExercise
    },
    {
      path: '/sports',
      name: 'sport',
      component: ListSports,
    },
    {
      path: '/sports/add',
      name:'addSport',
      component : AddSport
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
      name:'addMaterials',
      component : AddMaterial
    },
    {
      path: '/materials/show/:material_id',
      name:'showMaterial',
      component : ShowMaterial
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
  if (localStorage.getItem('user') === null && to.name !== 'login') {
    // redirect the user to the login page
    return { name: 'login' }
  } else if (localStorage.getItem('user') !== null && to.name === 'login') {
    return { name: 'home' }
  }
})

export default router
