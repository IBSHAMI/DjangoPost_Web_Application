import { Form as VeeForm, Field as VeeField } from "vee-validate";

// register a custom plugin,
// Vue will run the install function before mounting the app
export default {
  // install function is called by Vue.use()
  // install accept 2 arguments,
  // app:  the first is the Vue constructor
  // options: the second is an object with options
  install(app) {
    app.component("VeeForm", VeeForm);
    app.component("VeeField", VeeField);
  },
};
