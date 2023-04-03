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
import { getAuthenticationStore } from "@/services/authService";
import { fetchData, patchDataWithToken } from "@/services/apiService";
import { API } from "@/api";

export default {
  name: "ApplicantTableRow",
  props: ["applicant"],
  data() {
    return {
      dateCreated: new Date(this.applicant.date_applied).toLocaleDateString(),
      authenticationStore: getAuthenticationStore(),
    };
  },
  methods: {
    async downloadResume() {
      const url =
        API.employee.get_applicant_resume +
        this.applicant.employee_data.pk +
        "/";

      let resumePathToDownload = "";

      const fetchResumePath = await fetchData(url);

      if (fetchResumePath) {
        resumePathToDownload = fetchResumePath.resume;
      }

      if (resumePathToDownload) {
        window.open(resumePathToDownload, "_blank");
      }
    },
    async updateApplicationStatus(updateMessage) {
      const url = API.jobs.update_application_status + this.applicant.pk + "/";

      const data = {
        update_message: updateMessage,
      };

      const patchApplicationStatus = await patchDataWithToken(
        url,
        data,
        this.authenticationStore.token
      );

      if (patchApplicationStatus) {
        this.$emit("reloadApplicantsList");
      }
    },
  },
};
</script>

<style scoped></style>
