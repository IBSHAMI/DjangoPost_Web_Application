<template>
  <div
    class="cover-image sptb-1 bg-background"
    data-image-src="../src/assets/img/jobs_search/job_search_bg_img.jpg"
    style="
      background: url('../src/assets/img/jobs_search/job_search_bg_img.jpg')
        center center;
      background-repeat: no-repeat;
      background-size: 100% 100%;
      background-size: cover;
      padding-top: 4.5rem;
      padding-bottom: 4.5rem;
    "
  >
    <div class="header-text1 mb-0">
      <div class="container">
        <div class="row">
          <div class="col-xl-8 col-lg-12 col-md-12 d-block mx-auto">
            <div class="text-center text-white">
              <h1 class="text-center form-header">
                <span class="font-weight-bold">{{ totalJobsCount }}</span>
                Jobs Available In DjangoPost
              </h1>
            </div>
            <div class="search-background py-4 text-center mx-auto">
              <div class="form row no-gutters">
                <div class="col-xl-6 col-lg-5 col-md-12 mb-0 form-group">
                  <input
                    type="text"
                    class="form-control input-lg border-end-0 br-tr-md-0 br-br-md-0 form-control"
                    id="text"
                    v-model="searchTerm"
                    placeholder="Search Jobs"
                  />
                </div>
                <!-- <div
                  class="col-xl-4 col-lg-4 select2-lg col-md-12 mb-0 form-group"
                >
                  <select
                    class="form-control select2-show-search border-bottom-0 w-100 select2-hidden-accessible"
                    data-placeholder="Select"
                    data-select2-id="select2-data-1-v645"
                    tabindex="-1"
                    aria-hidden="true"
                  >
                    <optgroup label="Categories">
                      <option data-select2-id="select2-data-3-bm82">
                        All Categories
                      </option>
                      <option value="1">Accountant</option>
                      <option value="2">IT Software</option>
                      <option value="3">Banking</option>
                      <option value="4">Finaces</option>
                      <option value="5">Cook/Chef</option>
                      <option value="6">Driveing</option>
                      <option value="7">HR Recruiter</option>
                      <option value="8">IT Hardware</option>
                      <option value="9">Sales</option>
                    </optgroup>
                  </select>
                </div> -->
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
import axios from "axios";
import { API } from "@/api";

export default {
  name: "JobMainSearch",
  data() {
    return {
      searchTerm: "",
      totalJobsCount: 0,
    };
  },
  created() {
    this.get_total_jobs_count();
  },
  methods: {
    get_total_jobs_count() {
      const Url = API.jobs.get_total_jobs;

      axios
        .get(Url)
        .then((response) => {
          console.log(response.data);
          this.totalJobsCount = Number(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    searchByJobTitle() {
      this.$emit("searchByJobTitle", this.searchTerm);
    },
  },
};
</script>

<style scoped></style>
