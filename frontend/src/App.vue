<template>
  <router-view></router-view>
</template>

<script>
import { getAuthenticationStore } from "@/services/authService";

export default {
  name: "App",
  data() {
    return {
      authenticationStore: null,
    };
  },
  created() {
    this.authenticationStore = getAuthenticationStore();
    this.authenticationStore.initializeStore();
  },
  mounted() {
    if (this.authenticationStore.isAuthenticated) {
      // load profile pictures
      this.authenticationStore.getAccountPictures();
      // check if the profiles information are complete for profile and company
      this.authenticationStore.checkIfProfileComplete();
    }
  },
};
</script>

<style></style>
