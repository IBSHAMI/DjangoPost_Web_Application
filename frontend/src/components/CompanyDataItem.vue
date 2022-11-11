<template>
  <div>
    <div>
      <div class="md:grid md:grid-cols-3 md:gap-6">
        <div class="md:col-span-1">
          <div class="px-4 sm:px-0">
            <h3 class="text-lg font-medium leading-6 text-gray-900">Profile</h3>
            <p class="mt-1 text-sm text-gray-600">
              This information will be displayed publicly so be careful what you
              share.
            </p>
          </div>
        </div>
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
                      for="company_name"
                      class="block text-base font-medium text-gray-700"
                      >Company name</label
                    >
                    <ErrorMessage
                      name="company_name"
                      class="text-red-500 text-xs italic"
                    />
                    <div class="w-full h-full relative mt-1 py-2">
                      <vee-field
                        type="text"
                        name="company_name"
                        id="company_name"
                        class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        v-model="companyName"
                      />
                    </div>
                  </div>
                </div>
                <div class="grid grid-cols-4 gap-6 py-5">
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="company_size"
                      class="block text-base font-medium text-gray-700"
                      >Company size</label
                    >
                    <ErrorMessage
                      name="company_size"
                      class="text-red-500 text-xs italic"
                    />
                    <div class="w-full h-full relative mt-1 py-2">
                      <vee-field
                        type="text"
                        name="company_size"
                        id="company_size"
                        class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        v-model="companySize"
                      />
                    </div>
                  </div>
                </div>
                <div class="grid grid-cols-4 gap-6 py-5">
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="company-website"
                      class="block text-base font-medium text-gray-700"
                      >Company Website</label
                    >
                    <ErrorMessage
                      name="company-website"
                      class="text-red-500 text-xs italic"
                    />
                    <div class="mt-1 w-full h-full flex py-2">
                      <vee-field
                        type="text"
                        name="company-website"
                        id="company-website"
                        class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        v-model="companyWebsite"
                      />
                    </div>
                  </div>
                </div>
                <div>
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="company_description"
                      class="block text-base font-medium text-gray-700"
                      >Company Description</label
                    >
                    <ErrorMessage
                      name="about"
                      class="text-red-500 text-xs italic"
                    />
                    <div class="w-full h-full relative mt-1 py-2">
                      <vee-field
                        as="textarea"
                        id="company_description"
                        name="company_description"
                        rows="3"
                        class="mt-1 block w-full rounded-md border-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        v-model="companyDescription"
                      ></vee-field>
                    </div>
                  </div>
                </div>

                <div>
                  <label
                    class="block text-sm text-base font-medium text-gray-700"
                    >Upload Company logo</label
                  >
                  <div class="mt-1 py-2">
                    <div
                      v-show="!logoUploadShow"
                      class="flex items-center justify-between pb-4"
                    >
                      {{ companyLogo }}
                    </div>
                    <button
                      class="text-sky-500 border border-sky-500 hover:bg-sky-500 hover:text-white active:bg-sky-600 font-bold uppercase px-8 py-3 rounded-full outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                      type="button"
                      v-if="!logoUploadShow"
                      @click.prevent="logoUploadShow = true"
                    >
                      Upload Company logo
                    </button>
                    <company-logo-upload
                      v-else
                      @upload="upload"
                      @closeUploadModel="CloseUploadModel"
                    />
                  </div>
                </div>
              </div>
              <div
                class="bg-gray-50 px-4 py-3 text-right sm:px-6"
                @click.prevent="updateCompanyData"
              >
                <button
                  type="button"
                  class="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                >
                  Save
                </button>
              </div>
            </div>
          </vee-form>
        </div>
      </div>
    </div>

    <div class="hidden sm:block" aria-hidden="true">
      <div class="py-5">
        <div class="border-t border-gray-200"></div>
      </div>
    </div>
  </div>
</template>

<script>
import useAuthenticationStore from "@/stores/authentication";
import CompanyLogoUpload from "./CompanyLogoUpload.vue";
import AlertItem from "@/components/AlertItem.vue";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "ProfileDataItem",
  created() {
    this.getCompanyData();
  },
  setup() {
    // init the store
    const authenticationStore = useAuthenticationStore();
    return { authenticationStore };
  },
  data() {
    return {
      // Create schema for form validation
      schema: {
        company_name: "min:5|max:40",
        company_size: "min:1|max:40",
        company_website: "required|url",
        company_description: "min:5|max:1000",
      },

      // Upload Resume and Profile Picture varaibles
      logoUploadShow: false,

      // Upload alert
      alert: false,
      alertBackgroundColor: "",
      alertMessage: "",

      companyName: "",
      companySize: "",
      companyWebsite: "",
      companyDescription: "",
      companyLogo: "",
    };
  },
  components: {
    CompanyLogoUpload,
    AlertItem,
  },
  methods: {
    getFileBaseName(path) {
      return path.split("/").reverse()[0];
    },
    getCompanyData() {
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        "content-type": "application/json",
        // eslint-disable-next-line prettier/prettier
          "Authorization": token,
      };

      axios
        .get(API.company.details, { headers: headers })
        .then((response) => {
          this.companyName = response.data.company_name;
          this.companySize = response.data.company_size;
          this.companyWebsite = response.data.company_website;
          this.companyDescription = response.data.company_description;
          if (response.data.company_logo) {
            this.companyLogo = this.getFileBaseName(response.data.company_logo);
          }
        })
        // eslint-disable-next-line no-unused-vars
        .catch((error) => {
          console.log(error);
          this.alert = true;
          this.alertMessage = " Error occur while fetching data";
          this.alertBackgroundColor = "bg-red-500";
        });
    },
    upload(file) {
      // we save the file data to the profilePicture variable
      this.companyLogo = file[0];
    },
    CloseUploadModel() {
      this.logoUploadShow = false;
    },
    closeAlert() {
      this.alert = false;
      this.alertBackgroundColor = "";
      this.alertMessage = "";
    },
    // Send the user data to the backend
    updateCompanyData() {
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        // eslint-disable-next-line prettier/prettier
          "Authorization": token,
      };

      const data = new FormData();
      data.append("company_name", this.companyName);
      data.append("company_size", this.companySize);
      data.append("company_website", this.companyWebsite);
      data.append("company_description", this.companyDescription);

      // Check if resume is typeof file
      if (this.companyLogo === null) {
        data.append("company_logo", "");
      } else if (typeof this.companyLogo === "object") {
        data.append("company_logo", this.companyLogo);
      } else {
        data.append("company_logo", "");
      }

      axios
        .patch(API.company.details, data, { headers: headers })
        // eslint-disable-next-line no-unused-vars
        .then((response) => {
          // show that the data is updated
          this.alert = true;
          this.alertMessage = "Data updated successfully";
          this.alertBackgroundColor = "bg-green-500";
        })
        // eslint-disable-next-line no-unused-vars
        .catch((error) => {
          this.alert = true;
          this.alertMessage = " Error occur while updating data";
          this.alertBackgroundColor = "bg-red-500";
        });
    },
  },
};
</script>
