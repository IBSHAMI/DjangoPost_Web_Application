<template>
  <tr>
    <td class="fw-normal text-center">
      {{ job.title }}
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
        class="fw-normal text-info"
        data-bs-toggle="modal"
        data-bs-target="#modalNotification"
        style="cursor: pointer"
      >
        View
      </span>

      <!-- Modal Content -->
      <div
        class="modal fade"
        id="modalNotification"
        tabindex="-1"
        role="dialog"
        aria-labelledby="modalTitleNotify"
        aria-hidden="true"
      >
        <div class="modal-dialog modal-dialog-centered" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <p class="modal-title" id="modalTitleNotify">
                Welcome to StudentDiary Nov. 26, 2022, 12:17 p.m..
              </p>
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div class="modal-body">
              <div class="py-3 text-center">
                <svg
                  class="icon icon-xl text-primary"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"
                  ></path>
                </svg>
                <h2 class="h4 modal-title my-3">Product Added!</h2>
                <p class="text-justify">
                  Welcome to StudentDiary, We are pleased you decided to join
                  us. We hope you enjoy our services.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- End of Modal Content -->
    </td>
    <td class="fw-normal text-center">
      <span
        class="fw-normal text-danger"
        :class="job.is_active ? 'text-success' : 'text-danger'"
        style="cursor: pointer"
        @click.prevent="ChangeJobStatus"
        >{{ job.is_active ? "Deactive Job" : "Active Job" }}</span
      >
      |
      <span class="fw-normal text-danger" style="cursor: pointer">Delete</span>
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
