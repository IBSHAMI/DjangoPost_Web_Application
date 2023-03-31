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
      <span class="fw-normal text-primary" style="cursor: pointer">{{
        job.number_of_applications
      }}</span>
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
import useAuthenticationStore from "@/stores/authentication";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "JobRowTableItem",
  props: ["job"],
  data() {
    return {
      jobDropdown: false,
      dateCreated: new Date(this.job.date_created).toLocaleDateString(),
    };
  },
  setup() {
    const authenticationStore = useAuthenticationStore();
    return {
      authenticationStore,
    };
  },
  methods: {
    ChangeJobStatus() {
      const changeJobStatusUrl = API.jobs.change_job_status + this.job.pk + "/";

      const token = `Bearer ${this.authenticationStore.token}`;
      console.log(token);
      // Add the token to the header as Bearer token
      const headers = {
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      axios
        .get(changeJobStatusUrl, { headers: headers })
        .then((response) => {
          console.log(response);
          this.$emit("reloadJobsList");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    deleteJob() {
      const deleteJobUrl = API.jobs.delete_job + this.job.pk + "/";

      const token = `Bearer ${this.authenticationStore.token}`;
      console.log(token);
      // Add the token to the header as Bearer token
      const headers = {
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      axios
        .delete(deleteJobUrl, { headers: headers })
        .then((response) => {
          console.log(response);
          this.$emit("reloadJobsList");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    openJobDetails() {
      // make the details page open in a new tab
      const url = this.$router.resolve({
        name: "Jobs",
        params: { slug: `jobDetails-${this.job.pk}` },
      }).href;
      window.open(url, "_blank");
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
