<template>
  <div class="container py-4 my-4">
    <div class="row">
      <div class="row pb-3">
        <div class="container-fluid">
          <div class="row">
            <employee-card
              :fullName="getDisplayName()"
              :experience="employeeExperience"
              :linkedin="linkedinProfile"
              :protofolio="portfolioWebsite"
              :employeePicturePath="
                this.authenticationStore.employeeProfilePicture
              "
            />
            <div class="col-xl-8 order-xl-1">
              <vee-form
                action="#"
                :validation-schema="schema"
                @submit="updateUserData"
                class="card border-0 text-center text-md-start"
              >
                <div class="card-body">
                  <shared-component-alert-item
                    :alert="alert"
                    :alertBackgroundColor="alertBackgroundColor"
                    :alertMessage="alertMessage"
                    @closeAlert="closeAlert"
                  />
                  <h2 class="text-center form-header">Employee Information</h2>
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
                            class="error-message small font-italic"
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
                            class="error-message small font-italic"
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
                            class="error-message small font-italic"
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
                            class="error-message small font-italic"
                          />
                        </div>
                      </div>
                      <div class="form-group col-md-4 mb-2">
                        <label
                          for="expected_salary"
                          class="form-label fst-italic"
                          >Expected Salary (USD)</label
                        >
                        <div>
                          <vee-field
                            as="select"
                            name="expected_salary"
                            id="expected_salary"
                            class="form-control"
                            v-model="expectedSalary"
                          >
                            <option
                              v-for="(salary, index) in JobsSalary"
                              :key="index"
                              :value="salary"
                            >
                              {{ salary }}
                            </option>
                          </vee-field>
                          <ErrorMessage
                            name="expected_salary"
                            class="error-message small font-italic"
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
                            class="error-message small font-italic"
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
                            class="error-message small font-italic"
                          />
                        </div>
                      </div>
                    </div>
                    <button
                      type="submit"
                      class="btn button button-primary my-2"
                    >
                      Save all
                    </button>
                    <hr />
                    <div class="row py-2">
                      <div class="form-group col-md-12 mb-6">
                        <label class="form-label fst-italic"
                          >Upload Resume
                          <small>(File size must be below 5MB )</small></label
                        >
                        <div class="mt-1 py-2">
                          <div v-show="!resumeUploadShow">
                            {{ resume }}
                          </div>
                          <button
                            class="btn button btn-outline-primary my-3"
                            type="button"
                            v-if="!resumeUploadShow"
                            @click.prevent="resumeUploadShow = true"
                          >
                            Click to Drag New Resume
                          </button>
                          <employee-resume-upload
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
                          >Upload employee Photo
                          <small>(File size must be below 2MB )</small></label
                        >
                        <div class="mt-1 py-2">
                          <div v-show="!PictureUploadShow">
                            {{ employeePicture }}
                          </div>
                          <button
                            class="btn btn-outline-primary my-3"
                            type="button"
                            v-if="!PictureUploadShow"
                            @click.prevent="PictureUploadShow = true"
                          >
                            Click to Drag employee Picture
                          </button>
                          <employee-picture-upload
                            v-else
                            @upload="upload"
                            @closeUploadModel="CloseUploadModel"
                          />
                        </div>
                        <button
                          class="btn button button-primary my-2"
                          @click.prevent="uploadFiles"
                        >
                          Upload Files
                        </button>
                        <button
                          v-show="resume && resumeuploadedCheck"
                          class="btn button button-primary my-2 mx-2"
                          @click.prevent="downloadResume"
                        >
                          Download Resume
                        </button>
                      </div>
                    </div>
                  </div>
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
import EmployeeCard from "@/components/employeeComponents/EmployeeCard.vue";
import EmployeeResumeUpload from "@/components/employeeComponents/EmployeeResumeUpload.vue";
import EmployeePictureUpload from "@/components/employeeComponents/EmployeePictureUpload.vue";
import {
  getProfileData,
  updateProfileData,
  uploadProfilePicture,
  getChoicesData,
} from "@/services/profileService";
import { uploadEmployeeResume } from "@/services/employeeSpecificService";
import { getAuthenticationStore } from "@/services/authService";

