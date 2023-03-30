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
    employee_profile_picture: `${baseURL}/api/users/employee/employee_profile_picture/`,
    employee_profile_resume: `${baseURL}/api/users/employee/employee_profile_resume/`,
  },
  company: {
    details: `${baseURL}/api/users/company/data/`,
    contact_support: `${baseURL}/api/users/company/contact-support/`,
    company_profile_logo: `${baseURL}/api/users/company/company_profile_logo/`,
  },
  jobs: {
    list: `${baseURL}/api/jobs/`,
    get_total_jobs: `${baseURL}/api/jobs/get_total_jobs/`,
    company_list: `${baseURL}/api/jobs/company_job_list/`,
    detail: `${baseURL}/api/jobs/job_details/`,
    create: `${baseURL}/api/jobs/create/`,
    get_choices_data: `${baseURL}/api/jobs/job_choices/`,
    change_job_status: `${baseURL}/api/jobs/change_job_status/`,
    delete_job: `${baseURL}/api/jobs/delete_job/`,
    save_job: `${baseURL}/api/jobs/save_job/`,
    delete_saved_job: `${baseURL}/api/jobs/delete_saved_job/`,
  },
};
