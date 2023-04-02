<template>
  <div>
    <button
      class="btn button button-outline-primary"
      role="button"
      aria-label="option"
      @click="showDropdown = !showDropdown"
    >
      <svg
        class=""
        onclick=""
        xmlns="http://www.w3.org/2000/svg"
        width="20"
        height="20"
        viewBox="0 0 20 20"
        fill="none"
      >
        <path
          d="M4.16667 10.8332C4.62691 10.8332 5 10.4601 5 9.99984C5 9.5396 4.62691 9.1665 4.16667 9.1665C3.70643 9.1665 3.33334 9.5396 3.33334 9.99984C3.33334 10.4601 3.70643 10.8332 4.16667 10.8332Z"
          stroke="#9CA3AF"
          stroke-width="1.25"
          stroke-linecap="round"
          stroke-linejoin="round"
        ></path>
        <path
          d="M10 10.8332C10.4602 10.8332 10.8333 10.4601 10.8333 9.99984C10.8333 9.5396 10.4602 9.1665 10 9.1665C9.53976 9.1665 9.16666 9.5396 9.16666 9.99984C9.16666 10.4601 9.53976 10.8332 10 10.8332Z"
          stroke="#9CA3AF"
          stroke-width="1.25"
          stroke-linecap="round"
          stroke-linejoin="round"
        ></path>
        <path
          d="M15.8333 10.8332C16.2936 10.8332 16.6667 10.4601 16.6667 9.99984C16.6667 9.5396 16.2936 9.1665 15.8333 9.1665C15.3731 9.1665 15 9.5396 15 9.99984C15 10.4601 15.3731 10.8332 15.8333 10.8332Z"
          stroke="#9CA3AF"
          stroke-width="1.25"
          stroke-linecap="round"
          stroke-linejoin="round"
        ></path>
      </svg>
    </button>
    <div
      class="dropdown-content bg-white shadow w-24 absolute z-30 right-0 mr-6"
      :class="{ hidden: !showDropdown }"
    >
      <div
        tabindex="0"
        class="focus:outline-none focus:text-indigo-600 text-xs w-full hover:bg-indigo-700 py-4 px-4 cursor-pointer hover:text-white"
      >
        <p>Edit</p>
      </div>
      <div
        tabindex="0"
        class="focus:outline-none focus:text-indigo-600 text-xs w-full hover:bg-indigo-700 py-4 px-4 cursor-pointer hover:text-white"
        @click.prevent="deleteJob"
      >
        <p>Delete</p>
      </div>
    </div>
  </div>
</template>

<script>
import { getAuthenticationStore } from "@/services/authService";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "JobsDropdownItem",
  props: ["jobId"],
  data() {
    return {
      showDropdown: false,
      authenticationStore: getAuthenticationStore(),
    };
  },
  methods: {
    deleteJob() {
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };
      const jobDeleteUrl = API.jobs.list + `${this.jobId}/delete/`;

      axios.delete(jobDeleteUrl, { headers }).then((response) => {
        console.log(response);
        setTimeout(() => {
          this.$router.go();
        }, 1000);
      });
    },
  },
};
</script>

<style></style>
