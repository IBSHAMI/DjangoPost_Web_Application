<template>
  <!-- Sign in-->
  <div>
    <div>
      <div
        v-if="login_show_alert"
        class="text-center"
        :class="login_alert_variant"
      >
        <span>
          {{ login_alert_message }}
        </span>
      </div>
      <div class="text-center mt-2 mb-3">
        <h3 class="sign-in-header">Sign in</h3>
      </div>
      <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
        <vee-form action="#" :validation-schema="schema_login" @submit="login">
          <div class="form-group mb-3">
            <label for="email" class="py-1 form-label">Email Address:</label>
            <vee-field
              class="form-control"
              type="email"
              name="email"
              id="email"
              placeholder="name@company.com"
            />
            <ErrorMessage name="email" class="form-text error-message" />
          </div>
          <div class="form-group mb-3">
            <label for="password" class="py-1 form-label">Password</label>
            <vee-field
              class="form-control"
              type="password"
              name="password"
              id="password"
              placeholder="••••••••"
              required=""
            />
            <ErrorMessage name="password" class="form-text error-message" />
          </div>
          <div class="flex items-center justify-between">
            <a href="#" class="form-text pb-3 forget-pass">Forgot password?</a>
          </div>
          <div class="d-grid py-3">
            <button
              type="submit"
              :disabled="login_in_process"
              class="btn button btn-lg button-primary"
            >
              Sign In
            </button>
          </div>
          <p class="para">
            Don’t have an account yet?
            <a
              href="#"
              class="fw-bold text-underline forget-pass"
              @click.prevent="signupPageShow"
              >Sign up</a
            >
          </p>
        </vee-form>
      </div>
    </div>
  </div>
</template>

<script>
import { getAuthenticationStore } from "@/services/authService";
import { API } from "@/api";
import axios from "axios";

export default {
  name: "LoginItem",
  data() {
    return {
      schema_login: {
        email: "required|min:3|max:100",
        password: "required|min:9|max:100",
      },
      login_in_process: false,
      login_show_alert: false,
      login_alert_variant: "alert alert-info",
      login_alert_message: "Please wait, processing your request",
      authenticationStore: getAuthenticationStore(),
    };
  },
  methods: {
    login(values) {
      // vales is an object with all the values from the form
      this.login_show_alert = true;
      this.login_in_process = true;
      this.login_alert_variant = "alert alert-info";
      this.login_alert_message = "Please wait, processing your request";

      const loginCredentials = {
        email: values.email,
        password: values.password,
      };

      // send the login credentials to the server
      axios
        .post(API.auth.login, loginCredentials)
        .then((response) => {
          this.login_in_process = false;
          this.login_alert_variant = "alert alert-success";
          this.login_alert_message = "Login successful, redirecting...";
          // save the token in the store
          const token = response.data.auth_token;
          this.authenticationStore.setToken(token);
          this.authenticationStore.setUser(loginCredentials.email);

          this.authenticationStore.getAccountPictures();
          this.authenticationStore.checkIfProfileComplete();

          setTimeout(() => {
            this.$router.push({ name: "Jobs", params: { slug: "jobs" } });
          }, 3000);
        })
        // eslint-disable-next-line no-unused-vars
        .catch((error) => {
          this.login_in_process = false;
          this.login_alert_variant = "alert alert-danger";
          this.login_alert_message = "Login failed, please try again";
          console.log(error);
        });
    },
    signupPageShow() {
      this.$emit("signup-page-show");
    },
  },
};
</script>

<style scoped>
.forget-pass {
  color: #11ab7c;
  font-weight: 400;
  transition: all 0.2s ease;
  font: 400 0.875rem/1.5rem var(--font-family);
}

.sign-in-header {
  font: 600 1.5rem/2rem var(--font-family);
  color: var(--text-color);
  font-size: 2rem;
  margin-bottom: 2rem;
}
</style>
