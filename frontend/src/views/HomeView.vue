<template>
  <div>
    <section class="min-vh-100 h-100">
      <Navbar :pageType="homePage" />
      <hero-section />
      <features-section />
      <about-section
        :totalJobs="totalJobs"
        :totalCompanies="totalCompanies"
        :totalEmployees="totalEmployees"
      />
      <footer-section />
    </section>
  </div>
</template>

<script>
import Navbar from "@/components/sharedComponents/Navbar.vue";
import HeroSection from "@/components/landingPageComponents/HeroSection.vue";
import FeaturesSection from "@/components/landingPageComponents/FeaturesSection.vue";
import AboutSection from "@/components/landingPageComponents/AboutSection.vue";
import FooterSection from "@/components/sharedComponents/FooterSection.vue";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "LandingPage",
  data() {
    return {
      homePage: "home",
      totalJobs: 0,
      totalCompanies: 0,
      totalEmployees: 0,
    };
  },
  components: {
    Navbar,
    HeroSection,
    FeaturesSection,
    AboutSection,
    FooterSection,
  },
  created() {
    this.getWebAppStatusData();
  },
  methods: {
    getWebAppStatusData() {
      const Url = API.auth.get_webapp_status_data;

      axios
        .get(Url)
        .then((response) => {
          console.log(response.data);
          this.totalJobs = response.data.total_jobs;
          this.totalCompanies = response.data.total_companies;
          this.totalEmployees = response.data.total_employees;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
