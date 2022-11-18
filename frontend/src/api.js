const baseURL = "http://127.0.0.1:8000";

export const API = {
  auth: {
    login: `${baseURL}/api/auth/token/login/`,
    logout: `${baseURL}/api/auth/token/logout/`,
    register: `${baseURL}/api/auth/users/`,
  },
  employee: {
    details: `${baseURL}/api/users/employee/data/`,
    contact_support: `${baseURL}/api/users/employee/contact-support/`,
  },
  company: {
    details: `${baseURL}/api/users/company/data/`,
    contact_support: `${baseURL}/api/users/company/contact-support/`,
  },
  jobs: `${baseURL}/api/jobs/`,
};
