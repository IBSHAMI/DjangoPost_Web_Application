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
            }}</span
            ><span class="form-label fst-italic card-time">{{
              formattedDate()
            }}</span>
          </div>
        </div>
        <div class="col-lg-4 col-md-12 text-lg-end">
          <div
            class="btn button button-primary"
            data-bs-toggle="modal"
            data-bs-target="#ModalApplyJobForm"
          >
            {{ headerData.internal ? "Apply" : "Easy Apply" }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import moment from "moment";

export default {
  name: "JobDetailsHeader",
  props: ["headerData"],
  methods: {
    formattedDate() {
      const createdDate = moment(this.headerData.dateCreated);
      return createdDate.fromNow();
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
</style>
