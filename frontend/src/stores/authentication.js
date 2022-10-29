import { defineStore } from "pinia";

export default defineStore("authentication", {
  // We use state object to create gloabl state
  state: () => ({
    token: null,
    user: null,
    isAuthenticated: false,
  }),
  // actions is like methods in Vue
  actions: {
    // initialize is called when the store is created
    initializeStore() {
      if (localStorage.getItem("Bearer")) {
        this.$patch({
          token: localStorage.getItem("Bearer"),
          isAuthenticated: true,
        });
      } else {
        this.$patch({ token: null, isAuthenticated: false });
      }
    },
    setToken(token) {
      this.$patch({ token: token, isAuthenticated: true });
      // set token in local storage
      localStorage.setItem("Bearer", token);
    },
    setUser(user) {
      this.$patch({ user: user });
    },
    logout() {
      this.$patch({ token: null, user: null, isAuthenticated: false });
    },
  },
});
