<template>
  <div class="col-xl-4 order-xl-1 mb-3 p-2">
    <div class="card shadow border-0 text-center p-0">
      <div class="card-body pb-4">
        <img
          :src="companyLogoPath"
          class="img-fluid avatar-xl rounded-circle mx-auto mt-n7 mb-4"
          alt="company logo"
          style="width: 200px; height: 200px"
        />
        <h4 class="h3">{{ companyName }}</h4>
        <p class="text-gray mb-2">company size: {{ companySize }} employees</p>
        <p class="text-gray mb-2">company location: {{ companyLocation }}</p>

        <a class="fw-normal" :href="companyWebsite" target="_blank"
          >Company website</a
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CompanyCard",
  props: [
    "companyName",
    "companySize",
    "companyLocation",
    "companyWebsite",
    "companyLogoPath",
  ],
};
</script>

<style></style>
