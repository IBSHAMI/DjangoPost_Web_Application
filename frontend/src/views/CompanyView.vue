<template>
  <div>
    <Navbar
      class="pb-8"
      :companyProfile="companyProfile"
      :pageType="jobsPage"
    />
    <company-data-item v-if="passedSlug === 'data'" />
    <jobs-forms-item v-else-if="passedSlug === 'jobs'" />
    <create-job-form-item v-else-if="passedSlug === 'create-job'" />
  </div>
</template>

<script>
import Navbar from "../components/sharedComponents/Navbar.vue";
import CompanyDataItem from "../components/CompanyDataItem.vue";
import JobsFormsItem from "../components/JobsFormsItem.vue";
import CreateJobFormItem from "../components/CreateJobFormItem.vue";

export default {
  name: "CompanyView",
  data() {
    return {
      companyProfile: true,
      passedSlug: this.$route.params.slug,
      jobsPage: "jobs",
    };
  },
  components: {
    Navbar,
    CompanyDataItem,
    JobsFormsItem,
    CreateJobFormItem,
  },
  watch: {
    $route(to) {
      this.passedSlug = to.params.slug;
    },
  },
};
</script>

<style></style>
