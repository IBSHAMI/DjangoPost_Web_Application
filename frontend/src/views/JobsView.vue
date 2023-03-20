<template>
  <section>
    <Navbar :employeeProfile="employeeProfile" :pageType="jobsPage" />
  </section>
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
