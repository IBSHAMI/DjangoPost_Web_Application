import axios from "axios";
import { API } from "@/api";

const setHeaders = (token) => {
  return {
    Authorization: `Bearer ${token}`,
  };
};

export const uploadEmployeeResume = async (token, resume) => {
  const headers = setHeaders(token);
  const apiUrl = API.employee.employee_profile_resume;

  try {
    const response = await axios.put(apiUrl, resume, {
      headers: headers,
    });
    return response.data;
  } catch (error) {
    console.log(error);
    return null;
  }
};
