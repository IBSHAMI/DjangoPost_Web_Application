<template>
  <tr tabindex="0" class="">
    <td class="">
      <div class="flex items-center pl-5">
        <p class="text-base font-medium leading-none text-gray-700 mr-2">
          {{ job.title }}
        </p>
      </div>
    </td>
    <td class="pl-5">
      <div class="flex items-center">
        <p class="text-sm leading-none text-gray-600 ml-2">{{ job.type }}</p>
      </div>
    </td>
    <td class="pl-5">
      <div class="flex items-center">
        <p class="text-sm leading-none text-gray-600 ml-2">{{ job.salary }}</p>
      </div>
    </td>
    <td class="pl-5">
      <div class="flex items-center">
        <p class="text-sm leading-none text-gray-600 ml-2">
          {{ job.language }}
        </p>
      </div>
    </td>
    <td class="pl-5">
      <div class="flex items-center">
        <p class="text-sm leading-none text-gray-600 ml-2">{{ dateCreated }}</p>
      </div>
    </td>
    <td class="pl-5">
      <button
        class="py-3 px-3 text-sm focus:outline-none leading-none text-red-700 bg-red-100 rounded"
        :class="{
          'bg-red-100 text-red-700': job.is_active === false,
          'bg-green-100 text-green-700': job.is_active === true,
        }"
      >
        {{ job.is_active ? "Active" : "Inactive" }}
      </button>
    </td>
    <td class="pl-4">
      <a
        class="focus:ring-2 focus:ring-offset-2 focus:ring-red-300 text-sm leading-none text-gray-600 py-3 px-5 bg-gray-100 rounded hover:bg-gray-200 focus:outline-none"
      >
        View
      </a>
    </td>
    <div class="grid place-items-center px-5 pt-5">
      <jobs-dropdown-item :jobId="job.pk" />
    </div>
  </tr>
</template>

<script>
import JobsDropdownItem from "./JobsDropdownItem.vue";

export default {
  name: "JobRowTableItem",
  props: ["job"],
  data() {
    return {
      jobDropdown: false,
      dateCreated: new Date(this.job.date_created).toLocaleDateString(),
    };
  },
  components: {
    JobsDropdownItem,
  },
};
</script>

<style></style>
