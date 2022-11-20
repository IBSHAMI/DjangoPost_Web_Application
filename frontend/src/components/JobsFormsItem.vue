<template>
  <!-- component -->
  <div class="sm:px-6 w-full">
    <!--- more free and premium Tailwind CSS components at https://tailwinduikit.com/ --->
    <div class="px-4 md:px-10 py-4 md:py-7">
      <div class="flex items-center justify-between">
        <p
          tabindex="0"
          class="focus:outline-none text-base sm:text-lg md:text-xl lg:text-2xl font-bold leading-normal text-gray-800"
        >
          Jobs
        </p>
        <div
          class="py-3 px-4 flex items-center text-sm font-medium leading-none text-gray-600 bg-gray-200 hover:bg-gray-300 cursor-pointer rounded"
        >
          <p>Sort By:</p>
          <select
            aria-label="select"
            class="focus:text-indigo-600 focus:outline-none bg-transparent ml-1"
          >
            <option class="text-sm text-indigo-800">Latest</option>
            <option class="text-sm text-indigo-800">Oldest</option>
            <option class="text-sm text-indigo-800">
              Highest Applications
            </option>
          </select>
        </div>
      </div>
    </div>
    <div class="bg-white py-4 md:py-7 px-4 md:px-8 xl:px-10">
      <div class="sm:flex items-center justify-between">
        <div class="flex items-center">
          <a
            class="rounded-full focus:outline-none focus:ring-2 focus:bg-indigo-50 focus:ring-indigo-800"
            href=" javascript:void(0)"
          >
            <div class="py-2 px-8 bg-indigo-100 text-indigo-700 rounded-full">
              <p>All</p>
            </div>
          </a>
          <a
            class="rounded-full focus:outline-none focus:ring-2 focus:bg-indigo-50 focus:ring-indigo-800 ml-4 sm:ml-8"
            href="javascript:void(0)"
          >
            <div
              class="py-2 px-8 text-gray-600 hover:text-indigo-700 hover:bg-indigo-100 rounded-full"
            >
              <p>Active</p>
            </div>
          </a>
          <a
            class="rounded-full focus:outline-none focus:ring-2 focus:bg-indigo-50 focus:ring-indigo-800 ml-4 sm:ml-8"
            href="javascript:void(0)"
          >
            <div
              class="py-2 px-8 text-gray-600 hover:text-indigo-700 hover:bg-indigo-100 rounded-full"
            >
              <p>Inactive</p>
            </div>
          </a>
        </div>
        <router-link
          :to="{ name: 'Company', params: { slug: 'create-job' } }"
          class="focus:ring-2 focus:ring-offset-2 focus:ring-indigo-600 mt-4 sm:mt-0 inline-flex items-start justify-start px-6 py-3 bg-indigo-700 hover:bg-indigo-600 focus:outline-none rounded"
        >
          <p class="text-sm font-medium leading-none text-white">Add Job</p>
        </router-link>
      </div>
      <div class="mt-7 overflow-x-auto">
        <table class="w-full whitespace-nowrap">
          <thead
            class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
          >
            <tr>
              <th scope="col" class="py-3 px-6">Tile</th>
              <th scope="col" class="py-3 px-6">Type</th>
              <th scope="col" class="py-3 px-6">Salary</th>
              <th scope="col" class="py-3 px-6">Language</th>
              <th scope="col" class="py-3 px-6">Created at</th>
              <th scope="col" class="py-3 px-6">Active/Inactive</th>
              <th scope="col" class="py-3 px-6">View</th>
              <th scope="col" class="py-3 px-6">Action</th>
            </tr>
          </thead>
          <tbody>
            <job-row-table-item
              v-for="job in jobsList"
              :key="job.pk"
              :job="job"
            ></job-row-table-item>

            <tr class="h-3"></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import JobRowTableItem from "@/components/JobRowTableItem.vue";
import useAuthenticationStore from "@/stores/authentication";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "JobsForm",
  setup() {
    // init the store
    const authenticationStore = useAuthenticationStore();
    return { authenticationStore };
  },
  created() {
    this.getJobsList();
  },
  data() {
    return {
      jobsList: [],
    };
  },
  components: {
    JobRowTableItem,
  },
  methods: {
    // get jobs list
    getJobsList() {
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        // eslint-disable-next-line prettier/prettier
          "Authorization": token,
      };
      const jobsListUrl = API.jobs.list;

      axios
        .get(jobsListUrl, { headers: headers })
        .then((response) => {
          for (const job of response.data) {
            this.jobsList.push(job);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style></style>
