import { createRouter, createWebHistory } from "@ionic/vue-router";
import { RouteRecordRaw } from "vue-router";
import NavMenu from "./components/NavBar/NavBar.vue";

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
];

const router = createRouter({
  // Use: createWebHistory(process.env.BASE_URL) in your app
  history: createWebHistory(),
  routes,
});

export default router;
