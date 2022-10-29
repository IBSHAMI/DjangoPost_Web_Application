<template>
  <!-- Sign in-->
  <section class="absolute w-full h-full bg-[#6b7280]">
    <div>
      <div
        class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0"
      >
        <a
          href="#"
          class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white"
        >
          <img
            class="w-8 h-8 mr-2"
            src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/logo.svg"
            alt="logo"
          />
          Flowbite
        </a>
        <div
          class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700"
        >
          <div
            v-if="login_show_alert"
            class="text-white px-6 py-4 border-0 rounded relative mb-4 bg-indigo-500"
            :class="login_alert_variant"
          >
            <span class="text-xl inline-block mr-5 align-middle">
              <i class="fas fa-bell" />
            </span>
            <span class="inline-block align-middle mr-8">
              {{ login_alert_message }}
            </span>
          </div>
          <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
            <h1
              class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white"
            >
              Sign in to your account
            </h1>
            <vee-form
              class="space-y-4 md:space-y-6"
              action="#"
              :validation-schema="schema_login"
              @submit="login"
            >
              <div>
                <label
                  for="email"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Your email</label
                >
                <vee-field
                  type="email"
                  name="email"
                  id="email"
                  class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="name@company.com"
                />
                <ErrorMessage
                  name="email"
                  class="text-red-500 text-xs italic"
                />
              </div>
              <div>
                <label
                  for="password"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Password</label
                >
                <vee-field
                  type="password"
                  name="password"
                  id="password"
                  placeholder="••••••••"
                  class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  required=""
                />
                <ErrorMessage
                  name="password"
                  class="text-red-500 text-xs italic"
                />
              </div>
              <div class="flex items-center justify-between">
                <div class="flex items-start">
                  <div class="flex items-center h-5">
                    <input
                      id="remember"
                      aria-describedby="remember"
                      type="checkbox"
                      class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"
                      required=""
                    />
                  </div>
                  <div class="ml-3 text-sm">
                    <label
                      for="remember"
                      class="text-gray-500 dark:text-gray-300"
                      >Remember me</label
                    >
                  </div>
                </div>
                <a
                  href="#"
                  class="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500"
                  >Forgot password?</a
                >
              </div>
              <button
                type="submit"
                :disabled="login_in_process"
                class="bg-sky-500 text-white active:bg-blue-600 font-bold uppercase text-base px-8 py-3 rounded shadow-md hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
              >
                Sign In
              </button>
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
  </section>
</template>

<script>
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
      login_alert_variant: "bg-red-500",
      login_alert_message: "Please wait, processing your request",
    };
  },
  methods: {
    login(values) {
      // vales is an object with all the values from the form
      this.login_show_alert = true;
      this.login_in_process = true;
      this.login_alert_variant = "bg-blue-500";
      this.login_alert_message = "Please wait, processing your request";

      const loginCredentials = {
        email: values.email,
        password: values.password,
      };

      // send the login credentials to the server
      axios
        .post(API.auth.login, loginCredentials)
        .then((res) => console.log(res))
        .catch((err) => console.log(err));

      // show that the form submission is successful
      this.login_alert_variant = "bg-green-500";
      this.login_alert_message = "Login successful";
    },
    signupPageShow() {
      this.$emit("signupPageShow");
    },
  },
};
</script>
