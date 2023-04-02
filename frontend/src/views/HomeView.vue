<template>
  <div>
    <section class="min-vh-100 h-100">
      <shared-component-navbar :pageType="homePage" />
      <hero-section />
      <features-section />
      <about-section
        :totalJobs="totalJobs"
        :totalCompanies="totalCompanies"
        :totalEmployees="totalEmployees"
      />
      <shared-component-footer-section />
    </section>
  </div>
</template>

<script>
import HeroSection from "@/components/landingPageComponents/HeroSection.vue";
import FeaturesSection from "@/components/landingPageComponents/FeaturesSection.vue";
import AboutSection from "@/components/landingPageComponents/AboutSection.vue";
import { fetchData } from "@/services/apiService";
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
    HeroSection,
    FeaturesSection,
    AboutSection,
  },
  created() {
    this.getWebAppStatusData();
  },
  methods: {
    async getWebAppStatusData() {
      const Url = API.auth.get_webapp_status_data;
      const webAppStatusData = await fetchData(Url);

      if (webAppStatusData) {
        this.totalJobs = Number(webAppStatusData.total_jobs);
        this.totalCompanies = Number(webAppStatusData.total_companies);
        this.totalEmployees = Number(webAppStatusData.total_employees);
      }
    },
  },
};
</script>
