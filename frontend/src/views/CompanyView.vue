<template>
  <div class="relative bg-white mx-auto max-w-7xl px-4 sm:px-6">
    <main-navbar-item class="pb-8" :companyProfile="companyProfile" />
    <company-data-item v-if="passedSlug === 'data'" />
    <jobs-forms-item v-if="passedSlug === 'jobs'" />
  </div>
</template>

<script>
import MainNavbarItem from "@/components/MainNavbarItem.vue";
import CompanyDataItem from "../components/CompanyDataItem.vue";
import JobsFormsItem from "../components/JobsFormsItem.vue";

export default {
  name: "CompanyView",
  data() {
    return {
      companyProfile: true,
      passedSlug: this.$route.params.slug,
    };
  },
  components: {
    MainNavbarItem,
    CompanyDataItem,
    JobsFormsItem,
  },
  $route(to) {
    this.passedSlug = to.params.slug;
  },
};
</script>

<style></style>
