import axios from "axios";
import { API } from "@/api";

const setHeaders = (token) => {
  return {
    Authorization: `Bearer ${token}`,
  };
};

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
  const headers = setHeaders(token);
  const apiUrl = getAPIUrl(profileType, false);

  try {
    const response = await axios.get(apiUrl, {
      headers: headers,
    });
    return response.data;
  } catch (error) {
    console.log(error);
    return null;
  }
};

export const updateProfileData = async (token, data, profileType) => {
  const headers = setHeaders(token);
  const apiUrl = getAPIUrl(profileType, false);

  try {
    const response = await axios.put(apiUrl, data, {
      headers: headers,
    });
    return response.status;
  } catch (error) {
    console.log(error);
    return null;
  }
};

export const uploadProfilePicture = async (token, picture, profileType) => {
  const headers = setHeaders(token);
  const apiUrl = getAPIUrl(profileType, true);

  console.log("apiUrl: ", apiUrl);

  try {
    const response = await axios.put(apiUrl, picture, {
      headers: headers,
    });
    return response.data;
  } catch (error) {
    console.log(error);
    return null;
  }
};
