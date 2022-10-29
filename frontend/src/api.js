const baseURL = "http://127.0.0.1:8000";

export const API = {
  auth: {
    login: `${baseURL}/api/auth/token/login/`,
    logout: `${baseURL}/api/auth/token/logout/`,
  },
};
