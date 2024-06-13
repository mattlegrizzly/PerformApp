import { createRouter, createWebHistory } from "@ionic/vue-router";
import { RouteRecordRaw } from "vue-router";
import NavMenu from "./components/NavBar/NavBar.vue";
import { store } from "./store/store";
import { get, verifyToken, refresh } from "./lib/callApi";
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
        component: () => import("./views/HomePage.vue")
      },
      {
        path: "profile",
        name: "Profile",
        component: () => import("./views/Profile/ProfilePage.vue")
      },

      {
        path: "edit_profile",
        name: "EditProfile",
        component: () => import("./views/Profile/EditProfilePage.vue")
      },
      {
        path: "add_injurie",
        name: "AddInjurie",
        component: () => import("./views/Profile/AddInjuriePage.vue")
      },
      {
        path: "list_injuries",
        name: "ListInjuries",
        component: () => import("./views/Profile/ListInjuriesPage.vue")
      },
      {
        path: "view_injuries/:id",
        name: "ViewInjurie",
        component: () => import("./views/Profile/ViewInjuriePage.vue")
      },
      {
        path: "edit_injurie/:id",
        name: "EditInjurie",
        component: () => import("./views/Profile/EditInjuriePage.vue")
      },
      {
        path: "exercises",
        name: "Exercises",
        component: () => import("./views/Exercises/ListPage.vue")
      },
      {
        path: "exercises/:id",
        name: "ExercisesView",
        component: () => import("./views/Exercises/ViewPage.vue")
      },
      {
        path: "stats",
        name: "Statistics",
        component: () => import("./views/StatsPage.vue")
      },

      {
        path: "programs",
        name: "Programs",
        component: () => import("./views/ProgramsPage.vue")
      },
      {
        path: "conditions",
        component: () => import("./views/ConditionsPage.vue")
      },
    ],
  },
  {
    path: "/login",
    name: "login",
    component: () => import("./views/Login/LoginPage.vue"),
  },
];

const isLoggedIn = async () => {
  try {
    const res = await store.get("user");
    const access = JSON.parse(res).access;
    if (!access) return false;

    const verifyResponse = await verifyToken();

    if (verifyResponse.status > 300) {
      if (verifyResponse.status === 401) {
        const refreshResponse = refresh();
        //@ts-expect-error
        if (refreshResponse.status > 300) {
          store.remove("user");
          return false;
        }
      } else {
        store.remove("user");
        return false;
      }
    }
    const userResponse = await get("/admin/users_all/me/", { body: {} }, true);
    await store.set("user", JSON.stringify(userResponse));
    return true;
  } catch (error) {
    return false;
  }
};

const router = createRouter({
  // Use: createWebHistory(process.env.BASE_URL) in your app
  history: createWebHistory(),
  routes,
});

//@ts-expect-error
router.beforeEach(async (to, from, next) => {
  const isloggedin = (await isLoggedIn()) as any;
  if (to.name !== "login" && (await !isloggedin)) {
    next({
      path: "login",
      replace: true,
    });
  } else if (to.name == "login" && (await isloggedin)) {
    router.push("/");
  } else {
    if (to.params.animation) {
      to.meta.animation = to.params.animation;
    } else {
      to.meta.animation = 'default-animation'; // Animation par défaut
    }
    next();

  }
});

export default router;