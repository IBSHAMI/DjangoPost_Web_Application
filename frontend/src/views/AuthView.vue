<template>
  <div>
    <div class="container d-flex justify-content-center py-5">
      <div class="card mx-auto col-lg-5 col-md-7">
        <div class="card-header bg-transparent pb-5" v-if="slug == 'signin'">
          <login-item @signupPageShow="signupPageShow" />
        </div>
        <div
          v-else-if="slug == 'signup'"
          class="card-header bg-transparent pb-5"
        >
          <signup-item @signupPageShow="signupPageShow" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SignupItem from "@/components/authentication/Signup.vue";
import LoginItem from "@/components/authentication/Login.vue";

export default {
  name: "AuthView",
  created() {
    this.slug = this.$route.params.slug;
  },
  data() {
    return {
      slug: this.slug,
    };
  },
  components: {
    SignupItem,
    LoginItem,
  },
  methods: {
    signupPageShow() {
      if (this.slug == "signup") {
        this.slug = "signin";
      } else {
        this.slug = "signup";
      }
    },
  },
};
</script>
