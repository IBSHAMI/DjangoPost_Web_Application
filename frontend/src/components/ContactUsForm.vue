<template>
  <section class="container d-flex justify-content-center py-4 my-4">
    <div class="card w-75 border-0 text-center text-md-start">
      <div class="row card-title text-center">
        <h5 class="my-4 form-header">Contact Us</h5>
        <p class="para">
          Please contact us for any inqueries or questions you may have. We will
          get back to you as soon as possible.
        </p>
      </div>
      <div>
        <vee-form
          action="#"
          :validation-schema="schema"
          @submit="contactSupport"
          class=""
        >
          <div class="space-y-6 bg-white px-4 py-5 sm:p-6">
            <shared-component-alert-item
              :alert="alert"
              :alertBackgroundColor="alertBackgroundColor"
              :alertMessage="alertMessage"
              @closeAlert="closeAlert"
            />
            <div class="card-body">
              <div class="row py-2">
                <div class="form-group col-md-4 mb-3">
                  <label for="first_name" class="form-label fst-italic"
                    >First Name</label
                  >
                  <div>
                    <vee-field
                      type="text"
                      name="first_name"
                      id="first_name"
                      v-model="firstName"
                      class="form-control"
                    />
                    <ErrorMessage
                      name="first_name"
                      class="error-message small font-italic"
                    />
                  </div>
                </div>
                <div class="form-group col-md-4 mb-3">
                  <label for="last_name" class="form-label fst-italic"
                    >Last name</label
                  >
                  <div>
                    <vee-field
                      type="text"
                      id="last_name"
                      name="last_name"
                      v-model="lastName"
                      class="form-control"
                    />
                    <ErrorMessage
                      name="last_name"
                      class="error-message small font-italic"
                    />
                  </div>
                </div>
                <div class="form-group col-md-4 mb-3">
                  <label for="email" class="form-label fst-italic">Email</label>
                  <div>
                    <vee-field
                      type="text"
                      id="email"
                      name="email"
                      v-model="email"
                      class="form-control"
                    />
                    <ErrorMessage
                      name="email"
                      class="error-message small font-italic"
                    />
                  </div>
                </div>
              </div>
              <div class="form-group col-md-12 mb-3">
                <div class="relative">
                  <label for="message" class="form-label fst-itali"
                    >Message</label
                  >
                  <vee-field
                    as="textarea"
                    id="message"
                    name="message"
                    rows="5"
                    v-model="message"
                    class="form-control textarea"
                  ></vee-field>
                  <ErrorMessage
                    name="message"
                    class="error-message small font-italic"
                  />
                </div>
              </div>
            </div>
            <button type="submit" class="btn button btn-lg button-primary mx-4">
              Submit
            </button>
          </div>
        </vee-form>
      </div>
    </div>
  </section>
</template>

<script>
import { getAuthenticationStore } from "@/services/authService";
import { getProfileData } from "@/services/profileService";
import { postDataWithToken } from "@/services/apiService";
import { API } from "@/api";

export default {
  name: "EmployeeContactItem",
  async created() {
    this.authenticationStore = getAuthenticationStore();
    await this.getUserDate();
  },
  data() {
    return {
      firstName: "",
      lastName: "",
      email: "",
      message: "",

      // Upload alert
      alert: false,
      alertBackgroundColor: "",
      alertMessage: "",

      // authentication store
      authenticationStore: null,

      schema: {
        first_name: "required",
        last_name: "required",
        email: "required|email",
        message: "required",
      },
    };
  },
  methods: {
    async getUserDate() {
      const employeeData = await getProfileData(
        this.authenticationStore.token,
        "employee"
      );
      if (employeeData) {
        this.firstName = employeeData.first_name;
        this.lastName = employeeData.last_name;
        this.email = employeeData.email;
      }
    },
    closeAlert() {
      this.alert = false;
      this.alertBackgroundColor = "";
      this.alertMessage = "";
    },
    contactSupport() {
      const url = API.employee.contact_support;
      const data = {
        first_name: this.firstName,
        last_name: this.lastName,
        email: this.email,
        message: this.message,
      };
      const contactSupport = postDataWithToken(
        url,
        data,
        this.authenticationStore.token
      );

      if (contactSupport) {
        this.alert = true;
        this.alertBackgroundColor = "alert alert-success";
        this.alertMessage = "Message sent successfully";
      } else {
        this.alert = true;
        this.alertBackgroundColor = "alert alert-danger";
        this.alertMessage = "Something went wrong, try again later";
      }
    },
  },
};
</script>

<style></style>
