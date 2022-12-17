<template>
  <!-- Sign in-->
  <div>
    <div>
      <div class="">
        <div>
          <div v-if="login_show_alert" class="" :class="login_alert_variant">
            <span class="text-xl inline-block mr-5 align-middle">
              <i class="fas fa-bell" />
            </span>
            <span class="inline-block align-middle mr-8">
              {{ login_alert_message }}
            </span>
          </div>
          <div class="text-center mt-2 mb-3"><h3>Sign in with</h3></div>
          <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
            <vee-form
              action="#"
              :validation-schema="schema_login"
              @submit="login"
            >
              <div class="form-group mb-3">
                <label for="email" class="py-1">Email Address:</label>
                <vee-field
                  class="form-control"
                  type="email"
                  name="email"
                  id="email"
                  placeholder="name@company.com"
                />
                <ErrorMessage name="email" class="form-text text-red" />
              </div>
              <div class="form-group mb-3">
                <label for="password" class="py-1">Password</label>
                <vee-field
                  class="form-control"
                  type="password"
                  name="password"
                  id="password"
                  placeholder="••••••••"
                  required=""
                />
                <ErrorMessage name="password" class="form-text text-red" />
              </div>
              <div class="flex items-center justify-between">
                <a href="#" class="form-text pb-3">Forgot password?</a>
              </div>
              <div class="d-grid py-3">
                <button
                  type="submit"
                  :disabled="login_in_process"
                  class="btn btn-primary"
                >
                  Sign In
                </button>
              </div>
              <p class="text-sm font-light text-gray-500 dark:text-gray-400">
                Don’t have an account yet?
                <a
                  href="#"
                  class="font-medium text-primary-600 hover:underline dark:text-primary-500"
                  @click.prevent="signupPageShow"
                  >Sign up</a
                >
              </p>
            </vee-form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import useAuthenticationStore from "@/stores/authentication";
import { API } from "@/api";
import axios from "axios";

export default {
  name: "LoginItem",
  setup() {
    // init the store
    const authenticationStore = useAuthenticationStore();
    return { authenticationStore };
  },
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
      setTimeout(() => {
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
            setTimeout(() => {
              this.$router.push({ name: "Jobs" });
            }, 1000);
          })
          // eslint-disable-next-line no-unused-vars
          .catch((error) => {
            this.login_in_process = false;
            this.login_alert_variant = "alert alert-danger";
            this.login_alert_message = "Login failed, please try again";
            console.log(error);
          });
      }, 1000);
    },
    signupPageShow() {
      this.$emit("signupPageShow");
    },
  },
};
</script>
