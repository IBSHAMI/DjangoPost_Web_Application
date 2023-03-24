<template>
  <section class="min-vh-100 h-100">
    <div>
      <Navbar :employeeProfile="employeeProfile" :pageType="jobsPage" />
    </div>
    <job-main-search />
    <jobs-list v-if="passedSlug === 'jobs'" />
    <job-details v-else-if="checkIfJobDetails" :jobId="jobId" />
  </section>
</template>

<script>
import Navbar from "@/components/sharedComponents/Navbar.vue";
import JobMainSearch from "@/components/jobComponents/JobMainSearch.vue";
import JobDetails from "@/components/JobDetails.vue";
import JobsList from "@/components/jobComponents/JobsList.vue";

export default {
  name: "JobsView",
  data() {
    return {
      employeeProfile: true,
      jobsPage: "jobs",
      passedSlug: this.$route.params.slug,
    };
  },
  components: {
    Navbar,
    JobMainSearch,
    JobDetails,
    JobsList,
  },
  computed: {
    jobId() {
      console.log(this.passedSlug);
      return this.passedSlug.split("-")[1];
    },
  },
  methods: {
    checkIfJobDetails() {
      return this.passedSlug.includes("jobDetails");
    },
  },
};
</script>

<style></style>
