<template>
  <section class="features-section" id="features">
    <div class="container py-5 my-5">
      <div class="row justify-content-center my-5">
        <div class="col-lg-6">
          <div class="text-center mb-5">
            <h3 class="features-title">DjangoPost Features</h3>
            <p class="para features-para pt-2">
              Explore the key features that make DjangoPost the go-to platform
              for software development job seekers and employers.
            </p>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-lg-4 col-md-6">
          <div class="feature-card card border-0 mt-3">
            <div class="card-body" style="flex: 1 1 auto; padding: 1rem 1rem">
              <div class="mx-auto">
                <img
                  src="../../../src/assets/img/landing_page/dual-account.svg"
                  alt="Dual Account"
                  class="img-fluid svg-feature-icon"
                />
              </div>
              <div class="my-4">
                <h6 class="mb-3 py-2 fs-17">Dual Account Types</h6>
                <p class="text-muted">
                  Create both employee and company accounts, allowing you to
                  switch between job-seeking and hiring roles with ease.
                </p>
              </div>
            </div>
            <!--end card-body-->
          </div>
          <!--end feature-box-->
        </div>

        <div class="col-lg-4 col-md-6">
          <div class="feature-card card border-0 mt-3">
            <div class="card-body" style="flex: 1 1 auto; padding: 1rem 1rem">
              <div class="mx-auto">
                <img
                  src="../../../src/assets/img/landing_page/celery-search.svg"
                  alt="Celery Search"
                  class="img-fluid svg-feature-icon"
                />
              </div>
              <div class="my-4">
                <h6 class="mb-3 py-2 fs-17">Job Aggregation</h6>
                <p class="text-muted">
                  Our platform utilizes Celery to scrape job listings from
                  Indeed, expanding your job search beyond user-posted
                  positions.
                </p>
              </div>
            </div>
            <!--end card-body-->
          </div>
          <!--end feature-box-->
        </div>

        <div class="col-lg-4 col-md-6">
          <div class="feature-card card border-0 mt-3">
            <div class="card-body" style="flex: 1 1 auto; padding: 1rem 1rem">
              <div class="mx-auto">
                <img
                  src="../../../src/assets/img/landing_page/Skilled-based.svg"
                  alt="Skilled Based"
                  class="img-fluid svg-feature-icon"
                />
              </div>
              <div class="my-4">
                <h6 class="mb-3 py-2 fs-17">Skill-Based Jobs</h6>
                <p class="text-muted">
                  Showcase your skills in Django, Vue.js, and other popular
                  frameworks to find the perfect job or hire top talent in the
                  software development industry.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "FeaturesSection",
};
</script>

<style scoped>
.features-title {
  font: 500 2rem/1.5 var(--Nunito);
  color: var(--primary-color-1);
}

.features-para {
  font: 400 1rem/1.5 var(--Nunito);
  color: var(--primary-color-2);
}

.feature-card {
  text-align: center;
  background-color: transparent;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}

.svg-feature-icon {
  width: 300px;
  height: 250px;
}
</style>
