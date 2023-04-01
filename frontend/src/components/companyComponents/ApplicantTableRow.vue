<template>
  <tr>
    <td class="fw-normal text-left">
      <span class="fw-normal">{{
        applicant.employee_data.first_name +
        " " +
        applicant.employee_data.last_name
      }}</span>
    </td>
    <td class="fw-normal text-center">
      {{ dateCreated }}
    </td>
    <td class="fw-normal text-center">
      {{ applicant.employee_data.email }}
    </td>
    <td class="fw-normal text-center">
      {{ applicant.employee_data.experience }}
    </td>
    <td class="fw-normal text-center">
      <span class="fw-normal" style="cursor: pointer"
        ><a
          class="link-info"
          :href="applicant.employee_data.linkedin_url"
          target="_blank"
          >Linkedin</a
        ></span
      >
      |
      <span class="fw-normal" style="cursor: pointer"
        ><a
          class="link-info"
          :href="applicant.employee_data.portfolio_url"
          target="_blank"
          >Protofolio</a
        ></span
      >
    </td>
    <td class="fw-normal text-center">
      {{ applicant.employee_data.expected_salary }}
    </td>
    <td class="fw-normal text-center">
      <span
        class="fw-normal link-primary"
        style="cursor: pointer"
        @click.prevent="downloadResume"
        >Download Resume</span
      >
      |
      <span
        class="fw-normal text-danger"
        style="cursor: pointer"
        @click.prevent="updateApplicationStatus('rejected')"
        >Reject</span
      >
    </td>
  </tr>
</template>

<script>
import useAuthenticationStore from "@/stores/authentication";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "ApplicantTableRow",
  props: ["applicant"],
  setup() {
    const authenticationStore = useAuthenticationStore();
    return {
      authenticationStore,
    };
  },
  data() {
    return {
      dateCreated: new Date(this.applicant.date_applied).toLocaleDateString(),
    };
  },
  methods: {
    downloadResume() {
      console.log("download resume");

      const applicantResumeUrl =
        API.employee.get_applicant_resume +
        this.applicant.employee_data.pk +
        "/";

      console.log(applicantResumeUrl);

      let resumePathToDownload = "";

      // get the resume path to download
      axios
        .get(applicantResumeUrl)
        .then((response) => {
          console.log(response.data);
          resumePathToDownload = response.data.resume;
          if (resumePathToDownload) {
            // download the file
            window.open(resumePathToDownload, "_blank");
          }
          this.updateApplicationStatus("resume downloaded");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    updateApplicationStatus(updateMessage) {
      console.log("update application");

      const applicantDeleteUrl =
        API.jobs.update_application_status + this.applicant.pk + "/";

      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      const data = {
        update_message: updateMessage,
      };

      // update the application
      axios
        .patch(applicantDeleteUrl, data, { headers: headers })
        .then((response) => {
          console.log(response.data);
          this.$emit("reloadApplicantsList");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped></style>
