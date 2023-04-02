<template>
  <section class="min-vh-100 h-100">
    <div>
      <shared-component-navbar
        class="pb-8"
        :employeeProfile="employeeProfile"
        :pageType="jobsPage"
      />
    </div>
    <profile-data v-if="passedSlug === 'data'" />
    <contact-us-form v-else-if="passedSlug === 'contact'" />
  </section>
</template>

<script>
import ProfileData from "@/components/ProfileData.vue";
import ContactUsForm from "@/components/ContactUsForm.vue";
import { getAuthenticationStore } from "@/services/authService";

export default {
  name: "ProfileView",
  beforeRouteEnter(to, from, next) {
    const authenticationStore = getAuthenticationStore();
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
    ProfileData,
    ContactUsForm,
  },
  watch: {
    $route(to) {
      this.passedSlug = to.params.slug;
    },
  },
};
</script>

<style></style>
