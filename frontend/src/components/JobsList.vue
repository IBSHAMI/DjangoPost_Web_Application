<template>
  <div class="mt-4">
    <div class="container">
      <div class="job-tab text-center">
        <div class="btn-group d-flex justify-content-center py-4" role="group">
          <div style="cursor: pointer">
            <div class="btn button btn-lg button-primary">Hot Jobs</div>
          </div>
          <div style="cursor: pointer" class="mx-2">
            <div class="btn button button-outline-primary btn-lg">
              Recent Jobs
            </div>
          </div>
          <div style="cursor: pointer" class="mx-2">
            <div class="btn button button-outline-primary btn-lg">
              Popular Jobs
            </div>
          </div>
        </div>
        <div class="tab-content text-left">
          <div role="tabpanel" class="tab-pane fade active show" id="hot-jobs">
            <div class="row">
              <job-card v-for="job in jobsList" :job="job" :key="job.pk" />
            </div>
            <!-- /.row -->
          </div>
          <!-- /.tab-pane -->
        </div>
      </div>
      <!-- /.job-tab -->
    </div>
    <!-- /.container -->
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
      tableVariant: "active",
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

      const url = API.jobs.list;

      axios
        .get(url, { headers })
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
    },
  },
};
</script>

<style scoped>
/* Tr Job Post */
</style>
