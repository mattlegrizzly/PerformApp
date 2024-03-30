import { createRouter, createWebHistory } from '@ionic/vue-router';
import HomeView from '@/views/HomeView.vue'
import SecondPage from '@/views/SecondView.vue';
import NewView from '@/views/NewView.vue';
import PageNotFoundView from '@/views/PageNotFoundView.vue';
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/exercices',
      name: 'exercices',
      component: SecondPage
    },
    {
      path: '/users',
      name: 'users',
      component: SecondPage
    }, 
    {
      path: '/new',
      name: 'new',
      component: NewView
    }, 
    {
      path: '/*',
      name: 'not found',
      component: PageNotFoundView
    },
  ]
})

export default router
