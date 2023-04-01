<template>
  <section class="hero-section overflow-hidden" id="home">
    <div class="container mt-5 pt-5">
      <div class="position-relative" style="z-index: 1">
        <div class="row align-items-center">
          <div class="col-xl-5 col-lg-6">
            <div>
              <h6 class="title-text mb-4">Welcome to DjangoPost</h6>
              <h1>Your One-Stop Platform for Software Development Jobs</h1>
              <p class="text-black-100 para fs-17 pt-4">
                DjangoPost connects job seekers and employers in the software
                development industry. Our platform is designed to showcase your
                skills in Django, Vue.js, and other popular frameworks, making
                it easy to find the perfect job or hire top talent.
              </p>
              <div class="mt-5">
                <router-link
                  :to="{ name: 'Jobs', params: { slug: 'jobs' } }"
                  class="btn button btn-lg button-primary"
                  >Find Jobs</router-link
                >
              </div>
            </div>
          </div>
          <!--end col-->
          <div class="col-lg-6 offset-xl-1">
            <div class="mt-lg-0 mt-5">
              <img
                src="../../../src/assets/img/landing_page/hero-section.svg"
                alt="hero-section"
                class="img-fluid"
              />
            </div>
          </div>
        </div>
        <!--end row-->
      </div>
    </div>
    <!--end container-->
  </section>
</template>

<script>
export default {
  name: "HeroSection",
};
</script>

<style scoped>
.hero-section {
  background: rgba(6, 168, 99, 0.2);
  padding: 100px 0;
}
.title-text {
  font-size: 15px;
  font-weight: 600;
  color: #11ab7c;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}
</style>
