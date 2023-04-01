<template>
  <div class="container p-4">
    <div class="row">
      <div class="row pb-3">
        <div class="container-fluid">
          <div class="row">
            <!-- center the div on screen-->
            <div class="col-xl-8 mx-auto">
              <vee-form
                action="#"
                :validation-schema="schema"
                @submit="createJob"
                class="card border-0 text-center text-md-start"
              >
                <div class="card-body">
                  <alert-item
                    :alert="alert"
                    :alertBackgroundColor="alertBackgroundColor"
                    :alertMessage="alertMessage"
                    @closeAlert="closeAlert"
                  />
                  <h2 class="text-center h2 fw-bold my-2 px-2">Post a Job</h2>
                  <p class="text-center py-3 mx-4 paragraph">
                    You know what you are looking for. We help you find them.
                    Post your open positions and hire fast the best talent.
                  </p>
                  <div class="card-body px-2">
                    <div class="row py-2">
                      <div class="form-group col-md-6 mb-3">
                        <label
                          for="position_title"
                          class="form-label fst-italic"
                          >Position Title</label
                        >
                        <div>
                          <vee-field
                            type="text"
                            name="position_title"
                            id="position_title"
                            class="form-control"
                            v-model="positionTitle"
                          />
                          <ErrorMessage
                            name="position_title"
                            class="error-message small font-italic"
                          />
                        </div>
                      </div>
                      <div class="form-group col-md-6 mb-3">
                        <label for="position_type" class="form-label fst-italic"
                          >Position Type</label
                        >
                        <div>
                          <vee-field
                            as="select"
                            name="position_type"
                            id="position_type"
                            class="form-control"
                            v-model="positionType"
                          >
                            <option
                              v-for="(type, index) in JobTypes"
                              :key="index"
                              :value="type"
                            >
                              {{ type }}
                            </option>
                          </vee-field>
                          <ErrorMessage
                            name="position_type"
                            class="error-message small font-italic"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="row py-2">
                      <div class="form-group col-md-6 mb-3">
                        <label
                          for="position_location"
                          class="form-label fst-italic"
                          >Position Location</label
                        >
                        <div>
                          <vee-field
                            as="select"
                            name="position_location"
                            id="position_location"
                            class="form-control"
                            v-model="positionLocation"
                          >
                            <option
                              v-for="(type, index) in JobLocations"
                              :key="index"
                              :value="type"
                            >
                              {{ type }}
                            </option>
                          </vee-field>
                          <ErrorMessage
                            name="position_location"
                            class="error-message small font-italic"
                          />
                        </div>
                      </div>

                      <div class="form-group col-md-6 mb-3">
                        <label for="language" class="form-label fst-italic"
                          >Language Required</label
                        >
                        <div>
                          <vee-field
                            as="select"
                            name="language"
                            id="language"
                            class="form-control"
                            v-model="languageRequired"
                          >
                            <option
                              v-for="(type, index) in Languages"
                              :key="index"
                              :value="type"
                            >
                              {{ type }}
                            </option>
                          </vee-field>
                          <ErrorMessage
                            name="language"
                            class="error-message small font-italic"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="row py-2">
                      <div class="form-group col-md-6 mb-3">
                        <label
                          for="positions_number"
                          class="form-label fst-italic"
                          >Number of positions
                        </label>
                        <div>
                          <vee-field
                            type="number"
                            name="positions_number"
                            id="positions_number"
                            class="form-control"
                            v-model="positionsNumber"
                          />
                          <ErrorMessage
                            name="positions_number"
                            class="error-message small font-italic"
                          />
                        </div>
                      </div>
                      <div class="form-group col-md-6 mb-3">
                        <label for="salary" class="form-label fst-italic"
                          >Monthly Salary (USD)
                        </label>
                        <div class="input-group-prepend">
                          <vee-field
                            as="select"
                            name="salary"
                            id="salary"
                            class="form-control"
                            v-model="salary"
                          >
                            <option
                              v-for="(type, index) in JobsSalary"
                              :key="index"
                              :value="type"
                            >
                              {{ type }}
                            </option>
                          </vee-field>

                          <ErrorMessage
                            name="salary"
                            class="error-message small font-italic"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="row py-2">
                      <div class="form-group col-md-6 mb-3">
                        <label
                          for="position_experience"
                          class="form-label fst-italic"
                          >Years of Experience Required</label
                        >
                        <div>
                          <vee-field
                            as="select"
                            name="position_experience"
                            id="position_experience"
                            class="form-control"
                            v-model="positionExperience"
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
                      <div class="form-group col-md-6 mb-3">
                        <label for="framework" class="form-label fst-italic"
                          >FrameWork
                        </label>
                        <div class="input-group-prepend">
                          <vee-field
                            as="select"
                            name="framework"
                            id="framework"
                            class="form-control"
                            v-model="framework"
                          >
                            <option
                              v-for="(framework, index) in frameworks"
                              :key="index"
                              :value="framework"
                            >
                              {{ framework }}
                            </option>
                          </vee-field>
                          <ErrorMessage
                            name="framework"
                            class="error-message small font-italic"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="row py-2">
                      <div class="form-group col-md-12 mb-6">
                        <label
                          for="job_description"
                          class="form-label fst-italic"
                          >Job description</label
                        >
                        <ErrorMessage
                          name="job_description"
                          class="error-message small font-italic"
                        />
                        <div>
                          <vee-field
                            as="textarea"
                            id="job_description"
                            name="job_description"
                            rows="6"
                            class="form-control textarea"
                            v-model="jobDescription"
                          ></vee-field>
                        </div>
                      </div>
                    </div>
                    <div class="row py-2">
                      <div class="form-check col-md-12 mb-6">
                        <div class="m-3">
                          <vee-field
                            id="remote"
                            aria-describedby="remote"
                            type="checkbox"
                            class="form-check-input"
                            name="remote"
                            v-model="remote"
                            :value="true"
                          />
                          <ErrorMessage
                            name="remote"
                            class="error-message small font-italic"
                          />
                          <label for="remote" class="form-label fst-italic"
                            >Remote</label
                          >
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="text-center">
                    <button
                      type="submit"
                      class="btn button button-primary my-2"
                    >
                      Create Job
                    </button>
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
import useAuthenticationStore from "@/stores/authentication";
import AlertItem from "@/components/sharedComponents/AlertItem.vue";
import axios from "axios";
import { API } from "@/api";

