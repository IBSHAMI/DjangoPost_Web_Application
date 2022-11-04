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
              <div class="space-y-6 bg-white px-4 py-5 sm:p-6">
                <div class="grid grid-cols-4 gap-6 py-5">
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="price"
                      class="block text-base font-medium text-gray-700"
                      >First Name</label
                    >
                    <ErrorMessage
                      name="first_name"
                      class="text-red-500 text-xs italic"
                    />
                    <div class="w-full h-full relative mt-1 py-2">
                      <vee-field
                        type="text"
                        name="first_name"
                        id="first_name"
                        class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-800 focus:ring-indigo-800 sm:text-sm"
                        v-model="firstName"
                      />
                    </div>
                  </div>
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="company-website"
                      class="block text-base font-medium text-gray-700"
                      >Last Name</label
                    >
                    <ErrorMessage
                      name="last_name"
                      class="text-red-500 text-xs italic"
                    />
                    <div class="mt-1 w-full h-full flex py-2">
                      <vee-field
                        type="text"
                        name="last_name"
                        id="last_name"
                        class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        v-model="lastName"
                      />
                    </div>
                  </div>
                </div>
                <div class="grid grid-cols-4 gap-6 py-5">
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="price"
                      class="block text-base font-medium text-gray-700"
                      >Email</label
                    >
                    <div class="w-full h-full relative mt-1 py-2">
                      <vee-field
                        type="text"
                        name="email"
                        id="email"
                        class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        v-model="email"
                      />
                      <ErrorMessage
                        name="email"
                        class="text-red-500 text-xs italic"
                      />
                    </div>
                  </div>
                </div>
                <div class="grid grid-cols-4 gap-6 py-5">
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="price"
                      class="block text-base font-medium text-gray-700"
                      >Software Field</label
                    >
                    <ErrorMessage
                      name="software_field"
                      class="text-red-500 text-xs italic"
                    />
                    <div class="w-full h-full relative mt-1 py-2">
                      <vee-field
                        type="text"
                        name="software_field"
                        id="software_field"
                        class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        v-model="softwareField"
                      />
                    </div>
                  </div>
                </div>
                <div class="grid grid-cols-4 gap-6 py-5">
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="price"
                      class="block text-base font-medium text-gray-700"
                      >Expected Salary</label
                    >
                    <ErrorMessage
                      name="expected_salary"
                      class="text-red-500 text-xs italic"
                    />
                    <div class="w-full h-full relative mt-1 py-2">
                      <div
                        class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3"
                      >
                        <span class="text-gray-500 sm:text-sm">$</span>
                      </div>
                      <vee-field
                        type="number"
                        name="expected_salary"
                        id="expected_salary"
                        class="block w-full h-full rounded-md border-2 pl-7 pr-12 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        v-model="expectedSalary"
                      />

                      <div class="absolute inset-y-0 right-0 flex items-center">
                        <label for="currency" class="sr-only">Currency</label>
                        <select
                          id="currency"
                          name="currency"
                          class="h-full rounded-md border-transparent bg-transparent py-0 pl-2 pr-7 text-gray-500 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        >
                          <option>USD</option>
                        </select>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="grid grid-cols-4 gap-6 py-5">
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="company-website"
                      class="block text-base font-medium text-gray-700"
                      >Linkedin Profile</label
                    >
                    <ErrorMessage
                      name="linkedin_profile"
                      class="text-red-500 text-xs italic"
                    />
                    <div class="mt-1 w-full h-full flex py-2">
                      <vee-field
                        type="text"
                        name="linkedin_profile"
                        id="linkedin_profile"
                        class="block w-full h-full flex-1 rounded-none rounded-r-md border-2 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        v-model="linkedinProfile"
                      />
                    </div>
                  </div>
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="company-website"
                      class="block text-base font-medium text-gray-700"
                      >Portfolio Website</label
                    >
                    <div class="mt-1 w-full h-full flex py-2">
                      <vee-field
                        type="text"
                        name="portfolio_website"
                        id="profile_website"
                        class="block w-full flex-1 rounded-none rounded-r-md border-2 focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        v-model="portfolioWebsite"
                      />
                      <ErrorMessage
                        name="profile_website"
                        class="text-red-500 text-xs italic"
                      />
                    </div>
                  </div>
                </div>
                <div>
                  <div class="col-span-3 sm:col-span-2">
                    <label
                      for="price"
                      class="block text-base font-medium text-gray-700"
                      >About</label
                    >
                    <ErrorMessage
                      name="about"
                      class="text-red-500 text-xs italic"
                    />
                    <div class="w-full h-full relative mt-1 py-2">
                      <textarea
                        id="about"
                        name="about"
                        rows="3"
                        class="mt-1 block w-full rounded-md border-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        v-model="about"
                      ></textarea>
                    </div>
                  </div>
                </div>
                <div>
                  <label
                    class="block text-sm text-base font-medium text-gray-700"
                    >Upload Resume</label
                  >
                  <div class="mt-1 py-2">
                    <!--Show the name of the already uploaded file if any -->
                    <div
                      v-if="resume"
                      class="flex items-center justify-between pb-4"
                    >
                      {{ resume }}
                    </div>
                    <button
                      class="text-sky-500 border border-sky-500 hover:bg-sky-500 hover:text-white active:bg-sky-600 font-bold uppercase px-8 py-3 rounded-full outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                      type="button"
                      v-if="!resumeUploadShow"
                      @click.prevent="resumeUploadShow = true"
                    >
                      Upload Resume
                    </button>
                    <profile-resume-upload
                      v-else
                      @upload="upload"
                      @closeUploadModel="CloseUploadModel"
                    />
                  </div>
                </div>

                <div>
                  <label
                    class="block text-sm text-base font-medium text-gray-700"
                    >Upload Profile Photo</label
                  >
                  <div class="mt-1 py-2">
                    <div
                      v-if="profilePicture"
                      class="flex items-center justify-between pb-4"
                    >
                      {{ profilePicture }}
                    </div>
                    <button
                      class="text-sky-500 border border-sky-500 hover:bg-sky-500 hover:text-white active:bg-sky-600 font-bold uppercase px-8 py-3 rounded-full outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                      type="button"
                      v-if="!PictureUploadShow"
                      @click.prevent="PictureUploadShow = true"
                    >
                      Upload Profile Photo
                    </button>
                    <profile-picture-upload
                      v-else
                      @upload="upload"
                      @closeUploadModel="CloseUploadModel"
                    />
                  </div>
                </div>

                <!-- <profile-upload @upload="upload" /> -->
              </div>
              <div
                class="bg-gray-50 px-4 py-3 text-right sm:px-6"
                @click.prevent="updateUserData"
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
import ProfileResumeUpload from "@/components/ProfileResumeUpload.vue";
import ProfilePictureUpload from "@/components/ProfilePictureUpload.vue";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "ProfileDataItem",
  created() {
    this.getUserDate();
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
        first_name: "min:5|max:20",
        last_name: "min:5|max:20",
        email: "required|email",
        software_field: "max:25",
        expected_salary: "max:25",
        linkedin_profile: "url",
        portfolio_website: "url",
      },

      // Upload Resume and Profile Picture varaibles
      resumeUploadShow: false,
      PictureUploadShow: false,

      // Upload alert
      alert: false,
      alertBackgroundColor: "",
      alertMessage: "",

      firstName: "",
      lastName: "",
      email: "",
      softwareField: "",
      expectedSalary: null,
      linkedinProfile: "",
      portfolioWebsite: "",
      about: "",
      resume: "",
      profilePicture: "",
    };
  },
  components: {
    ProfileResumeUpload,
    ProfilePictureUpload,
  },
  methods: {
    getUserDate() {
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        "content-type": "application/json",
        // eslint-disable-next-line prettier/prettier
        "Authorization": token,
      };

      axios
        .get(API.employee.details, { headers: headers })
        .then((response) => {
          console.log(response.data);
          this.firstName = response.data.first_name;
          this.lastName = response.data.last_name;
          this.email = response.data.email;
          this.softwareField = response.data.software_field;
          this.expectedSalary = response.data.expected_salary;
          this.linkedinProfile = response.data.linkedin_url;
          this.portfolioWebsite = response.data.portfolio_url;
          this.about = response.data.about;
          this.resume = response.data.resume;
          this.profilePicture = response.data.profile_picture;
        })
        // eslint-disable-next-line no-unused-vars
        .catch((error) => {
          this.alert = true;
          this.alertMessage = " Error occur while fetching data";
          this.alertBackgroundColor = "bg-red-500";
        });
    },
    upload(file, type) {
      // We upload the files to their respective models
      if (type === "resume") {
        // we save the file data to the resume variable
        this.resume = file[0];
      } else if (type === "picture") {
        // we save the file data to the profilePicture variable
        this.profilePicture = file[0];
      }
    },
    CloseUploadModel(model) {
      if (model === "resume_model") {
        this.resumeUploadShow = false;
      } else if (model === "picture_model") {
        this.PictureUploadShow = false;
      }
    },
    // Send the user data to the backend
    updateUserData() {
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        // eslint-disable-next-line prettier/prettier
        "Authorization": token,
      };
      console.log(this.resume);
      console.log(typeof this.resume);

      const data = new FormData();
      data.append("first_name", this.firstName);
      data.append("last_name", this.lastName);
      data.append("email", this.email);
      data.append("software_field", this.softwareField);
      data.append("expected_salary", this.expectedSalary);
      data.append("linkedin_url", this.linkedinProfile);
      data.append("portfolio_url", this.portfolioWebsite);
      data.append("about", this.about);

      // Check if resume is typeof file
      if (this.resume === null) {
        data.append("resume", "");
      } else if (typeof this.resume === "object") {
        data.append("resume", this.resume);
      } else {
        data.append("resume", "");
      }

      // Check if profile picture is typeof file
      if (this.profilePicture === null) {
        data.append("profile_picture", "");
      } else if (typeof this.profilePicture === "object") {
        data.append("profile_picture", this.profilePicture);
      } else {
        data.append("profile_picture", "");
      }

      axios
        .patch(API.employee.details, data, { headers: headers })
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
