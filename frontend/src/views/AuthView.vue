<template>
  <main>
    <section class="min-vh-100 d-flex align-items-center">
      <div class="container form-bg-image" :style="backgroundImageStyle">
        <div class="card rounded mx-auto col-lg-5 col-md-7">
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
    </section>
  </main>
</template>

<script>
import AuthSvg from "@/assets/img/auth/signin.svg";
import SignupItem from "@/components/authentication/Signup.vue";
import LoginItem from "@/components/authentication/Login.vue";

export default {
  name: "AuthView",
  created() {
    this.slug = this.$route.params.slug;
  },
  data() {
    return {
      authSVG: AuthSvg,
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
  computed: {
    backgroundImageStyle() {
      return `background-image: url(${this.authSVG});`;
    },
  },
};
</script>

<style scoped>
.rounded {
  border-radius: 0.5rem !important;
}

.card {
  border: 0;
  box-shadow: 0 0 1rem 0 rgba(136, 152, 170, 0.15);
}

.form-bg-image {
  background-repeat: no-repeat;
  background-position: top center;
}
</style>
