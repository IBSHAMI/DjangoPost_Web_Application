<template>
  <tr>
    <td class="fw-normal text-left">
      <span
        class="fw-normal text-primary"
        style="cursor: pointer"
        @click.prevent="openJobDetails"
        >{{ job.title }}</span
      >
    </td>
    <td class="fw-normal text-center">
      {{ job.type }}
    </td>
    <td class="fw-normal text-center">
      {{ job.salary }}
    </td>
    <td class="fw-normal text-center">
      {{ job.language }}
    </td>
    <td class="fw-normal text-center">
      {{ dateCreated }}
    </td>
    <td
      class="fw-normal text-center font-weight-bold"
      :class="job.is_active ? 'text-success' : 'text-danger'"
    >
      {{ job.is_active ? "Active" : "Inactive" }}
    </td>
    <td class="fw-normal text-center">
      <span
        class="fw-normal text-primary"
        style="cursor: pointer"
        @click.prevent="openApplicantsTable"
        >{{ job.number_of_applications }}</span
      >
    </td>
    <td class="fw-normal text-center">
      <span
        class="fw-normal"
        :class="job.is_active ? 'text-danger' : 'text-success'"
        style="cursor: pointer"
        @click.prevent="ChangeJobStatus"
        >{{ job.is_active ? "Deactive Job" : "Active Job" }}</span
      >
      |
      <span
        class="fw-normal text-danger"
        style="cursor: pointer"
        @click.prevent="deleteJob"
        >Delete</span
      >
    </td>
  </tr>
</template>

<script>
import { getAuthenticationStore } from "@/services/authService";
import { fetchDataWithToken, deleteDataWithToken } from "@/services/apiService";
import { API } from "@/api";

export default {
  name: "JobRowTableItem",
  props: ["job"],
  data() {
    return {
      jobDropdown: false,
      dateCreated: new Date(this.job.date_created).toLocaleDateString(),
      authenticationStore: getAuthenticationStore(),
    };
  },
  methods: {
    async ChangeJobStatus() {
      const url = API.jobs.change_job_status + this.job.pk + "/";
      const changeJobStatus = await fetchDataWithToken(
        url,
        this.authenticationStore.token
      );

      if (changeJobStatus.status === 200) {
        this.$emit("reloadJobsList");
      }
    },
    async deleteJob() {
      const url = API.jobs.delete_job + this.job.pk + "/";
      const deleteJobStatus = await deleteDataWithToken(
        url,
        this.authenticationStore.token
      );

      if (deleteJobStatus === 204) {
        this.$emit("reloadJobsList");
      }
    },
    openJobDetails() {
      // make the details page open in a new tab
      const url = this.$router.resolve({
        name: "Jobs",
        params: { slug: `jobDetails-${this.job.pk}` },
      }).href;
      window.open(url, "_blank");
    },
    openApplicantsTable() {
      this.$router.push({
        name: "Company",
        params: { slug: `ApplicantsTable-${this.job.pk}` },
      });
    },
  },
};
</script>

<style scoped>
.custom-switch .custom-control-label {
  left: -4.25rem;
  width: 2.5rem;
  pointer-events: all;
  border: 0;
  border-radius: 0.625rem;
  box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #fff;
}
</style>
