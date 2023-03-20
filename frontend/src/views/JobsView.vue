<template>
  <div>
    <Navbar :employeeProfile="employeeProfile" :pageType="jobsPage" />
  </div>
</template>

<script>
import Navbar from "../components/sharedComponents/Navbar.vue";

export default {
  name: "JobsView",
  data() {
    return {
      employeeProfile: true,
      jobsPage: "jobs",
    };
  },
  components: {
    Navbar,
  },
};
</script>

<style></style>
