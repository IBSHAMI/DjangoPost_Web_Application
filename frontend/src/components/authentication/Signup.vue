<template>
  <!-- Sign up -->
  <div class="">
    <div class="">
      <div>
        <div
          v-if="sub_show_alert"
          class="text-center"
          :class="sub_alert_variant"
        >
          <span>
            {{ sub_alert_message }}
          </span>
        </div>
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <div class="text-center mt-2 mb-3">
            <h3 class="sign-up-header">Register new account</h3>
          </div>
          <vee-form action="#" :validation-schema="schema" @submit="register">
            <div class="form-group mb-3">
              <label for="email" class="py-1">Username</label>
              <vee-field
                class="form-control"
                type="text"
                name="username"
                id="username"
                placeholder="username"
              />
              <ErrorMessage name="username" class="invalid-input" />
            </div>
            <div class="form-group mb-3">
              <label for="email" class="py-1">Your email</label>
              <vee-field
                class="form-control"
                type="email"
                name="email"
                id="email"
                placeholder="name@company.com"
              />
              <ErrorMessage name="email" class="invalid-input" />
            </div>
            <div class="form-group mb-3">
              <label for="password" class="py-1">Password</label>
              <vee-field
                type="password"
                name="password"
                id="password"
                placeholder="••••••••"
                :bails="false"
                v-slot="{ field, errors }"
              >
                <input
                  type="password"
                  placeholder="••••••••"
                  v-bind="field"
                  class="form-control"
                />
                <div class="invalid-input" v-for="error in errors" :key="error">
                  {{ error }}
                </div>
              </vee-field>
            </div>
            <div class="form-group mb-3">
              <label for="confirm_password" class="py-1"
                >Confirm password</label
              >
              <vee-field
                class="form-control"
                type="password"
                name="confirm_password"
                id="confirm_password"
                placeholder="••••••••"
              />
              <ErrorMessage name="confirm_password" class="invalid-input" />
            </div>
            <div class="form-group mb-3">
              <vee-field
                class="form-check-input"
                id="terms"
                aria-describedby="terms"
                type="checkbox"
                name="terms"
                value="1"
              />

              <label for="terms" class="para form-check-label mx-2"
                >I accept the
                <a class="small-text" href="#">Terms and Conditions</a></label
              >

              <div>
                <ErrorMessage name="terms" class="invalid-input" />
              </div>
            </div>
            <div class="d-grid py-3">
              <button
                type="submit"
                class="btn button btn-lg button-primary"
                :disabled="sub_in_process"
              >
                Create an account
              </button>
            </div>
            <label class="para">
              Already have an account?
              <a
                class="fw-bold text-underline small-text"
                @click.prevent="signupPageShow"
                style="color: #11ab7c; cursor: pointer"
                >Login here</a
              >
            </label>
          </vee-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { signUpUser } from "@/services/authService";
import { API } from "@/api";

export default {
  name: "SignupItem",
  data() {
    return {
      schema: {
        username: "required|min:3|max:20|alpha_spaces",
        email: "required|min:3|max:100|email",
        password: "required|min:9|max:100|excluded_password:password",
        confirm_password: "confirmed:@password",
        terms: "required_terms",
      },
      sub_in_process: false,
      sub_show_alert: false,
      sub_alert_variant: "alert alert-info",
      sub_alert_message: "Please wait, processing your request",
    };
  },
  methods: {
    // this function will noot be called unless,
    // all from validation is passed
    async register(values) {
      // vales is an object with all the values from the form
      this.sub_show_alert = true;
      this.sub_in_process = true;
      this.sub_alert_variant = "alert alert-info";
      this.sub_alert_message = "Please wait, processing your request";

      const newUserData = {
        username: values.username,
        email: values.email,
        password: values.password,
      };
      const url = API.auth.register;
      const signUpResponse = await signUpUser(url, newUserData);

      if (signUpResponse) {
        this.sub_in_process = false;
        this.sub_alert_variant = "alert alert-success";
        this.sub_alert_message = "Registration successful, redirecting...";
        setTimeout(() => {
          this.sub_show_alert = false;
          this.signupPageShow();
        }, 2000);
      } else {
        this.sub_in_process = false;
        this.sub_alert_variant = "alert alert-danger";
        this.sub_alert_message = "Registration failed";
      }

      // // send data to the server
      // setTimeout(() => {
      //   axios
      //     .post(API.auth.register, newUserData)
      //     // eslint-disable-next-line no-unused-vars
      //     .then((res) => {
      //       this.sub_in_process = false;
      //       this.sub_alert_variant = "alert alert-success";
      //       this.sub_alert_message = "Registration successful, redirecting...";
      //       setTimeout(() => {
      //         this.sub_show_alert = false;
      //         this.signupPageShow();
      //       }, 2000);
      //     })
      //     // eslint-disable-next-line no-unused-vars
      //     .catch((err) => {
      //       this.sub_in_process = false;
      //       this.sub_alert_variant = "alert alert-danger";
      //       this.sub_alert_message = "Registration failed";
      //     });
      // }, 2000);
    },
    signupPageShow() {
      this.$emit("signup-page-show");
    },
  },
};
</script>

<style scoped>
.small-text {
  color: #11ab7c;
  font-weight: 400;
  transition: all 0.2s ease;
  font: 400 0.875rem/1.5rem var(--font-family);
}

.sign-up-header {
  font: 600 1.5rem/2rem var(--font-family);
  color: var(--text-color);
  font-size: 2rem;
  margin-bottom: 2rem;
}
</style>
