import { defineStore } from "pinia";

export default defineStore("company_employee_sections", {
  // We use state object to create gloabl state
  state: () => ({
    isEmployee: true,
    isCompanyVerified: false,
  }),
  // actions is like methods in Vue
  actions: {
    // initialize is called when the store is created
    initializeStore() {
      this.isEmployee = true;
    },
    switchAccountType() {
      this.isEmployee = !this.isEmployee;
    },
  },
});
