<template>
  <div class="container py-4 my-4">
    <div class="row">
      <div class="row pb-3">
        <div class="container-fluid">
          <div class="row">
            <div class="col-xl-8 mx-auto">
              <div class="card overflow-hidden">
                <job-details-header
                  :headerData="getJobHeaderData"
                  :isApplied="isApplied"
                  @applied="applied"
                />
                <job-details-body :bodyData="getJobBodyData" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getAuthenticationStore } from "@/services/authService";
import JobDetailsHeader from "@/components/jobComponents/JobDetailsHeader.vue";
import JobDetailsBody from "@/components/jobComponents/JobDetailsBody.vue";
import { fetchData, fetchDataWithToken } from "@/services/apiService";
import { API } from "@/api";

export default {
  name: "JobDetails",
  props: ["jobId"],
  created() {
    this.authenticationStore = getAuthenticationStore();
    this.getJobDetails();
  },
  data() {
    return {
      // job details
      pk: "",
      title: "",
      description: "",
      location: "",
      type: "",
      framework: "",
      language: "",
      experience: "",
      numberOfPositions: "",
      dateCreated: "",
      remote: "",
      salary: "",
      internal: "",
      jobLink: "",
      isApplied: "",
      // company details
      companyData: {},

      // authentication store
      authenticationStore: null,
    };
  },
  components: {
    JobDetailsHeader,
    JobDetailsBody,
  },
  methods: {
    async getJobDetails() {
      const url = API.jobs.detail + Number(this.jobId) + "/";
      let jobDetails;

      if (this.authenticationStore.isAuthenticated) {
        const token = this.authenticationStore.token;
        jobDetails = await fetchDataWithToken(url, token);
      } else {
        jobDetails = await fetchData(url);
      }
      if (jobDetails) {
        console.log(jobDetails);
        this.pk = jobDetails.pk;
        this.title = jobDetails.title;
        this.description = jobDetails.description;
        this.location = jobDetails.location;
        this.type = jobDetails.type;
        this.framework = jobDetails.framework;
        this.language = jobDetails.language;
        this.experience = jobDetails.experience;
        this.numberOfPositions = jobDetails.number_of_positions;
        this.dateCreated = jobDetails.date_created;
        this.remote = jobDetails.remote;
        this.salary = jobDetails.salary;
        this.internal = jobDetails.internal;
        this.jobLink = jobDetails.job_link;
        this.isApplied = jobDetails.is_applied;
        this.companyData = jobDetails.company_data;
      }
    },
    applied() {
      this.isApplied = true;
    },
  },
  computed: {
    getJobHeaderData() {
      return {
        pk: this.pk,
        title: this.title,
        type: this.type,
        framework: this.framework,
        dateCreated: this.dateCreated,
        internal: this.internal,
        jobLink: this.jobLink,
      };
    },
    getJobBodyData() {
      return {
        description: this.description,
        type: this.type,
        dateCreated: this.dateCreated,
        location: this.location,
        language: this.language,
        experience: this.experience,
        numberOfPositions: this.numberOfPositions,
        remote: this.remote,
        salary: this.salary,
        internal: this.internal,
        companyName: this.companyData.company_name,
      };
    },
  },
};
</script>

<style scoped></style>
