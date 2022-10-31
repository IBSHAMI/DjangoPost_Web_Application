<template>
  <div>
    <main-navbar-item />
    <profile-data v-if="(passedSlug = 'data')" />
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
