<template>
  <div class="container p-4">
    <div class="row">
      <div class="row pb-3">
        <div class="container-fluid">
          <div class="row">
            <company-card
              :companyName="companyName"
              :companySize="companySize"
              :companyLocation="companyLocation"
              :companyWebsite="companyWebsite"
              :companyLogoPath="this.authenticationStore.companyProfileLogo"
            />
            <div class="col-xl-8 order-xl-1">
              <vee-form
                action="#"
                :validation-schema="schema"
                @submit="updateCompanyData"
                class="card border-0 text-center text-md-start"
              >
                <div class="card-body">
                  <shared-component-alert-item
                    :alert="alert"
                    :alertBackgroundColor="alertBackgroundColor"
                    :alertMessage="alertMessage"
                    @closeAlert="closeAlert"
                  />
                  <h2 class="text-center form-header">Company Information</h2>
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
                            class="error-message small font-italic"
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
                            class="error-message small font-italic"
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
                            class="error-message small font-italic"
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
                            class="error-message small font-italic"
                          />
                        </div>
                      </div>
                    </div>
                    <button type="submit" class="btn button button-primary">
                      Save all
                    </button>
                    <hr />
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
                            class="btn button btn-outline-primary my-3"
                            type="button"
                            v-if="!logoUploadShow"
                            @click.prevent="logoUploadShow = true"
                          >
                            Click to drag your Company logo
                          </button>
                          <company-logo-upload
                            v-else
                            @upload="upload"
                            @closeUploadModel="CloseUploadModel"
                          />
                        </div>
                        <button
                          class="btn button button-primary my-2"
                          @click.prevent="uploadCompanyLogo"
                        >
                          Upload Company Logo
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
import CompanyCard from "@/components/companyComponents/CompanyCard.vue";
import CompanyLogoUpload from "./companyComponents/CompanyLogoUpload.vue";
import { getCompanyData } from "@/services/companyService";
import { getAuthenticationStore } from "@/services/authService";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "CompanyDataItem",
  async created() {
    this.authenticationStore = getAuthenticationStore();
    const companyData = await getCompanyData(this.authenticationStore.token);
    console.log(companyData);

    if (companyData) {
      this.companyName = companyData.company_name;
      this.companySize = companyData.company_size;
      this.companyLocation = companyData.company_location;
      this.companyWebsite = companyData.company_website;
      if (companyData.company_logo) {
        this.companyLogo = companyData.company_logo;
      }
    } else if (companyData == null) {
      this.alert = true;
      this.alertMessage = " Error occur while fetching data";
      this.alertBackgroundColor = "alert alert-danger";
    }
  },
  data() {
    return {
      // Create schema for form validation
      schema: {
        company_name: "required|min:5|max:40",
        company_size: "required|min:1|max:40",
        company_website: "required|url",
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
      companyLogo: "",

      // Authentication store
      authenticationStore: {},
    };
  },
  components: {
    CompanyLogoUpload,
    CompanyCard,
  },
  methods: {
    getFileBaseName(path) {
      return path.split("/").reverse()[0];
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

      axios
        .patch(API.company.details, data, { headers: headers })
        // eslint-disable-next-line no-unused-vars
        .then((response) => {
          // show that the data is updated
          this.alert = true;
          this.alertMessage = "Data updated successfully";
          this.alertBackgroundColor = "alert alert-success";

          this.authenticationStore.setIfCompanyProfileCompleted(true);
        })
        // eslint-disable-next-line no-unused-vars
        .catch((error) => {
          this.alert = true;
          this.alertMessage = " Error occur while updating data";
          this.alertBackgroundColor = "alert alert-danger";
        });
    },
    async uploadCompanyLogo() {
      // varaiable to check if logo is uploaded
      let uploadLogo = false;

      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      const data = new FormData();

      // Check if resume is typeof file
      if (this.companyLogo === null) {
        data.append("company_logo", "");
      } else if (typeof this.companyLogo === "object") {
        data.append("company_logo", this.companyLogo);
        uploadLogo = true;
      } else {
        data.append("company_logo", "");
      }

      if (uploadLogo) {
        console.log("uploadLogoStart");
        await axios
          .put(API.company.company_profile_logo, data, {
            headers: headers,
          })
          .then((response) => {
            // show that the data is updated
            this.alert = true;
            this.alertMessage = "Logo uploaded successfully";
            this.alertBackgroundColor = "alert alert-success";

            console.log(response.data);
            this.logoUploadShow = false;
            this.authenticationStore.getAccountPictures();
            if (response.data.company_logo) {
              this.companyLogo = this.getFileBaseName(
                response.data.company_logo
              );
            }
          })
          // eslint-disable-next-line no-unused-vars
          .catch((error) => {
            this.alert = true;
            this.alertMessage = " Error occur while updating data";
            this.alertBackgroundColor = "alert alert-danger";
          });
      }
    },
  },
};
</script>
