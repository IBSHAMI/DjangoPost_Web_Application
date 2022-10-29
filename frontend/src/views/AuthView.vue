<template>
  <div>
    <main class="container bg-[#6b7280]">
      <div v-if="!signup">
        <login-item @signupPageShow="signupPageShow" />
      </div>
      <div v-else-if="signup">
        <signup-item @signupPageShow="signupPageShow" />
      </div>
    </main>
  </div>
</template>

<script>
import SignupItem from "@/components/SignupItem.vue";
import LoginItem from "@/components/LoginItem.vue";
// Pinia built in function to merge the store with the component
import { mapStores } from "pinia";
// convention is to name the store with use and the name of the store at the end
import useAuthenticationStore from "@/stores/authentication";

export default {
  name: "AuthView",
  components: {
    SignupItem,
    LoginItem,
    ...mapStores(useAuthenticationStore),
  },
  data() {
    return {
      signup: false,
    };
  },
  methods: {
    signupPageShow() {
      this.signup = !this.signup;
    },
  },
};
</script>
