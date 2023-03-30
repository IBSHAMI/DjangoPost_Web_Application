<template>
  <!-- component -->
  <section class="container d-flex justify-content-center py-4 my-4">
    <div class="w-100 text-center text-md-start">
      <div class="row">
        <div class="d-flex justify-content-between py-4">
          <div class="d-block mb-4 mb-md-0">
            <h2 class="h3">Jobs</h2>
            <p class="para mb-0">
              Here you can view all the jobs that is posted under your company.
            </p>
          </div>
          <div class="">
            <router-link
              :to="{ name: 'Company', params: { slug: 'create-job' } }"
              class="btn button button-primary btn-lg"
            >
              Add Job
            </router-link>
          </div>
        </div>
      </div>

      <div class="row justify-content-between align-items-center">
        <div class="col-9 col-lg-8 d-md-flex">
          <div class="form-group col-md-4 mb-3">
            <p class="form-label">Search by Name:</p>
            <input
              type="text"
              name="search-job"
              id="search-job"
              class="form-control"
              placeholder="Search Jobs"
            />
          </div>
          <div class="form-group col-md-4 mb-3 mx-3">
            <p class="form-label">Sort By:</p>
            <select
              aria-label="select"
              class="form-control"
              v-model="selectedSort"
              @change.prevent="sortJobs(selectedSort)"
            >
              <option
                class="text-sm text-indigo-800"
                v-for="option in SortByOptions"
                v-bind:key="option.id"
                :selected="option.selected"
              >
                {{ option.name }}
              </option>
            </select>
          </div>
        </div>
      </div>
      <div class="btn-group d-flex justify-content-center py-4" role="group">
        <div style="cursor: pointer" @click="changeTableVariant('all')">
          <div
            class="btn button btn-lg"
            :class="{
              'button-primary': tableVariant === 'all',
              'button-outline-primary': tableVariant !== 'all',
            }"
          >
            All
          </div>
        </div>
        <div
          style="cursor: pointer"
          @click="changeTableVariant('active')"
          class="mx-2"
        >
          <div
            class="btn button btn-lg"
            :class="{
              'button-primary': tableVariant === 'active',
              'button-outline-primary': tableVariant !== 'active',
            }"
          >
            Active
          </div>
        </div>
        <div
          style="cursor: pointer"
          @click="changeTableVariant('inactive')"
          class="mx-2"
        >
          <div
            class="btn button btn-lg"
            :class="{
              'button-primary': tableVariant === 'inactive',
              'button-outline-primary': tableVariant !== 'inactive',
            }"
          >
            Inactive
          </div>
        </div>
      </div>
      <div class="bg-white table-responsive">
        <table class="table table-hover table-nowrap">
          <thead class="table-light">
            <tr>
              <th scope="col" class="border-bottom text-left">Title</th>
              <th scope="col" class="border-bottom text-center">Type</th>
              <th scope="col" class="border-bottom text-center">Salary</th>
              <th scope="col" class="border-bottom text-center">Language</th>
              <th scope="col" class="border-bottom text-center">Created at</th>
              <th scope="col" class="border-bottom text-center">
                Active/Inactive
              </th>
              <th scope="col" class="border-bottom text-center">Applicants</th>
              <th scope="col" class="border-bottom text-center">Action</th>
            </tr>
          </thead>
          <tbody>
            <job-row-table-item
              v-for="job in jobsList"
              :key="job.pk"
              :job="job"
              @reloadJobsList="getJobsList"
            ></job-row-table-item>

            <tr class="h-3"></tr>
          </tbody>
        </table>
      </div>
      <pagination-item
        :currentPage="currentPage"
        :totalPages="totalPages"
        @navigatePages="navigator"
        @navigateNext="getJobsList(true, 'Next')"
        @navigatePrevious="getJobsList(true, 'Previous')"
      ></pagination-item>
    </div>
  </section>
</template>

<script>
import JobRowTableItem from "@/components/JobRowTableItem.vue";
import PaginationItem from "./sharedComponents/PaginationItem.vue";
import useAuthenticationStore from "@/stores/authentication";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "JobsForm",
  setup() {
    // init the store
    const authenticationStore = useAuthenticationStore();
    return { authenticationStore };
  },
  created() {
    this.getJobsList();
  },
  data() {
    return {
      jobsList: [],
      tableVariant: "all",
      selectedSort: "None",
      page: 1,
      currentPage: 1,
      totalPages: 0,
      nextPageLink: null,
      previousPageLink: null,
      SortByOptions: [
        {
          id: 1,
          name: "None",
          selected: true,
        },
        {
          id: 2,
          name: "Latest",
          selected: false,
        },
        {
          id: 3,
          name: "Oldest",
          selected: false,
        },
      ],
    };
  },
  components: {
    JobRowTableItem,
    PaginationItem,
  },
  methods: {
    // get jobs list
    getJobsList(handleNextAndPrevious, NavigateType) {
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      const params = {
        table_variant: this.tableVariant,
      };
      let jobsListUrl = API.jobs.company_list;

      if (handleNextAndPrevious) {
        if (NavigateType === "Next") {
          jobsListUrl = this.nextPageLink;
        } else if (NavigateType === "Previous") {
          jobsListUrl = this.previousPageLink;
        }
      } else {
        params.page = this.page;
      }

      axios
        .get(jobsListUrl, {
          params: params,
          headers: headers,
        })
        .then((response) => {
          console.log(response.data);
          // empty the jobs list
          this.jobsList = [];
          for (const job of response.data.results) {
            this.jobsList.push(job);
          }
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
    sortJobs(sortOption) {
      // get the selected sort option
      for (const option in this.SortByOptions) {
        if (this.SortByOptions[option].name === sortOption) {
          this.SortByOptions[option].selected = true;
          this.selectedSort = sortOption;
        } else {
          this.SortByOptions[option].selected = false;
        }
      }
      this.getJobsList();
    },
  },
};
</script>

<style></style>
