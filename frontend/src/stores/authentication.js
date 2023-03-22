import { defineStore } from "pinia";
import { API } from "@/api";
import axios from "axios";

export default defineStore("authentication", {
  // We use state object to create gloabl state
  state: () => ({
    token: null,
    user: null,
    employeeProfilePicture: null,
    companyProfileLogo: null,
    isAuthenticated: false,
  }),
  // actions is like methods in Vue
  actions: {
    // initialize is called when the store is created
    initializeStore() {
      if (localStorage.getItem("Bearer")) {
        this.$patch({
          token: localStorage.getItem("Bearer"),
          user: localStorage.getItem("user"),
          isAuthenticated: true,
        });
      } else {
        this.$patch({ token: null, user: null, isAuthenticated: false });
      }
    },
    setToken(token) {
      this.$patch({ token: token, isAuthenticated: true });
      // set token in local storage
      localStorage.setItem("Bearer", token);
    },
    setUser(user) {
      this.$patch({ user: user });
      localStorage.setItem("user", user);
    },
    setEmployeeProfilePicture(employeeProfilePicture) {
      this.$patch({ employeeProfilePicture: employeeProfilePicture });
    },
    setCompanyProfileLogo(companyProfileLogo) {
      this.$patch({ companyProfileLogo: companyProfileLogo });
    },
    getAccountPictures() {
      // headers to retieve the account pictures
      const token = `Bearer ${this.token}`;
      // Add the token to the header as Bearer token
      const headers = {
        "content-type": "application/json",
        // eslint-disable-next-line prettier/prettier
        Authorization: token,
      };

      // get the employee profile picture
      axios
        .get(API.employee.employee_profile_picture, { headers: headers })
        .then((response) => {
          this.setEmployeeProfilePicture(response.data.profile_picture);
        })
        .catch((error) => {
          console.log(error);
        });

      // get the company logo
      axios
        .get(API.company.get_company_profile_logo, { headers: headers })
        .then((response) => {
          this.setCompanyProfileLogo(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    logout() {
      localStorage.removeItem("Bearer");
      localStorage.removeItem("user");
      this.$patch({ token: null, user: null, isAuthenticated: false });
    },
  },
});
