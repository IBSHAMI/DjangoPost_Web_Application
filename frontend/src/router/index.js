import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

// Vue excpect this to be an array of objects with a path and a component
// each object is called a route record
const routes = [
  {
    path: "/", // the path to match
    name: "LandingPage", // the name of the route
    component: HomeView, // the component to render when the route is matched
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
