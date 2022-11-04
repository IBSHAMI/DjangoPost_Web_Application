<template>
  <section class="text-gray-600 body-font relative">
    <div class="container px-5 py-12 mx-auto">
      <div class="flex flex-col text-center w-full mb-12">
        <h1
          class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900"
        >
          Contact Us
        </h1>
        <p class="lg:w-2/3 mx-auto leading-relaxed text-base">
          Whatever cardigan tote bag tumblr hexagon brooklyn asymmetrical
          gentrify.
        </p>
      </div>
      <div class="lg:w-1/2 md:w-2/3 mx-auto">
        <vee-form action="#" :validation-schema="schema">
          <div class="flex flex-wrap -m-2">
            <div class="p-2 w-1/2">
              <div class="relative">
                <label for="name" class="leading-7 text-sm text-gray-600"
                  >First Name</label
                >
                <ErrorMessage
                  name="first_name"
                  class="text-red-500 text-xs italic"
                />
                <div>
                  <vee-field
                    type="text"
                    id="first_name"
                    name="first_name"
                    v-model="firstName"
                    class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                  />
                </div>
              </div>
            </div>
            <div class="p-2 w-1/2">
              <div class="relative">
                <label for="email" class="leading-7 text-sm text-gray-600"
                  >Last name</label
                >
                <ErrorMessage
                  name="last_name"
                  class="text-red-500 text-xs italic"
                />
                <div>
                  <vee-field
                    type="test"
                    id="last_name"
                    name="last_name"
                    v-model="lastName"
                    class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                  />
                </div>
              </div>
            </div>
            <div class="p-2 w-1/2">
              <div class="relative">
                <label for="email" class="leading-7 text-sm text-gray-600"
                  >Email</label
                >
                <ErrorMessage
                  name="email"
                  class="text-red-500 text-xs italic"
                />
                <div>
                  <vee-field
                    type="email"
                    id="email"
                    name="email"
                    v-model="email"
                    class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                  />
                </div>
              </div>
            </div>
            <div class="p-2 w-full">
              <div class="relative">
                <label for="message" class="leading-7 text-sm text-gray-600"
                  >Message</label
                >
                <textarea
                  id="message"
                  name="message"
                  class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"
                ></textarea>
              </div>
            </div>
            <div class="p-2 w-full">
              <button
                class="flex mx-auto text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg"
              >
                Submit
              </button>
            </div>
            <div
              class="p-2 w-full pt-8 mt-8 border-t border-gray-200 text-center"
            >
              <a class="text-indigo-500">example@email.com</a>
              <p class="leading-normal my-5">
                49 Smith St. <br />Saint Cloud, MN 56301
              </p>
            </div>
          </div>
        </vee-form>
      </div>
    </div>
  </section>
</template>

<script>
import useAuthenticationStore from "@/stores/authentication";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "ProfileContactItem",
  created() {
    this.getUserDate();
  },
  data() {
    return {
      firstName: "",
      lastName: "",
      email: "",
      message: "",

      schema: {
        firstName: {
          required: true,
          min: 3,
          max: 255,
        },
        lastName: {
          required: true,
          min: 3,
          max: 255,
        },
        email: {
          required: true,
          email: true,
          min: 3,
          max: 255,
        },
        message: {
          required: true,
          min: 3,
          max: 255,
        },
      },
    };
  },
  setup() {
    // init the store
    const authenticationStore = useAuthenticationStore();
    return { authenticationStore };
  },
  methods: {
    getUserDate() {
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        "content-type": "application/json",
        // eslint-disable-next-line prettier/prettier
        "Authorization": token,
      };

      axios
        .get(API.employee.details, { headers: headers })
        .then((response) => {
          console.log(response.data);
          this.firstName = response.data.first_name;
          this.lastName = response.data.last_name;
          this.email = response.data.email;
        })
        // eslint-disable-next-line no-unused-vars
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style></style>
