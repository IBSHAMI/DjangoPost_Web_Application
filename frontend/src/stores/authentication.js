import { defineStore } from "pinia";

export default defineStore("authentication", {
  // We use state object to create gloabl state
  state: () => ({
    token: null,
    user: null,
    isAuthenticated: false,
  }),
  // // We use getters to create computed properties
  // getters: {
});
