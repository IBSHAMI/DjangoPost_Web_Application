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
    getJobsList() {
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        "content-type": "application/json",
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      const params = {
        table_variant: this.tableVariant,
        page: this.page,
      };

      const url = API.jobs.list;

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
        })
        .catch((error) => {
          console.log(error);
        });
    },
    changeTableVariant(variant) {
      this.tableVariant = variant;
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
