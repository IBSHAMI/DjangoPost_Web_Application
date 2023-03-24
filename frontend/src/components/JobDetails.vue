<template>
  <div class="container py-4 my-4">
    <div class="row">
      <div class="row pb-3">
        <div class="container-fluid">
          <div class="row">
            <div class="col-xl-8 order-xl-1">
              <div class="card overflow-hidden">
                <job-details-header />
                <job-details-body />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import JobDetailsHeader from "@/components/jobComponents/JobDetailsHeader.vue";
import JobDetailsBody from "@/components/jobComponents/JobDetailsBody.vue";

export default {
  name: "JobDetails",
  props: ["jobId"],
  components: {
    JobDetailsHeader,
    JobDetailsBody,
  },
};
</script>

<style scoped></style>
