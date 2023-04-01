<template>
  <div class="col-md-12 col-lg-6">
    <div class="job-card card overflow-hidden m-3">
      <div class="job-card__content">
        <div class="job-card_info">
          <h6 class="d-flex justify-content-between">
            <p class="paragraph">{{ job.company_name }}</p>
            <div
              class="float-right"
              v-show="authenticationStore.isAuthenticated"
              style="
                position: absolute;
                top: 15px;
                right: 10px;
                cursor: pointer;
              "
            >
              <img
                :src="heartSvgPath"
                alt="save job icon"
                class="img-fluid"
                @click.prevent="
                  !isSaved ? addToSavedJobs() : deleteFromSavedJobs()
                "
                style="width: 25px; height: 25px"
              />
            </div>
          </h6>
          <h4
            class="job-title text-start"
            @click.prevent="openJobDetails"
            style="cursor: pointer"
          >
            {{ job.title }}
          </h4>
          <p class="text-start paragraph mb-0" v-show="job.salary">
            ${{ job.salary }}
          </p>
          <p class="text-start mb-0 paragraph">
            Posted {{ formattedDate(job.date_created) }}
          </p>
          <p
            v-show="
              job.job_application_status && tableVariant === 'Applied Jobs'
            "
            class="text-start mb-0 paragraph"
            :class="
              job.job_application_status === 'rejected'
                ? 'text-danger'
                : 'text-success'
            "
          >
            Application Status: {{ job.job_application_status }}
          </p>
        </div>
      </div>
      <div class="job-card__footer">
        <div class="job-card_job-type">
          <!-- Special label for easy apply jobs-->
          <span class="job-label" v-show="!job.internal"> Easy Apply </span>
          <span class="job-label">{{ job.type }}</span>
          <span class="job-label">{{ job.location }}</span>
          <span class="job-label">{{ job.number_of_positions }} Position</span>
        </div>
        <button
          class="btn button btn-lg button-primary"
          @click.prevent="openJobDetails"
        >
          Apply
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import useAuthenticationStore from "@/stores/authentication";
import moment from "moment";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "JobCard",
  props: ["job", "tableVariant"],
  setup() {
    // init the store
    const authenticationStore = useAuthenticationStore();
    return { authenticationStore };
  },
  data() {
    return {
      heartSvgPath: this.job.is_saved_job
        ? "../../../src/assets/img/icons/icons-heart-filled.svg"
        : "../../../src/assets/img/icons/icons-heart.svg",
      isSaved: this.job.is_saved_job,
    };
  },
  methods: {
    formattedDate(data) {
      const createdDate = moment(data);
      return createdDate.fromNow();
    },
    openJobDetails() {
      // make the details page open in a new tab
      const url = this.$router.resolve({
        name: "Jobs",
        params: { slug: `jobDetails-${this.job.pk}` },
      }).href;
      window.open(url, "_blank");
    },
    addToSavedJobs() {
      console.log("add saved job");
      const saveJobUrl = API.jobs.save_job;
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      axios
        .post(saveJobUrl, { job_id: this.job.pk }, { headers })
        .then((res) => {
          console.log(res.status);
          if (res.status === 201) {
            this.heartSvgPath =
              "../../../src/assets/img/icons/icons-heart-filled.svg";
            this.isSaved = true;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteFromSavedJobs() {
      console.log("delete saved job");
      const deleteJobUrl = API.jobs.delete_saved_job;
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      axios
        .delete(deleteJobUrl, { headers, data: { job_id: this.job.pk } })
        .then((res) => {
          console.log(res.status);
          if (res.status === 204) {
            this.heartSvgPath = "../../../src/assets/img/icons/icons-heart.svg";
            this.isSaved = false;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
.job-card {
  background: #fff;
  padding: 25px;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.paragraph {
  color: var(--primary-color-2);
  font: normal 500 16px/16px var(--Nunito);
  color: var(--primary-color-2);
  padding: 2px 0;
  margin: 4px 0;
  box-sizing: border-box;
}

.job-title {
  font-size: 1.5rem;
  font-family: var(--Nunito);
  font-weight: 700;
  color: var(--primary-color-1);
  margin-bottom: 8px;
}

.company-logo {
  height: 200px;
  width: 200px;
  object-fit: contain;
  border-radius: 12px;
}

.job-card__content .job-card_img {
  margin-right: 25px;
}

.job-card__content .job-card_img img {
  height: 100px;
  width: 100px;
  object-fit: contain;
  border-radius: 8px;
}

p {
  display: block;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
}

.text-muted {
  color: #6c757d !important;
}

.job-card__content {
  display: flex;
  align-items: center;
  margin-bottom: 25px;
}

.job-card__footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.job-label {
  display: inline-block;
  padding: 6px 12px;
  background: #f5f5f5;
  border-radius: 5px;
  margin-right: 2px;
}

.job-card__content .job-card_info .text-muted a {
  color: #777;
}
</style>
