<template>
  <!-- Sign up -->
  <section class="absolute w-full h-full bg-[#6b7280]">
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
          v-if="sub_show_alert"
          class="text-black px-6 py-4 border-0 rounded relative mb-4"
          :class="sub_alert_variant"
        >
          <span class="text-xl inline-block mr-5 align-middle">
            <i class="fas fa-bell" />
          </span>
          <span class="inline-block align-middle mr-8">
            {{ sub_alert_message }}
          </span>
        </div>
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1
            class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white"
          >
            Create an account
          </h1>
          <vee-form
            class="space-y-4 md:space-y-6"
            action="#"
            :validation-schema="schema"
            @submit="register"
          >
            <div>
              <label
                for="email"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Username</label
              >
              <vee-field
                type="text"
                name="username"
                id="username"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="username"
              />
              <ErrorMessage
                name="username"
                class="text-red-500 text-xs italic"
              />
            </div>
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
              <ErrorMessage name="email" class="text-red-500 text-xs italic" />
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
                :bails="false"
                v-slot="{ field, errors }"
              >
                <input
                  type="password"
                  placeholder="••••••••"
                  v-bind="field"
                  class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                />
                <div
                  class="text-red-500 text-xs italic"
                  v-for="error in errors"
                  :key="error"
                >
                  {{ error }}
                </div>
              </vee-field>
              <ErrorMessage
                name="password"
                class="text-red-500 text-xs italic"
              />
            </div>
            <div>
              <label
                for="confirm_password"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Confirm password</label
              >
              <vee-field
                type="confirm_password"
                name="confirm_password"
                id="confirm_password"
                placeholder="••••••••"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              />
              <ErrorMessage
                name="confirm_password"
                class="text-red-500 text-xs italic"
              />
            </div>
            <div class="flex items-start">
              <div class="flex items-center h-5">
                <vee-field
                  id="terms"
                  aria-describedby="terms"
                  type="checkbox"
                  class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"
                  name="terms"
                  value="1"
                />
              </div>
              <div class="ml-3 text-sm">
                <label
                  for="terms"
                  class="font-light text-gray-500 dark:text-gray-300"
                  >I accept the
                  <a
                    class="font-medium text-primary-600 hover:underline dark:text-primary-500"
                    href="#"
                    >Terms and Conditions</a
                  ></label
                >
              </div>
            </div>
            <div>
              <ErrorMessage name="terms" class="text-red-500 text-xs italic" />
            </div>
            <button
              type="submit"
              :disabled="sub_in_process"
              class="bg-sky-500 text-white active:bg-blue-600 font-bold uppercase text-base px-8 py-3 rounded shadow-md hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
            >
              Create an account
            </button>
            <p class="text-sm font-light text-gray-500 dark:text-gray-400">
              Already have an account?
              <a
                href="#"
                class="font-medium text-primary-600 hover:underline dark:text-primary-500"
                @click.prevent="signupPageShow"
                >Login here</a
              >
            </p>
          </vee-form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { API } from "@/api";
import axios from "axios";

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
      sub_alert_variant: "bg-red-500",
      sub_alert_message: "Please wait, processing your request",
    };
  },
  methods: {
    // this function will noot be called unless,
    // all from validation is passed
    register(values) {
      // vales is an object with all the values from the form
      this.sub_show_alert = true;
      this.sub_in_process = true;
      this.sub_alert_variant = "bg-blue-500";
      this.sub_alert_message = "Please wait, processing your request";

      // show that the form submission is successful
      this.sub_alert_variant = "bg-green-500";
      this.sub_alert_message = "Registration successful";

      const newUserData = {
        username: values.username,
        email: values.email,
        password: values.password,
      };

      // send the new user data to the server
      axios
        .post(API.auth.register, newUserData)
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    signupPageShow() {
      this.$emit("signup-page-show");
    },
  },
};
</script>
