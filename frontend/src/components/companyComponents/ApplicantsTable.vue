<template>
  <!-- component -->
  <section class="container d-flex justify-content-center py-4 my-4">
    <div class="w-100 text-center text-md-start">
      <div class="row">
        <div class="d-flex justify-content-between py-4">
          <div class="d-block mb-4 mb-md-0">
            <h2 class="h3">{{ jobTitle }}</h2>
            <p class="para mb-0">
              Here you can view all the applicants that applied for this job.
            </p>
          </div>
        </div>
      </div>

      <div class="row justify-content-between align-items-center">
        <div class="col-9 col-lg-8 d-md-flex">
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
      <div class="table-responsive my-4">
        <table class="table table-hover table-nowrap">
          <thead class="table-light">
            <tr>
              <th scope="col" class="border-bottom text-left">Name</th>
              <th scope="col" class="border-bottom text-center">
                Applicantion Date
              </th>
              <th scope="col" class="border-bottom text-center">Email</th>
              <th scope="col" class="border-bottom text-center">Experience</th>
              <th scope="col" class="border-bottom text-center">Socials</th>
              <th scope="col" class="border-bottom text-center">
                Expected Salary
              </th>
              <th scope="col" class="border-bottom text-center">Action</th>
            </tr>
          </thead>
          <tbody>
            <applicant-table-row
              v-for="applicant in applicantList"
              :key="applicant.pk"
              :applicant="applicant"
              @reloadApplicantsList="getApplicantsList"
            />

            <tr class="h-3"></tr>
          </tbody>
        </table>
      </div>
      <pagination-item
        v-show="applicantList.length > 0"
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
import ApplicantTableRow from "@/components/companyComponents/ApplicantTableRow.vue";
import PaginationItem from "@/components/sharedComponents/PaginationItem.vue";
import { getAuthenticationStore } from "@/services/authService";
import { fetchDataWithTokenAndParams } from "@/services/apiService";
import { API } from "@/api";

export default {
  name: "ApplicantsTable",
  props: ["jobId"],
  created() {
    this.authenticationStore = getAuthenticationStore();
    this.getApplicantsList();
    this.getJobTitle();
  },
  data() {
    return {
      jobTitle: "",
      applicantList: [],
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
    ApplicantTableRow,
    PaginationItem,
  },
  watch: {
    searchTerm() {
      // search through the jobs list titles
      this.getApplicantsList();
    },
  },
  methods: {
    async getJobTitle() {
      const url = API.jobs.get_job_title;
      const params = {
        job_id: this.jobId,
      };
      const fetchJobTile = await fetchDataWithTokenAndParams(
        url,
        this.authenticationStore.token,
        params
      );

      if (fetchJobTile) {
        this.jobTitle = fetchJobTile.job_title;
      }
    },
    async getApplicantsList(handleNextAndPrevious, NavigateType) {
      let url = API.jobs.applicants_list;

      const params = {
        search_term: this.searchTerm,
        sorting_option: this.selectedSort,
        job_id: this.jobId,
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

      const fetchApplicatsList = await fetchDataWithTokenAndParams(
        url,
        this.authenticationStore.token,
        params
      );

      if (fetchApplicatsList) {
        this.applicantList = [];
        for (const applicantInformation of fetchApplicatsList.results) {
          this.applicantList.push(applicantInformation);
        }
        this.currentPage = fetchApplicatsList.page;
        this.totalPages = fetchApplicatsList.total_pages;
        this.nextPageLink = fetchApplicatsList.links.next;
        this.previousPageLink = fetchApplicatsList.links.previous;
      }
    },
    navigator(page) {
      console.log(page);
      this.page = page;
      this.getApplicantsList();
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
      this.getApplicantsList();
    },
  },
};
</script>

<style></style>
