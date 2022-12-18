<template>
  <div class="container py-4 my-4">
    <div class="row">
      <div class="row pb-3">
        <div class="container-fluid">
          <div class="row">
            <profile-card :fullName="getDisplayName()" />
            <div class="col-xl-8 order-xl-1">
              <vee-form
                action="#"
                :validation-schema="schema"
                @submit="updateUserData"
                class="card shadow border-0 text-center text-md-start"
              >
                <div class="card-body">
                  <alert-item
                    :alert="alert"
                    :alertBackgroundColor="alertBackgroundColor"
                    :alertMessage="alertMessage"
                    @closeAlert="closeAlert"
                  />
                  <h2 class="text-start h5 mb-2 px-2">Profile Information</h2>
                  <div class="card-body px-2">
                    <div class="row py-2">
                      <div class="form-group col-md-6 mb-3">
                        <label for="first_name" class="form-label fst-italic"
                          >First Name</label
                        >
                        <div>
                          <vee-field
                            type="text"
                            name="first_name"
                            id="first_name"
                            class="form-control"
                            v-model="firstName"
                          />
                          <ErrorMessage
                            name="first_name"
                            class="text-danger small font-italic"
                          />
                        </div>
                      </div>
                      <div class="form-group col-md-6 mb-3">
                        <label
                          for="company-website"
                          class="form-label fst-italic"
                          >Last Name</label
                        >
                        <div>
                          <vee-field
                            type="text"
                            name="last_name"
                            id="last_name"
                            class="form-control"
                            v-model="lastName"
                          />
                          <ErrorMessage
                            name="last_name"
                            class="text-danger small font-italic"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="row py-2">
                      <div class="form-group col-md-4 mb-2">
                        <label for="email" class="form-label fst-italic"
                          >Email</label
                        >
                        <div class="">
                          <vee-field
                            type="text"
                            name="email"
                            id="email"
                            class="form-control"
                            v-model="email"
                          />
                          <ErrorMessage
                            name="email"
                            class="text-danger small font-italic"
                          />
                        </div>
                      </div>
                      <div class="form-group col-md-4 mb-2">
                        <label
                          for="position_experience"
                          class="form-label fst-italic"
                          >Years of Experience</label
                        >
                        <div>
                          <vee-field
                            as="select"
                            name="position_experience"
                            id="position_experience"
                            class="form-select"
                            v-model="employeeExperience"
                          >
                            <option
                              v-for="(type, index) in JobExperience"
                              :key="index"
                              :value="type"
                            >
                              {{ type }}
                            </option>
                          </vee-field>
                          <ErrorMessage
                            name="position_experience"
                            class="text-danger small font-italic"
                          />
                        </div>
                      </div>
                      <div class="form-group col-md-4 mb-2">
                        <label for="price" class="form-label fst-italic"
                          >Expected Salary (USD)</label
                        >
                        <div>
                          <vee-field
                            type="number"
                            name="expected_salary"
                            id="expected_salary"
                            class="form-control"
                            v-model="expectedSalary"
                          />
                          <ErrorMessage
                            name="expected_salary"
                            class="text-danger small font-italic"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="row py-2">
                      <div class="form-group col-md-6 mb-3">
                        <label
                          for="company-website"
                          class="form-label fst-italic"
                          >Linkedin Profile</label
                        >
                        <div>
                          <vee-field
                            type="text"
                            name="linkedin_profile"
                            id="linkedin_profile"
                            class="form-control"
                            v-model="linkedinProfile"
                          />
                          <ErrorMessage
                            name="linkedin_profile"
                            class="text-danger small font-italic"
                          />
                        </div>
                      </div>
                      <div class="form-group col-md-6 mb-3">
                        <label
                          for="company-website"
                          class="form-label fst-italic"
                          >Portfolio Website</label
                        >
                        <div>
                          <vee-field
                            type="text"
                            name="portfolio_website"
                            id="profile_website"
                            class="form-control"
                            v-model="portfolioWebsite"
                          />
                          <ErrorMessage
                            name="portfolio_website"
                            class="text-danger small font-italic"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="row py-2">
                      <div class="form-group col-md-12 mb-6">
                        <label for="about" class="form-label fst-italic"
                          >About</label
                        >
                        <ErrorMessage
                          name="about"
                          class="text-danger small font-italic"
                        />
                        <div>
                          <vee-field
                            as="textarea"
                            id="about"
                            name="about"
                            rows="3"
                            class="form-control"
                            v-model="about"
                          ></vee-field>
                          <ErrorMessage
                            name="about"
                            class="text-danger small font-italic"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="row py-2">
                      <div class="form-group col-md-12 mb-6">
                        <label class="form-label fst-italic"
                          >Upload Resume</label
                        >
                        <div class="mt-1 py-2">
                          <div v-show="!resumeUploadShow">
                            {{ resume }}
                          </div>
                          <button
                            class="btn btn-outline-primary my-3"
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
                    </div>
                    <div class="row py-2">
                      <div class="form-group col-md-12 mb-6">
                        <label class="form-label fst-italic"
                          >Upload Profile Photo</label
                        >
                        <div class="mt-1 py-2">
                          <div v-show="!PictureUploadShow">
                            {{ profilePicture }}
                          </div>
                          <button
                            class="btn btn-outline-primary my-3"
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
                    </div>
                  </div>
                  <button type="submit" class="btn btn-primary">
                    Save all
                  </button>
                </div>
              </vee-form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import useAuthenticationStore from "@/stores/authentication";
