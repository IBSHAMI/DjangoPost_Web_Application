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
import axios from "axios";
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
    getJobDetails() {
      const jobDetailsUrl = API.jobs.detail + Number(this.jobId) + "/";

      let headers = {};
      if (this.authenticationStore.isAuthenticated) {
        const token = `Bearer ${this.authenticationStore.token}`;
        // Add the token to the header as Bearer token
        headers = {
          // eslint-disable-next-line prettier/prettier
          Authorization: token,
        };
      }

      axios
        .get(jobDetailsUrl, { headers })
        .then((response) => {
          console.log(response.data);
          this.pk = response.data.pk;
          this.title = response.data.title;
          this.description = response.data.description;
          this.location = response.data.location;
          this.type = response.data.type;
          this.framework = response.data.framework;
          this.language = response.data.language;
          this.experience = response.data.experience;
          this.numberOfPositions = response.data.number_of_positions;
          this.dateCreated = response.data.date_created;
          this.remote = response.data.remote;
          this.salary = response.data.salary;
          this.internal = response.data.internal;
          this.jobLink = response.data.job_link;
          this.isApplied = response.data.is_applied;
          this.companyData = response.data.company_data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    applied() {
      console.log("applied");
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
