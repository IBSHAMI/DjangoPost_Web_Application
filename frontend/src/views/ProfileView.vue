<template>
  <section class="min-vh-100 h-100">
    <div>
      <Navbar
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
import Navbar from "../components/sharedComponents/Navbar.vue";
import ProfileData from "@/components/ProfileData.vue";
import ContactUsForm from "@/components/ContactUsForm.vue";
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
