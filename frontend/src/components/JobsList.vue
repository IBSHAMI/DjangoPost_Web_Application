<template>
  <div class="mt-4">
    <div class="container">
      <div class="row job-tab text-center my-4 py-4">
        <div
          class="btn-group d-flex justify-content-center py-4"
          role="group"
          v-show="authenticationStore.isAuthenticated"
        >
          <div
            style="cursor: pointer"
            @click.prevent="changeTableVariant('All Jobs')"
            v-show="authenticationStore.isAuthenticated"
          >
            <div
              class="btn button btn-lg"
              :class="{
                'button-primary': tableVariant === 'All Jobs',
                'button-outline-primary': tableVariant !== 'All Jobs',
              }"
            >
              All Jobs
            </div>
          </div>
          <div
            style="cursor: pointer"
            class="mx-2"
            @click.prevent="changeTableVariant('Saved Jobs')"
            v-show="authenticationStore.isAuthenticated"
          >
            <div
              class="btn button btn-lg"
              :class="{
                'button-primary': tableVariant === 'Saved Jobs',
                'button-outline-primary': tableVariant !== 'Saved Jobs',
              }"
            >
              Saved Jobs
            </div>
          </div>
          <div
            style="cursor: pointer"
            class="mx-2"
            @click.prevent="changeTableVariant('Applied Jobs')"
            v-show="authenticationStore.isAuthenticated"
          >
            <div
              class="btn button btn-lg"
              :class="{
                'button-primary': tableVariant === 'Applied Jobs',
                'button-outline-primary': tableVariant !== 'Applied Jobs',
              }"
            >
              Applied Jobs
            </div>
          </div>
        </div>
        <div class="row tab-content text-left">
          <div role="tabpanel" class="tab-pane fade active show" id="hot-jobs">
            <div class="row">
              <job-card
                v-for="job in jobsList"
                :job="job"
                :tableVariant="tableVariant"
                :key="job.pk"
              />
            </div>
          </div>
        </div>
      </div>
      <shared-component-pagination-item
        v-show="jobsList.length > 0"
        :currentPage="currentPage"
        :totalPages="totalPages"
        @navigatePages="navigator"
        @navigateNext="getJobsList(true, 'Next')"
        @navigatePrevious="getJobsList(true, 'Previous')"
      />
    </div>
  </div>
</template>

<script>
import JobCard from "@/components/jobComponents/JobCard.vue";
import { getAuthenticationStore } from "@/services/authService";
import { fetchDataWithParams } from "@/services/apiService";
import { API } from "@/api";

export default {
  name: "JobsList",
  props: ["searchTitleTerm", "frameworkChoice"],
  components: {
    JobCard,
  },
  created() {
    this.authenticationStore = getAuthenticationStore();
    this.getJobsList();
  },
  data() {
    return {
      jobsList: [],
      tableVariant: "All Jobs",
      page: 1,
      currentPage: 1,
      totalPages: 0,
      nextPageLink: null,
      previousPageLink: null,
      authenticationStore: null,
    };
  },
  methods: {
    async getJobsList(handleNextAndPrevious, NavigateType) {
      let url = API.jobs.list;

      const params = {
        table_variant: this.tableVariant,
        search_term: this.searchTitleTerm,
        framework_choice: this.frameworkChoice,
      };
      if (handleNextAndPrevious) {
        if (NavigateType === "Next") {
          url = this.nextPageLink;
        } else if (NavigateType === "Previous") {
          url = this.previousPageLink;
        }
      } else {
        params.page = this.page;
      }

      const getJobsList = await fetchDataWithParams(url, params);

      if (getJobsList) {
        this.jobsList = getJobsList.results;
        this.currentPage = getJobsList.page;
        this.totalPages = getJobsList.total_pages;
        this.nextPageLink = getJobsList.links.next;
        this.previousPageLink = getJobsList.links.previous;
      }
    },
    changeTableVariant(variant) {
      if (this.tableVariant === variant) {
        return;
      }
      this.tableVariant = variant;
      this.page = 1;
      this.getJobsList();
    },
    navigator(page) {
      console.log(page);
      this.page = page;
      this.getJobsList();
    },
  },
  watch: {
    searchTitleTerm() {
      this.getJobsList();
    },
    frameworkChoice() {
      this.getJobsList();
    },
  },
};
</script>
