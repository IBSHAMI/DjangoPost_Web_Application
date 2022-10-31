<template>
  <div>
    <div class="relative bg-white mx-auto max-w-7xl px-4 sm:px-6">
      <main-navbar-item class="pb-8" />
      <profile-data v-if="(passedSlug = 'data')" />
    </div>
  </div>
</template>

<script>
import MainNavbarItem from "@/components/MainNavbarItem.vue";
import ProfileData from "@/components/ProfileData.vue";

export default {
  name: "ProfileView",
  data() {
    return {
      passedSlug: this.$route.params.slug,
    };
  },

  components: {
    MainNavbarItem,
    ProfileData,
  },
};
</script>

<style></style>
