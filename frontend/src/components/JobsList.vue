<template>
  <div class="mt-4">
    <div class="container">
      <div class="row job-tab text-center my-4 py-4">
        <div class="btn-group d-flex justify-content-center py-4" role="group">
          <div
            style="cursor: pointer"
            @click.prevent="changeTableVariant('All Jobs')"
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
              <job-card v-for="job in jobsList" :job="job" :key="job.pk" />
            </div>
          </div>
        </div>
      </div>
      <pagination-item
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
import PaginationItem from "./sharedComponents/PaginationItem.vue";
import useAuthenticationStore from "@/stores/authentication";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "JobsList",
  setup() {
    // init the store
    const authenticationStore = useAuthenticationStore();
    return { authenticationStore };
  },
  components: {
    JobCard,
    PaginationItem,
  },
  created() {
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
    };
  },
  methods: {
    getJobsList(handleNextAndPrevious, NavigateType) {
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        "content-type": "application/json",
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      let url = API.jobs.list;

      const params = {
        table_variant: this.tableVariant,
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

      axios
        .get(url, {
          params: params,
          headers: headers,
        })
        .then((response) => {
          console.log(response.data);
          this.jobsList = response.data.results;
          this.currentPage = response.data.page;
          this.totalPages = response.data.total_pages;
          this.nextPageLink = response.data.links.next;
          this.previousPageLink = response.data.links.previous;
        })
        .catch((error) => {
          console.log(error);
        });
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
};
</script>
