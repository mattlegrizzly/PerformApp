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
        name: "Splash",
        component: () => import("./views/SplashScreen/SplashScreen.vue"),
      },
      {
        path: "home",
        name: "Home",
        component: () => import("./views/Home/HomePage.vue")
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
        path: "edit_password",
        name: "EditPassword",
        component: () => import("./views/Profile/EditPasswordPage.vue")
      },
      {
        path: "add_injurie",
        name: "AddInjurie",
        component: () => import("./views/Injuries/AddInjuriePage.vue")
      },
      {
        path: "list_injuries",
        name: "ListInjuries",
        component: () => import("./views/Injuries/ListInjuriesPage.vue")
      },
      {
        path: "view_injuries/:id",
        name: "ViewInjurie",
        component: () => import("./views/Injuries/ViewInjuriePage.vue")
      },
      {
        path: "edit_injurie/:id",
        name: "EditInjurie",
        component: () => import("./views/Injuries/EditInjuriePage.vue")
      },
      {
        path: "records",
        name: "Records",
        component: () => import("./views/Records/ListRecords.vue")
      },

      {
        path: "show_records/:record_id",
        name: "ShowRecords",
        component: () => import("./views/Records/ShowRecords.vue")
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
        path: "coaching",
        name: "Coaching",
        component: () => import("./views/Coaching/CoachingPage.vue")
      },

      {
        path: "programs",
        name: "Programs",
        component: () => import("./views/Programs/ProgramsPage.vue")
      },
      {
        path: "conditions",
        component: () => import("./views/Documentation/ConditionsPage.vue")
      },
      {
        path: "login",
        name: "Login",
        component: () => import("./views/Login/LoginPage.vue"),
      }
    ],
  },
];

const isLoggedIn = async () => {
  try {
    const res = await store.get("user");
    const user = JSON.parse(res).user;
    const access = JSON.parse(res).access;
    if (!access) return false;

    const verifyResponse = await verifyToken();
    if (verifyResponse.status > 300) {
      console.log(verifyResponse.status === 401)
      if (verifyResponse.status === 401) {
        const refreshResponse = await refresh();
        console.log('??')
        console.log(refreshResponse)
        if (refreshResponse.status > 300) {
          
          await store.remove("user");
          return false;
        } else {
          const newUser = {
            user: user,
            refresh: refreshResponse.refresh,
            access: refreshResponse.access,
          };
          store.set('user', JSON.stringify(newUser)).then(() => {return true});
        }
      } else {
        await store.remove("user");
        return false;
      }
    } else {
      const userResponse = await get("/users/me/", { body: {} }, true);
      store.set("user", JSON.stringify(userResponse)).then(() => {return true});
    }
  } catch (error) {
    return false;
  }
  return true;

};


const router = createRouter({
  // Use: createWebHistory(process.env.BASE_URL) in your app
  history: createWebHistory(),
  routes,
});

//@ts-expect-error
router.beforeEach(async (to, from, next) => {
  const isloggedin = (await isLoggedIn()) as any;
  if (to.name !== "Login" && to.name !== "Splash" && (await !isloggedin)) {
    next({
      path: "login",
      replace: true,
    });
  } else if (to.name == "Login" && (await isloggedin)) {
    next({
      path: "home",
      replace: true,
    });
  } else {
    console.log('ici ')
    next();

  }
});

export default router;