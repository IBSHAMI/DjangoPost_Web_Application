<template>
  <div>
    <main-navbar-item :employeeProfile="employeeProfile" />
  </div>
</template>

<script>
import MainNavbarItem from "@/components/MainNavbarItem.vue";

export default {
  name: "JobsView",
  data() {
    return {
      employeeProfile: true,
    };
  },
  components: {
    MainNavbarItem,
  },
};
</script>

<style></style>
