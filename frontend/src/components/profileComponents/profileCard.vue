<template>
  <div class="col-xl-4 order-xl-1">
    <div class="card border-0 text-center p-0">
      <div class="card-body pb-5">
        <img
          :src="employeeProfilePicture"
          class="img-fluid avatar-xl rounded-circle mx-auto mt-n7 mb-4"
          alt="employee picture"
          style="width: 200px; height: 200px"
        />
        <h4 class="h3">{{ fullName }}</h4>
        <h5 class="fw-normal">Senior Software Engineer</h5>
        <p class="text-gray mb-4">New York, USA</p>
        <a
          class="btn button btn-sm btn-gray-800 d-inline-flex align-items-center me-2"
          href="#"
          ><svg
            class="icon icon-xs me-1"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M8 9a3 3 0 100-6 3 3 0 000 6zM8 11a6 6 0 016 6H2a6 6 0 016-6zM16 7a1 1 0 10-2 0v1h-1a1 1 0 100 2h1v1a1 1 0 102 0v-1h1a1 1 0 100-2h-1V7z"
            ></path>
          </svg>
          Connect </a
        ><a class="btn button btn-sm btn-secondary" href="#">Send Message</a>
      </div>
    </div>
  </div>
</template>

<script>
import useAuthenticationStore from "@/stores/authentication";

export default {
  name: "ProfileCard",
  props: ["fullName"],
  setup() {
    const authenticationStore = useAuthenticationStore();
    return { authenticationStore };
  },
  data() {
    return {
      employeeProfilePicture: "",
    };
  },
  mounted() {
    this.getEmployeeProfilePicture();
  },
  methods: {
    getEmployeeProfilePicture() {
      if (this.authenticationStore.employeeProfilePicture.profile_picture) {
        this.employeeProfilePicture =
          this.authenticationStore.employeeProfilePicture.profile_picture;
      }
    },
  },
};
</script>

<style></style>
