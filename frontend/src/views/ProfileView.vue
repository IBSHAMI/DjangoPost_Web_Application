<template>
  <div>
    <Navbar
      class="pb-8"
      :employeeProfile="employeeProfile"
      :pageType="jobsPage"
    />
    <profile-data-item v-if="passedSlug === 'data'" />
    <profile-contact-item v-else-if="passedSlug === 'contact'" />
  </div>
</template>

<script>
import Navbar from "../components/sharedComponents/Navbar.vue";
import ProfileDataItem from "@/components/ProfileDataItem.vue";
import ProfileContactItem from "@/components/ProfileContactItem.vue";
import useAuthenticationStore from "@/stores/authentication";

export default {
  name: "ProfileView",
  beforeRouteEnter(to, from, next) {
    const authenticationStore = useAuthenticationStore();
    const isauthenticated = authenticationStore.isAuthenticated;

    // Check if user is loggin in, otherwise redirect to auth page
    if (!isauthenticated) {
      next({ name: "Auth" });
    } else {
      next();
    }
  },
  data() {
    return {
      passedSlug: this.$route.params.slug,
      employeeProfile: true,
      jobsPage: "jobs",
    };
  },
  components: {
    Navbar,
    ProfileDataItem,
    ProfileContactItem,
  },
  watch: {
    $route(to) {
      this.passedSlug = to.params.slug;
    },
  },
};
</script>

<style></style>
