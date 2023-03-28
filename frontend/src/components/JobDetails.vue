<template>
  <div class="container py-4 my-4">
    <div class="row">
      <div class="row pb-3">
        <div class="container-fluid">
          <div class="row">
            <div class="col-xl-8 order-xl-1">
              <div class="card overflow-hidden">
                <job-details-header :headerData="getJobHeaderData" />
                <job-details-body :bodyData="getJobBodyData" />
              </div>
            </div>
            <company-card
              :company="companyData"
              :companyLogoPath="this.authenticationStore.companyProfileLogo"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import useAuthenticationStore from "@/stores/authentication";
import CompanyCard from "@/components/companyComponents/CompanyCard.vue";
import JobDetailsHeader from "@/components/jobComponents/JobDetailsHeader.vue";
import JobDetailsBody from "@/components/jobComponents/JobDetailsBody.vue";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "JobDetails",
  props: ["jobId"],
  setup() {
    // init the store
    const authenticationStore = useAuthenticationStore();
    return { authenticationStore };
  },
  created() {
    this.getJobDetails();
  },
  data() {
    return {
      // job details
      title: "",
      description: "",
      location: "",
      type: "",
      language: "",
      experience: "",
      numberOfPositions: "",
      dateCreated: "",
      remote: "",
      salary: "",
      internal: "",
      // company details
      companyData: {},
    };
  },
  components: {
    JobDetailsHeader,
    JobDetailsBody,
    CompanyCard,
  },
  methods: {
    getJobDetails() {
      console.log(typeof Number(this.jobId));
      const jobDetailsUrl = API.jobs.detail + Number(this.jobId) + "/";
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        "content-type": "application/json",
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      axios
        .get(jobDetailsUrl, { headers })
        .then((response) => {
          console.log(response.data);
          this.title = response.data.title;
          this.description = response.data.description;
          this.location = response.data.location;
          this.type = response.data.type;
          this.language = response.data.language;
          this.experience = response.data.experience;
          this.numberOfPositions = response.data.number_of_positions;
          this.dateCreated = response.data.date_created;
          this.remote = response.data.remote;
          this.salary = response.data.salary;
          this.internal = response.data.internal;
          this.companyData = response.data.company_data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  computed: {
    getJobHeaderData() {
      return {
        title: this.title,
        type: this.type,
        dateCreated: this.dateCreated,
        internal: this.internal,
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