import ProfileCard from "@/components/profileComponents/ProfileCard.vue";
import ProfileResumeUpload from "@/components/profileComponents/ProfileResumeUpload.vue";
import ProfilePictureUpload from "@/components/profileComponents/ProfilePictureUpload.vue";
import AlertItem from "@/components/AlertItem.vue";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "ProfileDataItem",
  created() {
    this.getEmployeeData();
    this.getChoicesData();
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
        expected_salary: "max:25",
        linkedin_profile: "required|url",
        portfolio_website: "required|url",
        about: "max:500|min:30",
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
      expectedSalary: null,
      employeeExperience: null,
      linkedinProfile: "",
      portfolioWebsite: "",
      about: "",
      resume: "",
      profilePicture: "",

      // choices data
      JobExperience: [],
    };
  },
  components: {
    ProfileCard,
    ProfileResumeUpload,
    ProfilePictureUpload,
    AlertItem,
  },
  methods: {
    getDisplayName() {
      return this.firstName + " " + this.lastName;
    },
    getFileBaseName(path) {
      return path.split("/").reverse()[0];
    },
    getChoicesData() {
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      const getChoicesData = API.jobs.get_choices_data;

      axios
        .get(getChoicesData, { headers })
        .then((response) => {
          this.JobExperience = response.data.job_experience_choices;
          console.log(this.JobExperience);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getEmployeeData() {
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        "content-type": "application/json",
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      axios
        .get(API.employee.details, { headers: headers })
        .then((response) => {
          this.firstName = response.data.first_name;
          this.lastName = response.data.last_name;
          this.email = response.data.email;
          this.expectedSalary = response.data.expected_salary;
          this.employeeExperience = response.data.experience;
          this.linkedinProfile = response.data.linkedin_url;
          this.portfolioWebsite = response.data.portfolio_url;
          this.about = response.data.about;
          if (response.data.resume) {
            this.resume = this.getFileBaseName(response.data.resume);
          }
          if (response.data.profile_picture) {
            this.profilePicture = this.getFileBaseName(
              response.data.profile_picture
            );
          }
          // this.resume = this.getFileBaseName(response.data.resume);
          // this.profilePicture = this.getFileBaseName(
          //   response.data.profile_picture
          // );
        })
        // eslint-disable-next-line no-unused-vars
        .catch((error) => {
          console.log(error);
          this.alert = true;
          this.alertMessage = " Error occur while fetching data";
          this.alertBackgroundColor = "alert alert-danger";
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
    closeAlert() {
      this.alert = false;
      this.alertBackgroundColor = "";
      this.alertMessage = "";
    },
    // Send the user data to the backend
    updateUserData() {
      console.log("updateUserData");
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      const data = new FormData();
      data.append("first_name", this.firstName);
      data.append("last_name", this.lastName);
      data.append("email", this.email);
      data.append("expected_salary", this.expectedSalary);
      data.append("experience", this.employeeExperience);
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
          this.alertBackgroundColor = "alert alert-success";
        })
        // eslint-disable-next-line no-unused-vars
        .catch((error) => {
          this.alert = true;
          this.alertMessage = " Error occur while updating data";
          this.alertBackgroundColor = "alert alert-danger";
        });
    },
  },
};
</script>
