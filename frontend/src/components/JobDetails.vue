<template>
  <div class="container py-4 my-4">
    <div class="row">
      <div class="row pb-3">
        <div class="container-fluid">
          <div class="row">
            <div class="col-xl-8 order-xl-1">
              <div class="card overflow-hidden">
                <job-details-header />
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

export default {
  name: "JobDetails",
  props: ["jobId"],
  components: {
    JobDetailsHeader,
  },
};
</script>

<style scoped></style>
