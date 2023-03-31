<template>
  <section class="min-vh-100 h-100">
    <div>
      <Navbar
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
import Navbar from "@/components/sharedComponents/Navbar.vue";
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
    Navbar,
    CompanyData,
    JobsFormsItem,
    CreateJobFormItem,
    ApplicantsTable,
  },
  computed: {
    jobId() {
      console.log(this.passedSlug);
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
