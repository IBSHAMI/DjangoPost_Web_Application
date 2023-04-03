<template>
  <section class="min-vh-100 h-100">
    <div>
      <shared-component-navbar
        :employeeProfile="employeeProfile"
        :pageType="jobsPage"
      />
    </div>
    <job-main-search @searchByJobTitle="searchByJobTitle" />
    <jobs-list
      v-if="passedSlug === 'jobs'"
      :searchTitleTerm="searchTitleTerm"
      :frameworkChoice="frameworkChoice"
    />
    <job-details v-else-if="checkIfJobDetails" :jobId="jobId" />
  </section>
</template>

<script>
import JobMainSearch from "@/components/jobComponents/JobMainSearch.vue";
import JobDetails from "@/components/JobDetails.vue";
import JobsList from "@/components/JobsList.vue";

export default {
  name: "JobsView",
  data() {
    return {
      employeeProfile: true,
      jobsPage: "jobs",
      passedSlug: this.$route.params.slug,
      searchTitleTerm: "",
      frameworkChoice: "",
    };
  },
  components: {
    JobMainSearch,
    JobDetails,
    JobsList,
  },
  computed: {
    jobId() {
      return this.passedSlug.split("-")[1];
    },
  },
  methods: {
    checkIfJobDetails() {
      return this.passedSlug.includes("jobDetails");
    },
    searchByJobTitle(searchTerm, frameworkChoice) {
      this.frameworkChoice = frameworkChoice;
      this.searchTitleTerm = searchTerm;
      this.passedSlug = "jobs";
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
