const baseURL = "http://127.0.0.1:8000";

export const API = {
  auth: {
    login: `${baseURL}/api/auth/token/login/`,
    logout: `${baseURL}/api/auth/token/logout/`,
    register: `${baseURL}/api/auth/users/`,
    create_demo_user: `${baseURL}/api/users/create_demo_user/`,
    checkIfProfileComplete: `${baseURL}/api/users/check_if_profile_complete/`,
    get_webapp_status_data: `${baseURL}/api/users/get_webapp_status_data/`,
  },
  employee: {
    details: `${baseURL}/api/users/employee/data/`,
    contact_support: `${baseURL}/api/users/employee/contact-support/`,
    get_choices_data: `${baseURL}/api/users/employee/employee_choices/`,
    employee_profile_picture: `${baseURL}/api/users/employee/employee_profile_picture/`,
    employee_profile_resume: `${baseURL}/api/users/employee/employee_profile_resume/`,
    get_applicant_resume: `${baseURL}/api/users/employee/get_applicant_resume/`,
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
    apply_job: `${baseURL}/api/jobs/apply_job/`,
    applicants_list: `${baseURL}/api/jobs/applicants_list/`,
    update_application_status: `${baseURL}/api/jobs/update_application_status/`,
    get_job_title: `${baseURL}/api/jobs/get_job_title/`,
  },
};
