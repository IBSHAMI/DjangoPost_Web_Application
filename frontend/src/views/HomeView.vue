<template>
  <section class="min-vh-100 h-100">
    <Navbar :pageType="homePage" />
  </section>
</template>

<script>
import Navbar from "../components/sharedComponents/Navbar.vue";
export default {
  name: "landing-page",
  data() {
    return {
      homePage: "home",
    };
  },
  components: {
    Navbar,
  },
};
</script>
