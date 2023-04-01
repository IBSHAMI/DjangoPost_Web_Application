<template>
  <section class="section bg-light" id="about">
    <div class="container py-5 my-5">
      <div class="row justify-content-center py-5 my-5">
        <div class="col-lg-7">
          <div class="text-center">
            <h2>
              I am a passionate developer with expertise in Django and Vue.js
            </h2>
            <p class="text-muted pt-4">
              My goal is to create an exceptional job board platform that
              connects job seekers and employers in the software development
              industry.
            </p>
          </div>
        </div>
      </div>

      <div class="row justify-content-center mt-5">
        <div class="col-md-6 col-lg-3">
          <div class="text-center mt-3">
            <h3><span class="statistics-value">200+</span></h3>
            <p class="text-muted">Job Listings</p>
          </div>
        </div>

        <div class="col-md-6 col-lg-3">
          <div class="text-center mt-3">
            <h3><span class="statistics-value">150+</span></h3>
            <p class="text-muted">Registered Users</p>
          </div>
        </div>

        <div class="col-md-6 col-lg-3">
          <div class="text-center mt-3">
            <h3 class="statistics-value">20</h3>
            <p class="text-muted">Companies Featured</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "AboutSection",
};
</script>

<style scoped>
.statistics-value {
  font-size: 2.5rem;
  font-weight: 600;
  color: #11ab7c;
}
</style>
