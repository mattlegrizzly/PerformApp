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
        meta: {
          transition: "fade",
        },
      },
      {
        path: "profile",
        name: "Profile",
        component: () => import("./views/Profile/ProfilePage.vue"),
        meta: {
          transition: "fade",
        },
      },
      {
        path: "add_injurie",
        name: "AddInjurie",
        component: () => import("./views/Profile/AddInjuriePage.vue"),
        meta: {
          transition: "fade",
        },
      },
      {
        path: "list_injuries",
        name: "ListInjuries",
        component: () => import("./views/Profile/ListInjuriesPage.vue"),
        meta: {
          transition: "fade",
        },
      },
      {
        path: "exercises",
        name: "Exercises",
        component: () => import("./views/Exercises/ListPage.vue"),
        meta: {
          transition: "fade",
        },
      },
      {
        path: "exercises/:id",
        name: "ExercisesView",
        component: () => import("./views/Exercises/ViewPage.vue"),
        meta: {
          transition: "fade",
        },
      },
      {
        path: "search",
        component: () => import("./views/SearchPage.vue"),
        meta: {
          transition: "fade",
        },
      },
    ],
  },
  {
    path: "/login",
    name: "login",
    component: () => import("./views/Login/LoginPage.vue"),
  },
];

const router = createRouter({
  // Use: createWebHistory(process.env.BASE_URL) in your app
  history: createWebHistory(),
  routes,
});

const isLogin = async () => {
  const user = await store.get("user");
  if ((await user) !== "" && (await user)) {
    return true;
  } else {
    return false;
  }
};

router.beforeEach(async (to, from, next) => {
  console.log(from);
  const isloggedin = await isLogin();
  if (to.name !== "login" && (await !isloggedin)) {
    next({
      path: "login",
      replace: true,
    });
  } else if (to.name == "login" && (await isloggedin)) {
    router.push("/");
  } else {
    next();
  }
});

export default router;
