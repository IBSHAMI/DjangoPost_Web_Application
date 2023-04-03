import { createRouter, createWebHistory } from "vue-router";
import { getAuthenticationStore } from "@/services/authService";

const HomeView = () => import("@/views/HomeView.vue");
const AuthView = () => import("@/views/AuthView.vue");
const JobsView = () => import("@/views/JobsView.vue");
const CompanyView = () => import("@/views/CompanyView.vue");
const EmployeeView = () => import("@/views/EmployeeView.vue");

const routes = [
  {
    path: "/", // the path to match
    name: "LandingPage", // the name of the route
    component: HomeView, // the component to render when the route is matched
  },
  {
    path: "/authentication/:slug",
    name: "Auth",
    props: true,
    component: AuthView,
  },
  {
    path: "/jobs/:slug",
    name: "Jobs",
    component: JobsView,
    meta: {},
  },
  {
    path: "/employee/:slug",
    name: "Employee",
    component: EmployeeView,
    props: true,
    meta: {
      requireAuthentication: true,
    },
  },
  {
    path: "/company/:slug",
    name: "Company",
    component: CompanyView,
    props: true,
    meta: {
      requireAuthentication: true,
    },
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const authenticationStore = getAuthenticationStore();

  // Check if the route requires authentication and if it is check if the user is authenticated
  if (to.meta.requireAuthentication && !authenticationStore.isAuthenticated) {
    console.log("You are not authenticated");
    // If the user is not authenticated redirect to the authentication page
    next({ name: "LandingPage" });
  } else {
    // If the user is authenticated or the route does not require authentication continue to the route
    next();
  }
});

export default router;
