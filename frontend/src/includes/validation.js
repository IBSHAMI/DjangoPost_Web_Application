import {
  Form as VeeForm,
  Field as VeeField,
  defineRule,
  ErrorMessage,
  configure,
} from "vee-validate";
import {
  required,
  min,
  max,
  alpha_spaces as alphaSpaces,
  email,
  confirmed,
  url,
  not_one_of as excluded,
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
    defineRule("required_terms", required);
    defineRule("min", min);
    defineRule("max", max);
    defineRule("alpha_spaces", alphaSpaces);
    defineRule("email", email);
    defineRule("confirmed", confirmed);
    defineRule("excluded_password", excluded);
    defineRule("url", url);

    // a global config object for all defined rules
    configure({
      // ctx is the context object contains the following properties
      // { form, field, formState }
      generateMessage: (ctx) => {
        const messages = {
          required: `The ${ctx.field} is required`,
          min: `The ${ctx.field} length is too short`,
          max: `The ${ctx.field} length is too long`,
          alpha_spaces: `The ${ctx.field} may only contain alphabetic characters and spaces`,
          email: `The ${ctx.field} must be a valid email`,
          confirmed: `The ${ctx.field} confirmation does not match`,
          excluded: `The ${ctx.field} is not allowed`,
          excluded_password: `The ${ctx.field} is an easy password`,
          required_terms: `You must agree to the terms and conditions`,
          url: `The ${ctx.field} must be a valid URL`,
        };
        const message = messages[ctx.rule.name]
          ? messages[ctx.rule.name]
          : `The ${ctx.field} is invalid`;

        return message;
      },
    });
  },
};
