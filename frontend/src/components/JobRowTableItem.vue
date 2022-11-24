<template>
  <tr
    tabindex="0"
    class="focus:outline-none h-16 border border-gray-100 rounded"
  >
    <td class="">
      <div class="flex items-center pl-5">
        <p class="text-base font-medium leading-none text-gray-700 mr-2">
          {{ job.title }}
        </p>
      </div>
    </td>
    <td class="pl-5">
      <div class="flex items-center">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          viewBox="0 0 20 20"
          fill="none"
        >
          <path
            d="M9.16667 2.5L16.6667 10C17.0911 10.4745 17.0911 11.1922 16.6667 11.6667L11.6667 16.6667C11.1922 17.0911 10.4745 17.0911 10 16.6667L2.5 9.16667V5.83333C2.5 3.99238 3.99238 2.5 5.83333 2.5H9.16667"
            stroke="#52525B"
            stroke-width="1.25"
            stroke-linecap="round"
            stroke-linejoin="round"
          ></path>
          <circle
            cx="7.50004"
            cy="7.49967"
            r="1.66667"
            stroke="#52525B"
            stroke-width="1.25"
            stroke-linecap="round"
            stroke-linejoin="round"
          ></circle>
        </svg>
        <p class="text-sm leading-none text-gray-600 ml-2">{{ job.type }}</p>
      </div>
    </td>
    <td class="pl-5">
      <div class="flex items-center">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          viewBox="0 0 20 20"
          fill="none"
        >
          <path
            d="M7.5 5H16.6667"
            stroke="#52525B"
            stroke-width="1.25"
            stroke-linecap="round"
            stroke-linejoin="round"
          ></path>
          <path
            d="M7.5 10H16.6667"
            stroke="#52525B"
            stroke-width="1.25"
            stroke-linecap="round"
            stroke-linejoin="round"
          ></path>
          <path
            d="M7.5 15H16.6667"
            stroke="#52525B"
            stroke-width="1.25"
            stroke-linecap="round"
            stroke-linejoin="round"
          ></path>
          <path
            d="M4.16669 5V5.00667"
            stroke="#52525B"
            stroke-width="1.25"
            stroke-linecap="round"
            stroke-linejoin="round"
          ></path>
          <path
            d="M4.16669 10V10.0067"
            stroke="#52525B"
            stroke-width="1.25"
            stroke-linecap="round"
            stroke-linejoin="round"
          ></path>
          <path
            d="M4.16669 15V15.0067"
            stroke="#52525B"
            stroke-width="1.25"
            stroke-linecap="round"
            stroke-linejoin="round"
          ></path>
        </svg>
        <p class="text-sm leading-none text-gray-600 ml-2">{{ job.salary }}</p>
      </div>
    </td>
    <td class="pl-5">
      <div class="flex items-center">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          viewBox="0 0 20 20"
          fill="none"
        >
          <path
            d="M3.33331 17.4998V6.6665C3.33331 6.00346 3.59671 5.36758 4.06555 4.89874C4.53439 4.4299 5.17027 4.1665 5.83331 4.1665H14.1666C14.8297 4.1665 15.4656 4.4299 15.9344 4.89874C16.4033 5.36758 16.6666 6.00346 16.6666 6.6665V11.6665C16.6666 12.3295 16.4033 12.9654 15.9344 13.4343C15.4656 13.9031 14.8297 14.1665 14.1666 14.1665H6.66665L3.33331 17.4998Z"
            stroke="#52525B"
            stroke-width="1.25"
            stroke-linecap="round"
            stroke-linejoin="round"
          ></path>
          <path
            d="M10 9.1665V9.17484"
            stroke="#52525B"
            stroke-width="1.25"
            stroke-linecap="round"
            stroke-linejoin="round"
          ></path>
          <path
            d="M6.66669 9.1665V9.17484"
            stroke="#52525B"
            stroke-width="1.25"
            stroke-linecap="round"
            stroke-linejoin="round"
          ></path>
          <path
            d="M13.3333 9.1665V9.17484"
            stroke="#52525B"
            stroke-width="1.25"
            stroke-linecap="round"
            stroke-linejoin="round"
          ></path>
        </svg>
        <p class="text-sm leading-none text-gray-600 ml-2">
          {{ job.language }}
        </p>
      </div>
    </td>
    <td class="pl-5">
      <div class="flex items-center">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          viewBox="0 0 20 20"
          fill="none"
        >
          <path
            d="M12.5 5.83339L7.08333 11.2501C6.75181 11.5816 6.56556 12.0312 6.56556 12.5001C6.56556 12.9689 6.75181 13.4185 7.08333 13.7501C7.41485 14.0816 7.86449 14.2678 8.33333 14.2678C8.80217 14.2678 9.25181 14.0816 9.58333 13.7501L15 8.33339C15.663 7.67034 16.0355 6.77107 16.0355 5.83339C16.0355 4.8957 15.663 3.99643 15 3.33339C14.337 2.67034 13.4377 2.29785 12.5 2.29785C11.5623 2.29785 10.663 2.67034 10 3.33339L4.58333 8.75005C3.58877 9.74461 3.03003 11.0935 3.03003 12.5001C3.03003 13.9066 3.58877 15.2555 4.58333 16.2501C5.57789 17.2446 6.92681 17.8034 8.33333 17.8034C9.73985 17.8034 11.0888 17.2446 12.0833 16.2501L17.5 10.8334"
            stroke="#52525B"
            stroke-width="1.25"
            stroke-linecap="round"
            stroke-linejoin="round"
          ></path>
        </svg>
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
