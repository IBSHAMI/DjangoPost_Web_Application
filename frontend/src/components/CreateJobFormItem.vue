<template>
  <div class="mt-5 md:col-span-2 md:mt-0">
    <vee-form action="#" :validation-schema="schema">
      <div class="shadow sm:overflow-hidden sm:rounded-md">
        <alert-item
          :alert="alert"
          :alertBackgroundColor="alertBackgroundColor"
          :alertMessage="alertMessage"
          @closeAlert="closeAlert"
        />
        <div class="space-y-6 bg-white px-4 py-5 sm:p-6">
          <div class="grid grid-cols-4 gap-6 py-5">
            <div class="col-span-3 sm:col-span-2">
              <label
                for="position_title"
                class="block text-base font-medium text-gray-700"
                >Position Title</label
              >
              <div class="w-full h-full relative mt-1 py-2">
                <vee-field
                  type="text"
                  name="position_title"
                  id="position_title"
                  class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                  v-model="positionTitle"
                />
                <ErrorMessage
                  name="position_title"
                  class="text-red-500 text-xs italic"
                />
              </div>
            </div>
          </div>
          <div class="grid grid-cols-4 gap-6 py-5">
            <div class="col-span-3 sm:col-span-2">
              <label
                for="position_type"
                class="block text-base font-medium text-gray-700"
                >Position Type</label
              >
              <div class="w-full h-full relative mt-1 py-2">
                <vee-field
                  type="text"
                  name="position_type"
                  id="position_type"
                  class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                  v-model="positionType"
                />
                <ErrorMessage
                  name="position_type"
                  class="text-red-500 text-xs italic"
                />
              </div>
            </div>
          </div>
          <div class="grid grid-cols-4 gap-6 py-5">
            <div class="col-span-3 sm:col-span-2">
              <label
                for="position_location"
                class="block text-base font-medium text-gray-700"
                >Position Location</label
              >
              <div class="w-full h-full relative mt-1 py-2">
                <vee-field
                  type="text"
                  name="position_location"
                  id="position_location"
                  class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                  v-model="positionLocation"
                />
                <ErrorMessage
                  name="position_location"
                  class="text-red-500 text-xs italic"
                />
              </div>
            </div>
          </div>
          <div class="grid grid-cols-4 gap-6 py-5">
            <div class="col-span-3 sm:col-span-2">
              <label
                for="language_required"
                class="block text-base font-medium text-gray-700"
                >Language Required</label
              >
              <div class="w-full h-full relative mt-1 py-2">
                <vee-field
                  type="text"
                  name="language_required"
                  id="language_required"
                  class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                  v-model="languageRequired"
                />
                <ErrorMessage
                  name="language_required"
                  class="text-red-500 text-xs italic"
                />
              </div>
            </div>
          </div>
          <div class="grid grid-cols-4 gap-6 py-5">
            <div class="col-span-3 sm:col-span-2">
              <label
                for="positions_number"
                class="block text-base font-medium text-gray-700"
                >Number of positions
              </label>
              <div class="w-full h-full relative mt-1 py-2">
                <vee-field
                  type="number"
                  name="positions_number"
                  id="positions_number"
                  class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                  v-model="positionsNumber"
                />
                <ErrorMessage
                  name="positions_number"
                  class="text-red-500 text-xs italic"
                />
              </div>
            </div>
          </div>
          <div class="grid grid-cols-4 gap-6 py-5">
            <div class="col-span-3 sm:col-span-2">
              <label
                for="salary"
                class="block text-base font-medium text-gray-700"
                >Salary
              </label>
              <div class="w-full h-full relative mt-1 py-2">
                <vee-field
                  type="number"
                  name="salary"
                  id="salary"
                  class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                  v-model="salary"
                />
                <ErrorMessage
                  name="salary"
                  class="text-red-500 text-xs italic"
                />
              </div>
            </div>
          </div>
          <div class="grid grid-cols-4 gap-6 py-5">
            <div class="col-span-3 sm:col-span-2">
              <label
                for="position_experience"
                class="block text-base font-medium text-gray-700"
                >Years of Experience Required</label
              >
              <div class="w-full h-full relative mt-1 py-2">
                <vee-field
                  type="text"
                  name="position_experience"
                  id="position_experience"
                  class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                  v-model="positionExperienceRequired"
                />
                <ErrorMessage
                  name="position_experience"
                  class="text-red-500 text-xs italic"
                />
              </div>
            </div>
          </div>
          <div>
            <div class="col-span-3 sm:col-span-2">
              <label
                for="job_description"
                class="block text-base font-medium text-gray-700"
                >Job description</label
              >
              <ErrorMessage
                name="job_description"
                class="text-red-500 text-xs italic"
              />
              <div class="w-full h-full relative mt-1 py-2">
                <vee-field
                  as="textarea"
                  id="job_description"
                  name="job_description"
                  rows="3"
                  class="mt-1 block w-full rounded-md border-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                  v-model="jobDescription"
                ></vee-field>
              </div>
            </div>
            <div class="grid grid-cols-4 gap-6 py-5">
              <div class="col-span-3 sm:col-span-2">
                <vee-field
                  id="remote"
                  aria-describedby="remote"
                  type="checkbox"
                  class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"
                  name="terms"
                  v-model="remote"
                />
                <ErrorMessage
                  name="remote"
                  class="text-red-500 text-xs italic"
                />
                <label
                  for="remote"
                  class="block text-base font-medium text-gray-700"
                  >Remote</label
                >
              </div>
            </div>
          </div>
        </div>
        <div class="bg-gray-50 px-4 py-3 text-center sm:px-6" @click.prevent="">
          <button
            type="button"
            class="text-sky-500 border border-sky-500 hover:bg-sky-500 hover:text-white active:bg-sky-600 font-bold uppercase px-8 py-3 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
          >
            Create Job
          </button>
        </div>
      </div>
    </vee-form>
  </div>
</template>

<script>
import AlertItem from "@/components/AlertItem.vue";

export default {
  name: "CreateJobFormItem",
  data() {
    return {
      // Alert varaibles
      alert: false,
      alertMessage: "",
      alertBackgroundColor: "",

      // schema for the form
      schema: {
        position_title: "required|min:10|max:100",
        position_type: "required|min:10|max:100",
        position_location: "required|min:10|max:100",
        language_required: "required|min:10|max:100",
        positions_number: "required",
        salary: "required",
        position_experience: "",
        job_description: "required|min:100|max:1000",
        remote: "",
      },

      // form data
      positionTitle: "",
      positionType: "",
      positionLocation: "",
      languageRequired: "",
      positionsNumber: "",
      salary: "",
      positionExperienceRequired: "",
      jobDescription: "",
      remote: false,
    };
  },
  components: {
    AlertItem,
  },
  methods: {
    getCompanyDescription() {
      this.companyDescription = this.$store.state.user.company_description;
    },
    closeAlert() {
      this.alert = false;
      this.alertBackgroundColor = "";
      this.alertMessage = "";
    },
  },
};
</script>

<style></style>
