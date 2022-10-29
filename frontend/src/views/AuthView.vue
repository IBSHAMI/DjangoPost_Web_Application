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

export default {
  name: "AuthView",
  components: {
    SignupItem,
    LoginItem,
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
