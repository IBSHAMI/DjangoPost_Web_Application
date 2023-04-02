import {
  fetchDataWithToken,
  updateDataWithToken,
  uploadDataWithToken,
} from "./apiService";
import { API } from "@/api";

const getAPIUrl = (profileType, isUpload) => {
  let baseURL = null;
  if (profileType === "employee") {
    if (isUpload) {
      baseURL = API.employee.employee_profile_picture;
    } else {
      baseURL = API.employee.details;
    }
  } else if (profileType === "company") {
    baseURL = API.company.company_profile_logo;
    if (isUpload) {
      baseURL = API.company.company_profile_logo;
    } else {
      baseURL = API.company.details;
    }
  }
  return baseURL;
};

export const getProfileData = async (token, profileType) => {
  const apiUrl = getAPIUrl(profileType, false);
  return await fetchDataWithToken(apiUrl, token);
};

export const updateProfileData = async (token, data, profileType) => {
  const apiUrl = getAPIUrl(profileType, false);
  return await updateDataWithToken(apiUrl, data, token);
};

export const uploadProfilePicture = async (token, picture, profileType) => {
  const apiUrl = getAPIUrl(profileType, true);
  return await uploadDataWithToken(apiUrl, picture, token);
};

export const getChoicesData = async (token) => {
  const apiUrl = API.jobs.get_choices_data;
  return await fetchDataWithToken(apiUrl, token);
};
