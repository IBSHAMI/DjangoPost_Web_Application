import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import veeValidatePlugin from "@/includes/validation";
import axios from "axios";

import "./assets/base.css";

const app = createApp(App);

// we register the plugin on the app
// before creating the router
app.use(createPinia());

// we create the router after the plugin
app.use(router);

// we pass our custom plugins
app.use(veeValidatePlugin);

// we use axios to make http requests to the django backend
app.use(axios);

app.mount("#app");
