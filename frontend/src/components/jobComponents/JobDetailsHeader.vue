<template>
  <div class="card-body h-100">
    <div class="row">
      <div class="row mt-10">
        <div class="col-lg-8 col-md-12">
          <h3 class="job-title">
            {{ headerData.title }}
          </h3>
          <div class="mt-0 mb-15">
            <span class="form-label fst-italic card-briefcase mx-2">{{
              headerData.type
            }}</span>
            <span class="form-label fst-italic card-framework">{{
              headerData.framework
            }}</span>
            <span class="form-label fst-italic card-time">{{
              formattedDate()
            }}</span>
          </div>
        </div>
        <div class="col-lg-4 col-md-12 text-lg-end">
          <div v-if="authenticationStore.isAuthenticated">
            <div
              class="btn button button-primary"
              v-if="!isApplied"
              @click.prevent="applyJob"
            >
              {{ headerData.internal ? "Apply" : "Easy Apply" }}
            </div>
            <div class="btn button btn-secondary" v-else>Applied</div>
          </div>
          <div v-else>
            <router-link
              :to="{ name: 'Auth', params: { slug: 'signin' } }"
              class="btn button button-primary"
              >Login/SignUp</router-link
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getAuthenticationStore } from "@/services/authService";
import { postDataWithToken } from "@/services/apiService";
import moment from "moment";
import { API } from "@/api";

export default {
  name: "JobDetailsHeader",
  props: ["headerData", "isApplied"],
  data() {
    return {
      authenticationStore: getAuthenticationStore(),
    };
  },
  methods: {
    formattedDate() {
      const createdDate = moment(this.headerData.dateCreated);
      return createdDate.fromNow();
    },
    async applyJob() {
      // check if the job is internal
      if (this.headerData.internal) {
        // if internal, redirect to the job details page in indeed
        window.open(this.headerData.jobLink, "_blank");
      } else {
        // if not internal, open the easy apply modal
        console.log("easy apply");
        if (this.authenticationStore.employeeProfileCompleted) {
          const url = API.jobs.apply_job;
          const applyToJobAPI = await postDataWithToken(
            url,
            { job_id: this.headerData.pk },
            this.authenticationStore.token
          );

          if (applyToJobAPI) {
            this.$emit("applied");
          }
        } else {
          // show alert to ask user to complete employee profile before they can apply
          alert("Please complete your employee profile first");
        }
      }
    },
  },
};
</script>

<style scoped>
.job-title {
  font-size: 1.6rem;
  font-family: var(--Nunito);
  font-weight: 500;
  line-height: 1.5;
  color: var(----primary-color-1);
}
.card-briefcase {
  display: inline-block;
  padding: 2px 20px 2px 20px;
  background: url(../src/assets/img/icons/icons-briefcase.svg) no-repeat 0px 6px;
  background-size: 15px;
  margin-right: 10px;
  background-position: 0px 6px;
}

.card-time {
  display: inline-block;
  padding: 2px 20px 2px 20px;
  background: url(../src/assets/img/icons/icons-refresh.svg) no-repeat 0px 6px;
  background-size: 15px;
  margin-right: 10px;
  background-position: 0px 6px;
}

.card-framework {
  display: inline-block;
  padding: 4px 25px 4px 25px;
  background: url(../src/assets/img/icons/icons-framework.svg) no-repeat 0px 6px;
  background-size: 20px;
  margin-right: 10px;
  background-position: 0px 6px;
}
</style>
