<template>
  <div>
    <main-navbar-item />
  </div>
</template>

<script>
import MainNavbarItem from "@/components/MainNavbarItem.vue";

export default {
  name: "ProfileView",
  props: {
    // this is the prop that will be passed from the router
    // this prop will be used to know what to show
    // in the profile view
    slug: {
      type: String,
      required: true,
    },
  },
  components: {
    MainNavbarItem,
  },
};
</script>

<style></style>