export default {
  name: "CreateJobFormItem",
  setup() {
    // init the store
    const authenticationStore = useAuthenticationStore();
    return { authenticationStore };
  },
  created() {
    this.getChoicesData();
  },
  data() {
    return {
      // Alert varaibles
      alert: false,
      alertMessage: "",
      alertBackgroundColor: "",

      // schema for the form
      schema: {
        position_title: "required|min:10|max:100",
        position_type: "required|min:3|max:100",
        framework: "required|min:3|max:100",
        position_location: "required|min:2|max:100",
        language: "required|min:2|max:100",
        positions_number: "required",
        salary: "required",
        position_experience: "",
        job_description: "required|min:1|max:1000",
        remote: "",
      },

      // form data
      positionTitle: "",
      positionType: "",
      framework: "",
      positionLocation: "",
      languageRequired: "",
      positionsNumber: "",
      salary: "",
      positionExperience: "",
      jobDescription: "",
      remote: false,

      // choices data
      JobTypes: [],
      frameworks: [],
      JobLocations: [],
      Languages: [],
      JobExperience: [],
      JobsSalary: [],
    };
  },
  components: {
    AlertItem,
  },
  methods: {
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
          this.JobTypes = response.data.job_type_choices;
          this.JobLocations = response.data.job_location_choices;
          this.Languages = response.data.job_language_choices;
          this.JobExperience = response.data.job_experience_choices;
          this.JobsSalary = response.data.job_salary_choices;
          this.frameworks = response.data.framework_choices;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    closeAlert() {
      this.alert = false;
      this.alertBackgroundColor = "";
      this.alertMessage = "";
    },
    createJob() {
      const token = `Bearer ${this.authenticationStore.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };
      const createJobUrl = API.jobs.create;

      const data = new FormData();

      data.append("title", this.positionTitle);
      data.append("type", this.positionType);
      data.append("framework", this.framework);
      data.append("location", this.positionLocation);
      data.append("language", this.languageRequired);
      data.append("number_of_positions", this.positionsNumber);
      data.append("salary", this.salary);
      data.append("experience", this.positionExperience);
      data.append("description", this.jobDescription);
      if (this.remote) {
        data.append("remote", this.remote);
      }

      console.log(data);

      axios
        .post(createJobUrl, data, { headers: headers })
        .then((response) => {
          if (response.status === 201) {
            this.alert = true;
            this.alertMessage = "Job created successfully";
            this.alertBackgroundColor = "alert alert-success";
            setTimeout(() => {
              this.$router.push({ name: "Company", params: { slug: "jobs" } });
            }, 2000);
          }
        })
        .catch((error) => {
          console.log(error);
          this.alert = true;
          this.alertMessage = "Error creating job";
          this.alertBackgroundColor = "alert alert-danger";
        });
    },
  },
};
</script>

<style scoped>
.form-check input[type="checkbox"] + .form-check-label::after {
  opacity: 0;
}
.form-check.square-check .form-check-label::after {
  border-radius: 2px;
}
.form-check .form-check-label::after {
  content: "\f00c";
  font-family: "Font Awesome 5 Free";
  top: 0;
  text-align: center;
  opacity: 0;
  color: #31344b;
  font-weight: 900;
  border: 0;
}

.form-check {
  position: relative;
  display: block;
  padding-left: 1.25rem;
}

.paragraph {
  font: italic 500 20px/2em var(--Nunito);
  font-size: 1.2rem;
  line-height: 1.5;
  color: var(--primary-color-1);
}
</style>
