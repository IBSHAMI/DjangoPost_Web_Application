<template>
  <router-view></router-view>
</template>

<script>
import axios from "axios";
import useAuthenticationStore from "@/stores/authentication";

export default {
  name: "App",
  setup() {
    // init the store
    const authenticationStore = useAuthenticationStore();
    return { authenticationStore };
  },
  beforeCreate() {
    // init the authentication store using initializeStore function
    // from the authentication store
    this.authenticationStore.initializeStore();

    const token = this.authenticationStore.token;

    if (token) {
      axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
    } else {
      axios.defaults.headers.common["Authorization"] = null;
    }
  },
};
</script>

<style></style>