export default {
  name: "EmployeeDataItem",
  async created() {
    this.authenticationStore = getAuthenticationStore();
    const employeeData = await getProfileData(
      this.authenticationStore.token,
      "employee"
    );

    if (employeeData) {
      this.firstName = employeeData.first_name;
      this.lastName = employeeData.last_name;
      this.email = employeeData.email;
      this.expectedSalary = employeeData.expected_salary;
      this.employeeExperience = employeeData.experience;
      this.linkedinProfile = employeeData.linkedin_url;
      this.portfolioWebsite = employeeData.portfolio_url;
      if (employeeData.resume) {
        this.resume = this.getFileBaseName(employeeData.resume);
        this.resumeuploadedCheck = true;
      }
      if (employeeData.profile_picture) {
        this.employeePicture = this.getFileBaseName(
          employeeData.profile_picture
        );
      }
    } else if (employeeData == null) {
      this.alert = true;
      this.alertMessage = " Error occur while fetching data";
      this.alertBackgroundColor = "alert alert-danger";
    }
    await this.getChoicesData();
  },
  data() {
    return {
      // Create schema for form validation
      schema: {
        first_name: "required|min:5|max:20",
        last_name: "required|min:5|max:20",
        email: "required|email",
        expected_salary: "required|max:25",
        linkedin_profile: "required|url",
        portfolio_website: "required|url",
      },

      // Upload Resume and employee Picture varaibles
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
      resume: "",
      employeePicture: "",

      // this value is used to help show download resume button
      // since resume value is updated even tho the user did not
      // upload the resume to the server yet, resume value is updated
      // hence resume value alone cant be used to show the download resume button
      resumeuploadedCheck: false,

      // choices data
      JobExperience: [],
      JobsSalary: [],

      // Authentication store
      authenticationStore: {},
    };
  },
  components: {
    EmployeeCard,
    EmployeeResumeUpload,
    EmployeePictureUpload,
  },
  methods: {
    getDisplayName() {
      return this.firstName + " " + this.lastName;
    },
    getFileBaseName(path) {
      return path.split("/").reverse()[0];
    },
    async getChoicesData() {
      const choicesData = await getChoicesData(this.authenticationStore.token);

      if (choicesData) {
        this.JobExperience = choicesData.job_experience_choices;
        this.JobsSalary = choicesData.job_salary_choices;
      }
    },
    upload(file, type) {
      if (type === "resume") {
        this.resume = file[0];
      } else if (type === "picture") {
        this.employeePicture = file[0];
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
    async updateUserData() {
      const data = new FormData();
      data.append("first_name", this.firstName);
      data.append("last_name", this.lastName);
      data.append("email", this.email);
      data.append("expected_salary", this.expectedSalary);
      data.append("experience", this.employeeExperience);
      data.append("linkedin_url", this.linkedinProfile);
      data.append("portfolio_url", this.portfolioWebsite);

      const updateEmployeeStatus = await updateProfileData(
        this.authenticationStore.token,
        data,
        "employee"
      );

      if (updateEmployeeStatus === 200) {
        this.alert = true;
        this.alertMessage = "Data updated successfully";
        this.alertBackgroundColor = "alert alert-success";
        this.authenticationStore.setIfEmployeeProfileCompleted(true);
      } else {
        this.alert = true;
        this.alertMessage = " Error occur while updating data";
        this.alertBackgroundColor = "alert alert-danger";
      }

      this.authenticationStore.getAccountPictures();
    },
    async uploadFiles() {
      // Upload Resume and employee Picture varaibles
      let uploadResumeCheck = false;
      let uploademployeePictureCheck = false;

      const Resumedata = new FormData();
      const PictureData = new FormData();

      // Check if resume is typeof file
      if (this.resume === null) {
        Resumedata.append("resume", "");
      } else if (typeof this.resume === "object") {
        Resumedata.append("resume", this.resume);
        uploadResumeCheck = true;
      } else {
        Resumedata.append("resume", "");
      }

      // Check if employee picture is typeof file
      if (this.employeePicture === null) {
        PictureData.append("profile_picture", "");
      } else if (typeof this.employeePicture === "object") {
        PictureData.append("profile_picture", this.employeePicture);
        uploademployeePictureCheck = true;
      } else {
        PictureData.append("profile_picture", "");
      }

      if (uploadResumeCheck) {
        console.log("resume");
        console.log(this.resume);
        console.log(Resumedata);
        const updateEmployeeResume = await uploadEmployeeResume(
          this.authenticationStore.token,
          Resumedata
        );

        if (updateEmployeeResume) {
          this.alert = true;
          this.alertMessage = "Files uploaded successfully";
          this.alertBackgroundColor = "alert alert-success";

          if (updateEmployeeResume.resume) {
            this.resume = this.getFileBaseName(updateEmployeeResume.resume);
            this.resumeuploadedCheck = true;
          }
          this.resumeUploadShow = false;
        } else {
          this.alert = true;
          this.alertMessage = " Error occur while uploading files";
          this.alertBackgroundColor = "alert alert-danger";
        }
      }
      if (uploademployeePictureCheck) {
        console.log("picture");
        console.log(this.employeePicture);
        console.log(PictureData);
        const updateEmployeePicture = await uploadProfilePicture(
          this.authenticationStore.token,
          PictureData,
          "employee"
        );

        console.log("updateEmployeePicture : ", updateEmployeePicture);

        if (updateEmployeePicture) {
          console.log(updateEmployeePicture);
          this.alert = true;
          this.alertMessage = "Files uploaded successfully";
          this.alertBackgroundColor = "alert alert-success";

          if (updateEmployeePicture.profile_picture) {
            this.employeePicture = this.getFileBaseName(
              updateEmployeePicture.profile_picture
            );
          }
          this.PictureUploadShow = false;
          this.authenticationStore.getAccountPictures();
        } else {
          this.alert = true;
          this.alertMessage = " Error occur while uploading files";
          this.alertBackgroundColor = "alert alert-danger";
        }
      }
    },
    downloadResume() {
      // get the download link from server
      this.authenticationStore.getResumePathToDownload();
      console.log(
        "resumePath : ",
        this.authenticationStore.resumePathToDownload
      );
      const downloadUrl = this.authenticationStore.getResumePathToDownloadUrl;

      if (downloadUrl) {
        // download the file
        window.open(downloadUrl, "_blank");
      }
    },
  },
};
</script>
