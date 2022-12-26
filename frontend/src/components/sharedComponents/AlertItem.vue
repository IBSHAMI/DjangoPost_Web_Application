<template>
  <div
    class="px-6 py-4 border-0 rounded mb-4 d-flex justify-content-between"
    :class="alertBackgroundColor"
    v-if="alert"
  >
    <span class="ml-auto">
      {{ alertMessage }}
    </span>
    <button
      class="btn btn-close ml-auto"
      style="cursor: pointer"
      @click.prevent="closeAlert"
    ></button>
  </div>
</template>

<script>
export default {
  name: "AlertItem",
  props: ["alert", "alertMessage", "alertBackgroundColor"],
  methods: {
    closeAlert() {
      this.$emit("closeAlert");
    },
  },
};
</script>
