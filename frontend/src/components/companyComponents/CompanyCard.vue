<template>
  <div class="col-xl-4 order-xl-1">
    <div class="card shadow border-0 text-center p-0">
      <div class="card-body pb-4">
        <img
          :src="companyLogoPath"
          class="img-fluid shadow-4-strong avatar-xl mx-auto mt-n7 mb-4 border border-2"
          alt="company logo"
          style="width: 200px; height: 200px"
        />
        <h4 class="h3">{{ company.company_name }}</h4>
        <p class="text-gray mb-2">{{ company.company_location }}</p>
        <a class="fw-normal" :href="company.company_website" target="_blank"
          >Company website</a
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CompanyCard",
  props: ["company", "companyLogoPath"],
};
</script>

<style></style>
