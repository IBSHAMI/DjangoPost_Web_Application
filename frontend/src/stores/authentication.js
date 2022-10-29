import { defineStore } from "pinia";

export default defineStore("authentication", {
  // We use state object to create gloabl state
  state: () => ({
    token: null,
    user: null,
    isAuthenticated: false,
  }),
  // actions is like methods in Vue
  mutations: {
    // initialize is called when the store is created
    initializeStore(state) {
      if (localStorage.getItem("Bearer")) {
        state.token = localStorage.getItem("Bearer");
        state.isAuthenticated = true;
      } else {
        state.token = null;
        state.isAuthenticated = false;
      }
    },
  },
});
