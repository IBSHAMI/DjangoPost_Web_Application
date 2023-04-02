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
import useAuthenticationStore from "@/stores/authentication";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "ProfileContactItem",
  created() {
    this.getUserDate();
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

      schema: {
        first_name: "required",
        last_name: "required",
        email: "required|email",
        message: "required",
      },
    };
  },
  setup() {
    // init the store
    const authenticationStore = useAuthenticationStore();
    return { authenticationStore };
  },
  methods: {
    getUserDate() {
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
        })
        // eslint-disable-next-line no-unused-vars
        .catch((error) => {
          console.log(error);
        });
    },
    closeAlert() {
      this.alert = false;
      this.alertBackgroundColor = "";
      this.alertMessage = "";
    },
    contactSupport() {
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      const data = {
        first_name: this.firstName,
        last_name: this.lastName,
        email: this.email,
        message: this.message,
      };

      axios
        .post(API.employee.contact_support, data, { headers: headers })
        // eslint-disable-next-line no-unused-vars
        .then((response) => {
          this.alert = true;
          this.alertBackgroundColor = "alert alert-success";
          this.alertMessage = "Message sent successfully";
        })
        // eslint-disable-next-line no-unused-vars
        .catch((error) => {
          this.alert = true;
          this.alertBackgroundColor = "alert alert-danger";
          this.alertMessage = "Something went wrong, try again later";
        });
    },
  },
};
</script>

<style></style>
