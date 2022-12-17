<template>
  <div>
    <div class="mx-auto max-w-7xl px-4 sm:px-6">
      <div
        class="flex items-center justify-between border-b-2 border-gray-100 py-6 md:justify-start md:space-x-10"
      >
        <div class="flex justify-start lg:w-0 lg:flex-1">
          <a href="#">
            <span class="sr-only">Your Company</span>
            <img
              class="h-8 w-auto sm:h-10"
              src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600"
              alt=""
            />
          </a>
        </div>
        <div class="-my-2 -mr-2 md:hidden">
          <button
            type="button"
            class="inline-flex items-center justify-center rounded-md bg-white p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500"
            aria-expanded="false"
          >
            <span class="sr-only">Open menu</span>
            <!-- Heroicon name: outline/bars-3 -->
            <svg
              class="h-6 w-6"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              aria-hidden="true"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
              />
            </svg>
          </button>
        </div>
        <div v-if="employeeProfile">
          <nav
            class="hidden space-x-10 md:flex"
            v-if="!authenticationStore.isAuthenticated"
          >
            <router-link
              :to="{ name: 'Auth' }"
              class="text-base font-medium text-gray-500 hover:text-gray-900"
              >Login/Signup</router-link
            >
          </nav>
          <nav
            class="hidden space-x-10 md:flex"
            v-else-if="authenticationStore.isAuthenticated"
          >
            <a
              href="#"
              class="text-base font-medium text-gray-500 hover:text-gray-900"
              ><svg
                xmlns="http://www.w3.org/2000/svg"
                name="notification"
                focusable="false"
                role="img"
                fill="currentColor"
                viewBox="0 0 24 24"
                aria-hidden="true"
                class="h-6 w-6"
              >
                <path
                  d="M12 2a1.5 1.5 0 00-1.5 1.5v.161A7.003 7.003 0 005 10.5V16l-1.854 1.854a.5.5 0 00-.146.353v.293a.5.5 0 00.5.5h17a.5.5 0 00.5-.5v-.293a.5.5 0 00-.146-.353L19 16v-5.5a7.003 7.003 0 00-5.5-6.839V3.5A1.5 1.5 0 0012 2zm0 20a3.001 3.001 0 01-2.83-2h5.66A3.001 3.001 0 0112 22z"
                ></path>
              </svg>
            </a>

            <div class="relative" @click.prevent="toggleDropdown">
              <!-- Item active: "text-gray-900", Item inactive: "text-gray-500" -->
              <button
                type="button"
                class="text-gray-500 group inline-flex items-center rounded-md bg-white text-base font-medium hover:text-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                aria-expanded="false"
              >
                <svg
                  class="h-6 w-6"
                  name="profile"
                  xmlns="http://www.w3.org/2000/svg"
                  focusable="false"
                  role="img"
                  fill="currentColor"
                  viewBox="0 0 24 24"
                  aria-hidden="true"
                >
                  <path
                    d="M12 12c2.486 0 4.5-2.014 4.5-4.5S14.486 3 12 3a4.499 4.499 0 00-4.5 4.5C7.5 9.986 9.514 12 12 12zm0 2.25c-3.004 0-9 1.508-9 4.5v1.75a.5.5 0 00.5.5h17a.5.5 0 00.5-.5v-1.75c0-2.992-5.996-4.5-9-4.5z"
                  ></path>
                </svg>
              </button>
              <div
                class="absolute left-1/2 z-10 mt-3 w-screen max-w-md -translate-x-1/2 transform px-2 sm:px-0 dropdown-content"
                :style="{ display: dropdownOpen ? 'block' : 'none' }"
              >
                <div
                  class="overflow-hidden rounded-lg shadow-lg ring-1 ring-black ring-opacity-5"
                >
                  <div
                    class="relative grid gap-6 bg-white px-5 py-6 sm:gap-8 sm:p-8"
                  >
                    <router-link
                      to="/profile/data"
                      class="-m-3 flex items-start rounded-lg p-3 hover:bg-gray-50"
                    >
                      <!-- Heroicon name: outline/lifebuoy -->
                      <svg
                        class="h-6 w-6 flex-shrink-0 text-indigo-600"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke-width="1.5"
                        stroke="currentColor"
                        aria-hidden="true"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          d="M16.712 4.33a9.027 9.027 0 011.652 1.306c.51.51.944 1.064 1.306 1.652M16.712 4.33l-3.448 4.138m3.448-4.138a9.014 9.014 0 00-9.424 0M19.67 7.288l-4.138 3.448m4.138-3.448a9.014 9.014 0 010 9.424m-4.138-5.976a3.736 3.736 0 00-.88-1.388 3.737 3.737 0 00-1.388-.88m2.268 2.268a3.765 3.765 0 010 2.528m-2.268-4.796a3.765 3.765 0 00-2.528 0m4.796 4.796c-.181.506-.475.982-.88 1.388a3.736 3.736 0 01-1.388.88m2.268-2.268l4.138 3.448m0 0a9.027 9.027 0 01-1.306 1.652c-.51.51-1.064.944-1.652 1.306m0 0l-3.448-4.138m3.448 4.138a9.014 9.014 0 01-9.424 0m5.976-4.138a3.765 3.765 0 01-2.528 0m0 0a3.736 3.736 0 01-1.388-.88 3.737 3.737 0 01-.88-1.388m2.268 2.268L7.288 19.67m0 0a9.024 9.024 0 01-1.652-1.306 9.027 9.027 0 01-1.306-1.652m0 0l4.138-3.448M4.33 16.712a9.014 9.014 0 010-9.424m4.138 5.976a3.765 3.765 0 010-2.528m0 0c.181-.506.475-.982.88-1.388a3.736 3.736 0 011.388-.88m-2.268 2.268L4.33 7.288m6.406 1.18L7.288 4.33m0 0a9.024 9.024 0 00-1.652 1.306A9.025 9.025 0 004.33 7.288"
                        />
                      </svg>
                      <div class="ml-4">
                        <p class="text-base font-medium text-gray-900">
                          Your Profile
                        </p>
                        <p class="mt-1 text-sm text-gray-500">
                          View your profile data and edit and upload your latest
                          resume.
                        </p>
                      </div>
                    </router-link>

                    <a
                      href="#"
                      class="-m-3 flex items-start rounded-lg p-3 hover:bg-gray-50"
                    >
                      <!-- Heroicon name: outline/bookmark-square -->
                      <svg
                        class="h-6 w-6 flex-shrink-0 text-indigo-600"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke-width="1.5"
                        stroke="currentColor"
                        aria-hidden="true"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          d="M16.5 3.75V16.5L12 14.25 7.5 16.5V3.75m9 0H18A2.25 2.25 0 0120.25 6v12A2.25 2.25 0 0118 20.25H6A2.25 2.25 0 013.75 18V6A2.25 2.25 0 016 3.75h1.5m9 0h-9"
                        />
                      </svg>
                      <div class="ml-4">
                        <p class="text-base font-medium text-gray-900">
                          Jobs Histroy
                        </p>
                        <p class="mt-1 text-sm text-gray-500">
                          Learn how to maximize our platform to get the most out
                          of it.
                        </p>
                      </div>
                    </a>

                    <router-link
                      to="/profile/contact"
                      class="-m-3 flex items-start rounded-lg p-3 hover:bg-gray-50"
                    >
                      <!-- Heroicon name: outline/calendar -->
                      <svg
                        class="h-6 w-6 flex-shrink-0 text-indigo-600"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke-width="1.5"
                        stroke="currentColor"
                        aria-hidden="true"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5"
                        />
                      </svg>
                      <div class="ml-4">
                        <p class="text-base font-medium text-gray-900">
                          Contacts
                        </p>
                        <p class="mt-1 text-sm text-gray-500">
                          See what meet-ups and other events we might be
                          planning near you.
                        </p>
                      </div>
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
          </nav>
        </div>
        <div v-else-if="companyProfile">
          <nav class="space-x-10 md:flex">
            <router-link
              :to="{ name: 'Company', params: { slug: 'data' } }"
              class="text-base font-medium text-gray-500 hover:text-gray-900"
              >Company Profile</router-link
            >
            <!-- <router-link
              to=""
              class="text-base font-medium text-gray-500 hover:text-gray-900"
              >Create Job</router-link
            > -->
            <router-link
              :to="{ name: 'Company', params: { slug: 'jobs' } }"
              class="text-base font-medium text-gray-500 hover:text-gray-900"
              >Jobs</router-link
            >
          </nav>
        </div>
        <div class="hidden items-center justify-end md:flex md:flex-1 lg:w-0">
          <a
            href="#"
            @click.prevent="logout"
            class="whitespace-nowrap text-base font-medium text-gray-500 hover:text-gray-900"
          >
            Logout
          </a>
          <router-link
            v-if="employeeProfile"
            :to="{ name: 'Company', params: { slug: 'data' } }"
            class="ml-8 inline-flex items-center justify-center whitespace-nowrap rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-base font-medium text-white shadow-sm hover:bg-indigo-700"
            >{{ "Post Jobs" }}</router-link
          >
          <router-link
            v-if="companyProfile"
            :to="{ name: 'Profile', params: { slug: 'data' } }"
            class="ml-8 inline-flex items-center justify-center whitespace-nowrap rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-base font-medium text-white shadow-sm hover:bg-indigo-700"
            >{{ "Find Jobs" }}</router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import useprofileDropdownStore from "@/stores/profile_dropdown.js";
import useAuthenticationStore from "@/stores/authentication";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "MainNavbarItem",
  setup() {
    // Initialize the dropdown
    const dropdownStore = useprofileDropdownStore();

    // initialize the authentification store
    const authenticationStore = useAuthenticationStore();

    // initialize the company employee sections store

    return {
      dropdownStore,
      authenticationStore,
    };
  },
  data() {
    return {};
  },
  props: ["companyProfile", "employeeProfile"],
  methods: {
    toggleDropdown() {
      this.dropdownStore.toggleDropdown();
    },
    logout() {
      console.log("logout");
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        "content-type": "application/json",
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      // Send the request to the backend to logout
      axios
        .post(API.auth.logout, token, {
          headers: headers,
        })
        .then((response) => {
          // If the logout was successful, remove the token from the store
          console.log(response);
          this.authenticationStore.logout();
          this.$router.go();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  computed: {
    dropdownOpen() {
      return this.dropdownStore.dropdownOpen;
    },
  },
};
</script>

<style></style>
