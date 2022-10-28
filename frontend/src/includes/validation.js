import {
  Form as VeeForm,
  Field as VeeField,
  defineRule,
  ErrorMessage,
} from "vee-validate";
import {
  required,
  min,
  max,
  alpha_spaces as alphaSpaces,
  email,
  confirmed,
} from "@vee-validate/rules";

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
    app.component("ErrorMessage", ErrorMessage);

    defineRule("required", required);
    defineRule("min", min);
    defineRule("max", max);
    defineRule("alpha_spaces", alphaSpaces);
    defineRule("email", email);
    defineRule("confirmed", confirmed);
  },
};
