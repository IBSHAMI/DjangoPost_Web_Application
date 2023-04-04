<template>
  <div class="col-xl-4 order-xl-1 mb-sm-4">
    <div class="card border-0 text-center p-0">
      <div class="card-body pb-5">
        <img
          :src="employeePicturePath"
          class="img-fluid avatar-xl rounded-circle mx-auto mt-n7 mb-4"
          alt="employee picture"
          style="width: 200px; height: 200px"
        />
        <h4 class="h3">{{ fullName }}</h4>
        <h5 class="fw-normal">{{ experience }}</h5>
        <p class="text-gray mb-4">New York, USA</p>
        <p class="text-gray mb-4">
          <a class="fw-normal" :href="linkedin" target="_blank">Linkedin</a>
          |
          <a class="fw-normal" :href="protofolio" target="_blank">Protofolio</a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "EmployeeCard",
  props: [
    "fullName",
    "experience",
    "linkedin",
    "protofolio",
    "employeePicturePath",
  ],
};
</script>

<style></style>
