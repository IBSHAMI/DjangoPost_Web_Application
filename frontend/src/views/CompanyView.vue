<template>
  <div>
    <Navbar
      class="pb-8"
      :companyProfile="companyProfile"
      :pageType="jobsPage"
    />
    <hr />
    <company-data v-if="passedSlug === 'data'" />
    <jobs-forms-item v-else-if="passedSlug === 'jobs'" />
    <create-job-form-item v-else-if="passedSlug === 'create-job'" />
  </div>
</template>

<script>
import Navbar from "../components/sharedComponents/Navbar.vue";
import CompanyData from "../components/CompanyData.vue";
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
    CompanyData,
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
