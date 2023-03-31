<template>
  <router-view></router-view>
</template>

<script>
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
  },
  mounted() {
    // load profile pictures
    this.authenticationStore.getAccountPictures();
    // check if the profiles information are complete for profile and company
    this.authenticationStore.checkIfProfileComplete();
  },
};
</script>

<style></style>
