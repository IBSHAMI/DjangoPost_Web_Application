<template>
  <div class="cover-image sptb-1 bg-background" :style="backgroundImageStyle">
    <div class="header-text1 mb-0">
      <div class="container">
        <div class="row">
          <div class="col-xl-8 col-lg-12 col-md-12 d-block mx-auto">
            <div class="text-center text-white mx-auto">
              <h1 class="text-center form-header">
                <span class="font-weight-bold">{{ totalJobsCount }}</span>
                Jobs Available In DjangoPost
              </h1>
            </div>
            <div class="search-background py-4 text-center mx-auto">
              <div class="form row no-gutters d-flex justify-content-center">
                <div class="col-xl-4 col-lg-3 col-md-12 mb-0 form-group">
                  <input
                    type="text"
                    class="form-control input-lg border-end-0 br-tr-md-0 br-br-md-0 form-control"
                    id="text"
                    v-model="searchTerm"
                    placeholder="Search Jobs"
                  />
                </div>
                <div
                  class="col-xl-3 col-lg-3 select2-lg col-md-12 mb-0 form-group"
                >
                  <select
                    class="form-control select2-show-search border-bottom-0 w-100 select2-hidden-accessible"
                    data-placeholder="Select"
                    data-select2-id="select2-data-1-v645"
                    tabindex="-1"
                    aria-hidden="true"
                    v-model="frameworkChoice"
                  >
                    <option data-select2-id="select2-data-3-bm82">
                      All Frameworks
                    </option>
                    <option
                      v-for="(framework, index) in frameworks"
                      :value="framework"
                      :key="index"
                    >
                      {{ framework }}
                    </option>
                  </select>
                </div>
                <div
                  class="col-xl-3 col-lg-3 select2-lg col-md-12 mb-0 form-group"
                >
                  <select
                    class="form-control select2-show-search border-bottom-0 w-100 select2-hidden-accessible"
                    data-placeholder="Select"
                    data-select2-id="select2-data-1-v645"
                    tabindex="-1"
                    aria-hidden="true"
                    v-model="applyType"
                  >
                    <option data-select2-id="select2-data-3-bm82">
                      All Jobs
                    </option>
                    <option data-select2-id="select2-data-3-bm82">
                      Easy Apply
                    </option>
                  </select>
                </div>
                <div class="col-xl-2 col-lg-3 col-md-12 mb-0 form-group">
                  <a
                    @click.prevent="searchByJobTitle"
                    class="btn btn-lg btn-block btn-secondary br-bl-0 br-tl-0"
                    >Search</a
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- /header-text -->
  </div>
</template>

<script>
import SearchImg from "@/assets/img/jobs_search/job_search_bg_img.jpg";
import { fetchData } from "@/services/apiService";
import { API } from "@/api";

export default {
  name: "JobMainSearch",
  data() {
    return {
      jobSearchBG: SearchImg,
      searchTerm: "",
      frameworkChoice: "All Frameworks",
      applyType: "All Jobs",
      totalJobsCount: 0,
      frameworks: [],
    };
  },
  created() {
    this.getTotalJobsAndFrameworkChoices();
  },
  computed: {
    backgroundImageStyle() {
      return `background: url(${this.jobSearchBG}) center center; background-repeat: no-repeat; background-size: 100% 100%; background-size: cover; padding-top: 4.5rem; padding-bottom: 4.5rem;`;
    },
  },

  methods: {
    async getTotalJobsAndFrameworkChoices() {
      const Url = API.jobs.get_total_jobs;
      const totalJobs = await fetchData(Url);

      if (totalJobs) {
        this.totalJobsCount = Number(totalJobs.total_jobs);
        this.frameworks = totalJobs.framework_choices;
      }
    },
    searchByJobTitle() {
      const frameworkChosen =
        this.frameworkChoice !== "All Frameworks" ? this.frameworkChoice : "";
      const applyTypeChosen =
        this.applyType !== "All Jobs" ? this.applyType : "";
      this.$emit(
        "searchByJobTitle",
        this.searchTerm,
        frameworkChosen,
        applyTypeChosen
      );
    },
  },
};
</script>

<style scoped></style>
