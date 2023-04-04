import { defineStore } from "pinia";
import { fetchDataWithToken } from "@/services/apiService";
import { API } from "@/api";

export default defineStore("authentication", {
  // We use state object to create gloabl state
  state: () => ({
    token: null,
    user: null,
    employeeProfileCompleted: false,
    companyProfileCompleted: false,
    employeeProfilePicture: null,
    companyProfileLogo: null,
    resumePathToDownload: null,
    isAuthenticated: false,
  }),
  // getters is like computed properties in Vue
  getters: {
    getResumePathToDownloadUrl() {
      return this.resumePathToDownload;
    },
  },
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
    setIfEmployeeProfileCompleted(employeeProfileCompleted) {
      this.$patch({ employeeProfileCompleted: employeeProfileCompleted });
    },
    setIfCompanyProfileCompleted(companyProfileCompleted) {
      this.$patch({ companyProfileCompleted: companyProfileCompleted });
    },
    setEmployeeProfilePicture(employeeProfilePicture) {
      this.$patch({ employeeProfilePicture: employeeProfilePicture });
    },
    setCompanyProfileLogo(companyProfileLogo) {
      this.$patch({ companyProfileLogo: companyProfileLogo });
    },
    setResumePathToDownload(resumePathToDownload) {
      this.$patch({ resumePathToDownload: resumePathToDownload });
    },
    async getAccountPictures() {
      const employeeProfilePicUrl = API.employee.employee_profile_picture;
      const companyProfileLogoUrl = API.company.company_profile_logo;

      const employeeProfilePic = await fetchDataWithToken(
        employeeProfilePicUrl,
        this.token
      );

      if (employeeProfilePic) {
        this.setEmployeeProfilePicture(employeeProfilePic.profile_picture);
      }

      const companyProfileLogo = await fetchDataWithToken(
        companyProfileLogoUrl,
        this.token
      );

      if (companyProfileLogo) {
        this.setCompanyProfileLogo(companyProfileLogo.company_logo);
      }
    },
    async checkIfProfileComplete() {
      const url = API.auth.checkIfProfileComplete;
      const profileCompleteCheck = await fetchDataWithToken(url, this.token);

      if (profileCompleteCheck) {
        this.setIfEmployeeProfileCompleted(
          profileCompleteCheck.employee_profile_complete
        );
        this.setIfCompanyProfileCompleted(
          profileCompleteCheck.company_profile_complete
        );
      }
    },

    async getResumePathToDownload() {
      const url = API.employee.employee_profile_resume;
      const resumePathToDownload = await fetchDataWithToken(url, this.token);

      if (resumePathToDownload) {
        this.setResumePathToDownload(resumePathToDownload.resume);
      }
    },
    logout() {
      localStorage.removeItem("Bearer");
      localStorage.removeItem("user");
      this.$patch({ token: null, user: null, isAuthenticated: false });
    },
  },
});
