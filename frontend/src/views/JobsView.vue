<template>
  <section class="min-vh-100 h-100">
    <div>
      <Navbar :employeeProfile="employeeProfile" :pageType="jobsPage" />
    </div>
    <jobs-list v-if="passedSlug === 'jobs'" />
    <job-details v-else-if="passedSlug === 'jobDetails'" />
  </section>
</template>

<script>
import Navbar from "@/components/sharedComponents/Navbar.vue";
import JobDetails from "@/components/jobComponents/JobDetails.vue";
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
    JobDetails,
    JobsList,
  },
};
</script>

<style></style>
