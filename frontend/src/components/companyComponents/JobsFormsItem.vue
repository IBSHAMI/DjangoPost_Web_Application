<template>
  <!-- component -->
  <section class="container d-flex justify-content-center py-4 my-4">
    <div class="w-100 text-center text-md-start">
      <div class="row pb-3">
        <div
          class="d-flex flex-column flex-md-row justify-content-center justify-content-md-between py-4"
        >
          <div class="d-block mb-3 mb-md-0">
            <h2 class="h3">Jobs</h2>
            <p class="para mb-0">
              Here you can view all the jobs that are posted under your company.
            </p>
          </div>
          <div class="d-flex align-items-center mx-auto mx-md-0">
            <div
              @click.prevent="createJob"
              class="btn button button-primary btn-lg"
            >
              Create Job
            </div>
          </div>
        </div>
      </div>

      <div class="row justify-content-between align-items-center">
        <div class="col-9 col-lg-8 d-md-flex mx-auto mx-md-0">
          <div class="form-group col-md-4 mb-3">
            <p class="form-label">Search by Name:</p>
            <input
              v-model.lazy="searchTerm"
              type="text"
              name="search-job"
              id="search-job"
              class="form-control"
              placeholder="Search Jobs"
            />
          </div>
          <div class="form-group col-md-4 mb-3 mx-md-3">
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
      <div class="table-responsive table-nowrap">
        <table class="table table-hover">
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
      <shared-component-pagination-item
        v-show="jobsList.length > 0"
        :currentPage="currentPage"
        :totalPages="totalPages"
        @navigatePages="navigator"
        @navigateNext="getJobsList(true, 'Next')"
        @navigatePrevious="getJobsList(true, 'Previous')"
      ></shared-component-pagination-item>
    </div>
  </section>
</template>

<script>
import JobRowTableItem from "@/components/companyComponents/JobRowTableItem.vue";
import { getAuthenticationStore } from "@/services/authService";
import { fetchDataWithTokenAndParams } from "@/services/apiService";
import { API } from "@/api";

export default {
  name: "JobsForm",
  async created() {
    this.authenticationStore = getAuthenticationStore();
    await this.getJobsList();
  },
  data() {
    return {
      jobsList: [],
      tableVariant: "all",
      searchTerm: "",
      selectedSort: "None",
      page: 1,
      currentPage: 1,
      totalPages: 0,
      nextPageLink: null,
      previousPageLink: null,
      authenticationStore: null,
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
  },
  watch: {
    searchTerm() {
      // search through the jobs list titles
      this.getJobsList();
    },
  },
  methods: {
    // get jobs list
    async getJobsList(handleNextAndPrevious, NavigateType) {
      let url = API.jobs.company_list;

      const params = {
        table_variant: this.tableVariant,
        search_term: this.searchTerm,
        sorting_option: this.selectedSort,
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

      const fetchJobsList = await fetchDataWithTokenAndParams(
        url,
        this.authenticationStore.token,
        params
      );

      if (fetchJobsList) {
        this.jobsList = fetchJobsList.results;
        this.currentPage = fetchJobsList.page;
        this.totalPages = fetchJobsList.total_pages;
        this.nextPageLink = fetchJobsList.links.next;
        this.previousPageLink = fetchJobsList.links.previous;
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
    createJob() {
      if (this.authenticationStore.companyProfileCompleted) {
        this.$router.push({ name: "Company", params: { slug: "create-job" } });
      } else {
        alert("Please complete your company profile first");
      }
    },
  },
};
</script>

<style></style>
