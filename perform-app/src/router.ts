import { createRouter, createWebHistory } from "@ionic/vue-router";
import { RouteRecordRaw } from "vue-router";
import NavMenu from "./components/NavBar/NavBar.vue";
import { store } from "./store/store";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    component: NavMenu,
    children: [
      {
        path: "",
        redirect: "/home",
      },
      {
        path: "home",
        name: "Home",
        component: () => import("./views/HomePage.vue"),
      },
      {
        path: "profile",
        name: "Profile",
        component: () => import("./views/Profile/ProfilePage.vue"),
      },
      {
        path: "exercises",
        name: "Exercises",
        component: () => import("./views/Exercises/ListPage.vue"),
      },
      {
        path: "exercises/:id",
        name: "ExercisesView",
        component: () => import("./views/Exercises/ViewPage.vue"),
      },
      {
        path: "search",
        component: () => import("./views/SearchPage.vue"),
      },
    ],
  },
  {
    path: '/login',
    name: 'login',
    component: () => import("./views/Login/LoginPage.vue")
  }
];

const router = createRouter({
  // Use: createWebHistory(process.env.BASE_URL) in your app
  history: createWebHistory(),
  routes,
});

const isLogin = async () => {
  const user = await store.get('user');
  if (await user !== '' || await user) {
    return true;
  } else {
    return false;
  }
}

router.beforeEach(async (to, from, next) => {
  const isloggedin = await isLogin();
  if (to.name !== 'login' && await !isloggedin) {
    console.log('return to login')
    next({
      path: 'login',
      replace: true
    })
  } else if (to.name == 'login' && await isloggedin) {
    console.log('already login')
    router.push('/')
  } else {
    next();
  }

})

export default router;
