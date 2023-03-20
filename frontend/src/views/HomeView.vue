<template>
  <div>
    <Navbar :pageType="homePage" />
  </div>
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
