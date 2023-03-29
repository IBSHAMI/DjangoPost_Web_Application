<template>
  <div class="col-md-12 col-lg-6">
    <div class="job-card card overflow-hidden m-3">
      <div class="job-card__content">
        <div class="job-card_info">
          <h6 class="d-flex justify-content-between">
            <p class="paragraph">{{ job.company_name }}</p>
            <a
              href="#!"
              class="float-right"
              style="position: absolute; top: 15px; right: 10px"
            >
              <img
                src="../../../src/assets/img/icons/icons-heart.svg"
                alt="save job icon"
                class="img-fluid"
                style="width: 25px; height: 25px"
              />
            </a>
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
        </div>
      </div>
      <div class="job-card__footer">
        <div class="job-card_job-type">
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
import moment from "moment";

export default {
  name: "JobCard",
  props: ["job"],
  computed: {
    getLogoPath() {
      return "http://127.0.0.1:8000" + this.job.company_logo;
    },
  },
  methods: {
    formattedDate(data) {
      const createdDate = moment(data);
      return createdDate.fromNow();
    },
    openJobDetails() {
      this.$router.push({
        name: "Jobs",
        params: { slug: `jobDetails-${this.job.pk}` },
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
