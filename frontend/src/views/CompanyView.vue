<template>
  <section class="min-vh-100 h-100">
    <div>
      <shared-component-navbar
        class="pb-8"
        :companyProfile="companyProfile"
        :pageType="jobsPage"
      />
    </div>
    <company-data v-if="passedSlug === 'data'" />
    <jobs-forms-item v-else-if="passedSlug === 'jobs'" />
    <create-job-form-item v-else-if="passedSlug === 'create-job'" />
    <applicants-table v-else-if="checkIfApplicantsTable" :jobId="jobId" />
  </section>
</template>

<script>
import CompanyData from "@/components/CompanyData.vue";
import JobsFormsItem from "@/components/companyComponents/JobsFormsItem.vue";
import CreateJobFormItem from "@/components/companyComponents/CreateJobFormItem.vue";
import ApplicantsTable from "@/components/companyComponents/ApplicantsTable.vue";

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
    CompanyData,
    JobsFormsItem,
    CreateJobFormItem,
    ApplicantsTable,
  },
  computed: {
    jobId() {
      return this.passedSlug.split("-")[1];
    },
  },
  methods: {
    checkIfApplicantsTable() {
      return this.passedSlug.includes("ApplicantsTable");
    },
  },
  watch: {
    $route(to) {
      this.passedSlug = to.params.slug;
    },
  },
};
</script>

<style></style>
