<template>
  <div>
    <div class="relative bg-white mx-auto max-w-7xl px-4 sm:px-6">
      <main-navbar-item class="pb-8" />
      <profile-data-item v-if="(passedSlug = 'data')" />
    </div>
  </div>
</template>

<script>
import MainNavbarItem from "@/components/MainNavbarItem.vue";
import ProfileDataItem from "@/components/ProfileDataItem.vue";

export default {
  name: "ProfileView",
  data() {
    return {
      passedSlug: this.$route.params.slug,
    };
  },

  components: {
    MainNavbarItem,
    ProfileDataItem,
  },
};
</script>

<style></style>
