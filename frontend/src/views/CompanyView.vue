<template>
  <div>
    <main-navbar-item :companyProfile="companyProfile" />
  </div>
</template>

<script>
import MainNavbarItem from "@/components/MainNavbarItem.vue";

export default {
  name: "CompanyView",
  data() {
    return {
      companyProfile: true,
    };
  },
  components: {
    MainNavbarItem,
  },
};
</script>

<style></style>
