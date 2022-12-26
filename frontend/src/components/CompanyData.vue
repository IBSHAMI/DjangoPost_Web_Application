<template>
  <div class="container py-4 my-4">
    <div class="row">
      <div class="row pb-3">
        <div class="container-fluid">
          <div class="row">
            <company-card :company="companyName" />
            <div class="col-xl-8 order-xl-1">
              <vee-form
                action="#"
                :validation-schema="schema"
                @submit="updateCompanyData"
                class="card shadow border-0 text-center text-md-start"
              >
                <div class="card-body">
                  <alert-item
                    :alert="alert"
                    :alertBackgroundColor="alertBackgroundColor"
                    :alertMessage="alertMessage"
                    @closeAlert="closeAlert"
                  />
                  <h2 class="text-start h5 mb-2 px-2">Company Information</h2>
                  <div class="card-body px-2">
                    <div class="row py-2">
                      <div class="form-group col-md-6 mb-3">
                        <label for="company_name" class="form-label fst-italic"
                          >Company name</label
                        >
                        <div>
                          <vee-field
                            type="text"
                            name="company_name"
                            id="company_name"
                            class="form-control"
                            v-model="companyName"
                          />
                          <ErrorMessage
                            name="company_name"
                            class="text-danger small font-italic"
                          />
                        </div>
                      </div>
                      <div class="form-group col-md-6 mb-3">
                        <label for="company_size" class="form-label fst-italic"
                          >Company size</label
                        >
                        <div>
                          <vee-field
                            type="text"
                            name="company_size"
                            id="company_size"
                            class="form-control"
                            v-model="companySize"
                          />
                          <ErrorMessage
                            name="company_size"
                            class="text-danger small font-italic"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="row py-2">
                      <div class="form-group col-md-6 mb-3">
                        <label
                          for="company_location"
                          class="form-label fst-italic"
                          >Company Location</label
                        >
                        <div>
                          <vee-field
                            type="text"
                            name="company_location"
                            id="company_location"
                            class="form-control"
                            v-model="companyLocation"
                          />
                          <ErrorMessage
                            name="company_location"
                            class="text-danger small font-italic"
                          />
                        </div>
                      </div>
                      <div class="form-group col-md-6 mb-3">
                        <label
                          for="company_website"
                          class="form-label fst-italic"
                          >Company Website</label
                        >
                        <div>
                          <vee-field
                            type="text"
                            name="company_website"
                            id="company_website"
                            class="form-control"
                            v-model="companyWebsite"
                          />
                          <ErrorMessage
                            name="company_website"
                            class="text-danger small font-italic"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="row py-2">
                      <div class="form-group col-md-12 mb-6">
                        <label
                          for="company_description"
                          class="form-label fst-italic"
                          >Company Description</label
                        >

                        <div class="w-full h-full relative mt-1 py-2">
                          <vee-field
                            as="textarea"
                            id="company_description"
                            name="company_description"
                            rows="6"
                            class="form-control"
                            v-model="companyDescription"
                          ></vee-field>
                          <ErrorMessage
                            name="company_description"
                            class="text-danger small font-italic"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="row py-2">
                      <div class="form-group col-md-12 mb-6">
                        <label class="form-label fst-italic"
                          >Upload Company logo</label
                        >
                        <div class="mt-1 py-2">
                          <div v-show="!logoUploadShow">
                            {{ companyLogo }}
                          </div>
                          <button
                            class="btn btn-outline-primary my-3"
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
                  </div>
                  <button type="submit" class="btn btn-primary">Save</button>
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
import CompanyCard from "@/components/companyComponents/CompanyCard.vue";
import CompanyLogoUpload from "./companyComponents/CompanyLogoUpload.vue";
import AlertItem from "@/components/sharedComponents/AlertItem.vue";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "CompanyDataItem",
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
        company_name: "required|min:5|max:40",
        company_size: "required|min:1|max:40",
        company_website: "required|url",
        company_description: "required|min:5|max:1000",
        company_location: "required|min:2|max:40",
      },

      // Upload Resume and Profile Picture varaibles
      logoUploadShow: false,

      // Upload alert
      alert: false,
      alertBackgroundColor: "",
      alertMessage: "",

      companyName: "",
      companySize: "",
      companyLocation: "",
      companyWebsite: "",
      companyDescription: "",
      companyLogo: "",
    };
  },
  components: {
    CompanyLogoUpload,
    AlertItem,
    CompanyCard,
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
        Authorization: token,
      };

      axios
        .get(API.company.details, { headers: headers })
        .then((response) => {
          this.companyName = response.data.company_name;
          this.companySize = response.data.company_size;
          this.companyLocation = response.data.company_location;
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
          this.alertBackgroundColor = "alert alert-danger";
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
      console.log("updateCompanyData");
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      const data = new FormData();
      data.append("company_name", this.companyName);
      data.append("company_size", this.companySize);
      data.append("company_location", this.companyLocation);
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
