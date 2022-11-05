<template>
  <div
    class="text-white px-6 py-4 border-0 rounded relative mb-4"
    :class="alertBackgroundColor"
    v-show="alert"
  >
    <span class="text-xl inline-block mr-5 align-middle">
      <i class="fas fa-bell" />
    </span>
    <span class="inline-block align-middle mr-8">
      {{ alertMessage }}
    </span>
    <div
      class="absolute bg-transparent text-2xl font-semibold leading-none right-0 top-0 mt-4 mr-6 outline-none focus:outline-none"
      style="cursor: pointer"
      @click.prevent="closeAlert"
    >
      <span>×</span>
    </div>
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
