<template>
  <div>
    <div class="relative bg-white mx-auto max-w-7xl px-4 sm:px-6">
      <main-navbar-item class="pb-8" />
      <profile-data-item v-if="passedSlug === 'data'" />
      <profile-contact-item v-else-if="passedSlug === 'contact'" />
    </div>
  </div>
</template>

<script>
import MainNavbarItem from "@/components/MainNavbarItem.vue";
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
    };
  },
  components: {
    MainNavbarItem,
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
