import axios from "axios";
import { API } from "@/api";

const setHeaders = (token) => {
  return {
    Authorization: `Bearer ${token}`,
  };
};

export const getCompanyData = async (token) => {
  const headers = setHeaders(token);

  try {
    const response = await axios.get(API.company.details, { headers: headers });
    return response.data;
  } catch (error) {
    console.log(error);
    return null;
  }
};

export const updateCompanyData = async (token, data) => {
  const headers = setHeaders(token);

  try {
    const response = await axios.put(API.company.details, data, {
      headers: headers,
    });
    return response.status;
  } catch (error) {
    console.log(error);
    return null;
  }
};

export const uploadCompanyLogo = async (token, logo) => {
  const headers = setHeaders(token);

  try {
    const response = await axios.put(API.company.company_profile_logo, logo, {
      headers: headers,
    });
    return response.data;
  } catch (error) {
    console.log(error);
    return null;
  }
};
