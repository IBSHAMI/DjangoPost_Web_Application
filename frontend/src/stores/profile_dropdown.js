import { defineStore } from "pinia";

export default defineStore("profileDropdown", {
  // We use state object to create gloabl state
  state: () => ({
    dropdownOpen: false,
  }),
  // actions is like methods in Vue
  actions: {
    // open or close dropdown
    toggleDropdown() {
      this.$patch({ dropdownOpen: !this.dropdownOpen });
    },
  },
});
