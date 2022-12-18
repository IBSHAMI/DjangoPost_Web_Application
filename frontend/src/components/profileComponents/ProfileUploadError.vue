<template>
  <div
    class="alert alert-danger d-flex justify-content-between"
    v-if="uploadError"
  >
    <span class="ml-auto"> <b>Error!</b> {{ uploadErrorMessage }} </span>
    <button
      class="btn btn-close ml-auto"
      style="cursor: pointer"
      @click.prevent="closeErrorAlert"
    ></button>
  </div>
</template>

<script>
export default {
  name: "ProfileUploadError",
  props: ["uploadError", "uploadErrorMessage"],
  methods: {
    closeErrorAlert() {
      this.$emit("closeErrorAlert");
    },
  },
};
</script>

<style></style>
