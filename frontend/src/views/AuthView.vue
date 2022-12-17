<template>
  <div>
    <div class="container d-flex justify-content-center py-5">
      <div class="card mx-auto col-lg-5 col-md-7">
        <div class="card-header bg-transparent pb-5" v-if="!signup">
          <login-item @signupPageShow="signupPageShow" />
        </div>
        <div v-else-if="signup" class="card-header bg-transparent pb-5">
          <signup-item @signupPageShow="signupPageShow" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SignupItem from "@/components/SignupItem.vue";
import LoginItem from "@/components/LoginItem.vue";

export default {
  name: "AuthView",
  created() {
    this.signup = this.$route.params.signup;
  },
  data() {
    return {
      signup: this.signup,
    };
  },
  components: {
    SignupItem,
    LoginItem,
  },
  methods: {
    signupPageShow() {
      this.signup = !this.signup;
    },
  },
};
</script>
