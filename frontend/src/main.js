import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

import "./assets/base.css";

const app = createApp(App);

// we register the plugin on the app
// before creating the router
app.use(createPinia());

// we create the router after the plugin
app.use(router);

app.mount("#app");
