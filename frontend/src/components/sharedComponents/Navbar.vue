<template>
  <header class="header-area bg-white py-1">
    <div class="main-menu">
      <nav
        id="navbar-main"
        aria-label="Primary navigation"
        class="navbar navbar-expand-lg navbar-light"
      >
        <div class="container-fluid">
          <router-link class="navbar-brand" :to="{ name: 'LandingPage' }">
            DjangoPost
          </router-link>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <div class="mx-auto"></div>
            <ul class="nav navbar-nav">
              <li
                class="nav-item"
                v-show="
                  !authenticationStore.isAuthenticated ||
                  (authenticationStore.isAuthenticated && employeeProfile)
                "
              >
                <router-link
                  :to="{ name: 'Jobs', params: { slug: 'jobs' } }"
                  class="nav-link"
                >
                  Find Jobs
                </router-link>
              </li>
              <li
                class="nav-item"
                v-show="authenticationStore.isAuthenticated && companyProfile"
              >
                <router-link
                  :to="{ name: 'Company', params: { slug: 'data' } }"
                  class="nav-link"
                  >Company Profile</router-link
                >
              </li>
              <li
                class="nav-item"
                v-show="authenticationStore.isAuthenticated && companyProfile"
              >
                <router-link
                  :to="{ name: 'Company', params: { slug: 'jobs' } }"
                  class="nav-link"
                  >Jobs</router-link
                >
              </li>
              <li
                class="nav-item"
                v-show="authenticationStore.isAuthenticated && employeeProfile"
              >
                <router-link
                  :to="{ name: 'Profile', params: { slug: 'data' } }"
                  class="nav-link"
                >
                  Profile
                </router-link>
              </li>
              <li class="nav-item" v-show="authenticationStore.isAuthenticated">
                <router-link
                  :to="{ name: 'Profile', params: { slug: 'contact' } }"
                  class="nav-link"
                  >Contact Us</router-link
                >
              </li>
              <div v-if="!authenticationStore.isAuthenticated">
                <router-link
                  :to="{ name: 'Auth', params: { slug: 'signin' } }"
                  class="btn button button-primary"
                >
                  Login</router-link
                >
                <router-link
                  :to="{ name: 'Auth', params: { slug: 'signup' } }"
                  class="btn button button-primary"
                  >SignUp</router-link
                >
              </div>
              <div v-else-if="authenticationStore.isAuthenticated">
                <a
                  href=""
                  @click.prevent="logout"
                  class="btn button button-primary"
                >
                  logout</a
                >
                <router-link
                  v-if="pageType === 'home'"
                  :to="{ name: 'Profile', params: { slug: 'data' } }"
                  target="_blank"
                  class="btn button button-primary"
                  >Job Board</router-link
                >
                <router-link
                  v-if="employeeProfile && pageType === 'jobs'"
                  :to="{ name: 'Company', params: { slug: 'data' } }"
                  class="btn button button-primary"
                  >{{ "Post Jobs" }}</router-link
                >
                <router-link
                  v-if="companyProfile && pageType === 'jobs'"
                  :to="{ name: 'Profile', params: { slug: 'data' } }"
                  class="btn button button-primary"
                  >{{ "Find Jobs" }}</router-link
                >
              </div>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </header>
</template>

<script>
import useAuthenticationStore from "@/stores/authentication";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "HomeNavbar",
  props: ["pageType", "companyProfile", "employeeProfile"],
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

<style scoped>
/* start navigation styles */

.header-area .main-menu .navbar .btn {
  margin: 0.5rem 0.5rem;
}

.header-area .main-menu .navbar .navbar-brand {
  padding: 0 2rem 0 0;
  color: var(--primary-color);
  font-family: var(--Nunito);
  font-weight: 700;
}

.header-area .main-menu .navbar .navbar-brand:hover {
  background: var(--button-background-color);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.header-area .main-menu .navbar {
  margin: 16px 170px;
  padding: 0 15px;
}

.header-area .main-menu .nav-item .nav-link {
  font: normal 700 15px/2px var(--Nunito);
  text-transform: uppercase;
  padding: 2rem 1rem;
  color: #66799e;
}

.header-area .main-menu .navbar-nav .active {
  background: var(--gradient-color);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.header-area .main-menu .navbar-nav a:hover {
  background: var(--gradient-color);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* end navigation styles */
</style>
