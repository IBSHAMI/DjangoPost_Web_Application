<template>
  <div>
    <section class="min-vh-100 h-100">
      <Navbar :pageType="homePage" />
      <hero-section />
    </section>
  </div>
</template>

<script>
import Navbar from "@/components/sharedComponents/Navbar.vue";
import HeroSection from "@/components/landingPageComponents/HeroSection.vue";
export default {
  name: "LandingPage",
  data() {
    return {
      homePage: "home",
    };
  },
  components: {
    Navbar,
    HeroSection,
  },
};
</script>
