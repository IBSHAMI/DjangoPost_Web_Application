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
    get_choices_data: `${baseURL}/api/users/employee/employee_choices/`,
    get_employee_profile_picture: `${baseURL}/api/users/employee/employee_profile_picture/`,
  },
  company: {
    details: `${baseURL}/api/users/company/data/`,
    contact_support: `${baseURL}/api/users/company/contact-support/`,
    get_company_profile_logo: `${baseURL}/api/users/company/company_profile_logo/`,
  },
  jobs: {
    list: `${baseURL}/api/jobs/`,
    create: `${baseURL}/api/jobs/create/`,
    get_choices_data: `${baseURL}/api/jobs/job_choices/`,
  },
};
