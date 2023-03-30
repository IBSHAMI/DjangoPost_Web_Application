<template>
  <div class="mt-4">
    <div class="container">
      <div class="job-tab text-center">
        <div class="btn-group d-flex justify-content-center py-4" role="group">
          <div
            style="cursor: pointer"
            @click.prevent="changeTableVariant('All Jobs')"
          >
            <div
              class="btn button btn-lg"
              :class="{
                'button-primary': tableVariant === 'All Jobs',
                'button-outline-primary': tableVariant !== 'All Jobs',
              }"
            >
              All Jobs
            </div>
          </div>
          <div
            style="cursor: pointer"
            class="mx-2"
            @click.prevent="changeTableVariant('Saved Jobs')"
          >
            <div
              class="btn button btn-lg"
              :class="{
                'button-primary': tableVariant === 'Saved Jobs',
                'button-outline-primary': tableVariant !== 'Saved Jobs',
              }"
            >
              Saved Jobs
            </div>
          </div>
          <div
            style="cursor: pointer"
            class="mx-2"
            @click.prevent="changeTableVariant('Applied Jobs')"
          >
            <div
              class="btn button btn-lg"
              :class="{
                'button-primary': tableVariant === 'Applied Jobs',
                'button-outline-primary': tableVariant !== 'Applied Jobs',
              }"
            >
              Applied Jobs
            </div>
          </div>
        </div>
        <div class="tab-content text-left">
          <div role="tabpanel" class="tab-pane fade active show" id="hot-jobs">
            <div class="row">
              <job-card v-for="job in jobsList" :job="job" :key="job.pk" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import JobCard from "@/components/jobComponents/JobCard.vue";
import useAuthenticationStore from "@/stores/authentication";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "JobsList",
  setup() {
    // init the store
    const authenticationStore = useAuthenticationStore();
    return { authenticationStore };
  },
  components: {
    JobCard,
  },
  created() {
    this.getJobsList();
  },
  data() {
    return {
      jobsList: [],
      tableVariant: "All Jobs",
    };
  },
  methods: {
    getJobsList() {
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        "content-type": "application/json",
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      const params = {
        table_variant: this.tableVariant,
      };

      const url = API.jobs.list;

      axios
        .get(url, {
          params: params,
          headers: headers,
        })
        .then((response) => {
          console.log(response.data);
          this.jobsList = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    changeTableVariant(variant) {
      this.tableVariant = variant;
      this.getJobsList();
    },
  },
};
</script>

<style scoped>
/* Tr Job Post */
</style>
