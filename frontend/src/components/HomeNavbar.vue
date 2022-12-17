<template>
  <header class="header-global">
    <nav
      id="navbar-main"
      aria-label="Primary navigation"
      class="navbar navbar-main navbar-expand-lg navbar-theme-primary headroom navbar-light"
    >
      <div class="container position-relative">
        <a class="navbar-brand me-lg-5" href="../../index.html">
          <img
            class="navbar-brand-light"
            src="../../assets/img/brand/dark.svg"
            alt="Logo dark"
          />
        </a>
        <div class="navbar-collapse collapse me-auto" id="navbar_global">
          <div class="navbar-collapse-header">
            <div class="row">
              <div class="col-6 collapse-close">
                <a
                  href="#navbar_global"
                  class="fas fa-times"
                  data-bs-toggle="collapse"
                  data-bs-target="#navbar_global"
                  aria-controls="navbar_global"
                  aria-expanded="false"
                  title="close"
                  aria-label="Toggle navigation"
                ></a>
              </div>
            </div>
          </div>
          <ul class="navbar-nav navbar-nav-hover align-items-lg-center">
            <li class="nav-item dropdown">
              <a href="#" class="nav-link">Pages</a>
            </li>
            <li class="nav-item dropdown">
              <a href="#" class="nav-link">Dashboard</a>
            </li>
          </ul>
        </div>
        <div class="d-flex align-items-center">
          <div v-if="!authenticationStore.isAuthenticated">
            <router-link
              :to="{ name: 'Auth', params: { slug: 'signin' } }"
              target="_blank"
              class="btn btn-outline-gray-100 d-none d-lg-inline me-md-3"
            >
              Login</router-link
            >
            <router-link
              :to="{ name: 'Auth', params: { slug: 'signup' } }"
              target="_blank"
              class="btn btn-primary"
              >SignUp</router-link
            >
          </div>
          <div v-else-if="authenticationStore.isAuthenticated">
            <a
              href=""
              target="_blank"
              @click.prevent="logout"
              class="btn btn-outline-gray-100 d-none d-lg-inline me-md-3"
            >
              logout</a
            >
            <router-link
              v-if="authenticationStore.isAuthenticated"
              :to="{ name: 'Profile', params: { slug: 'data' } }"
              target="_blank"
              class="btn btn-primary"
              >Job Board</router-link
            >
          </div>
          <button
            class="navbar-toggler ms-2"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbar_global"
            aria-controls="navbar_global"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import useAuthenticationStore from "@/stores/authentication";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "HomeNavbar",
  setup() {
    // initialize the authentification store
    const authenticationStore = useAuthenticationStore();

    // return the computed properties
    return {
      authenticationStore,
    };
  },
  methods: {
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
};
</script>

<style></style>
