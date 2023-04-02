import axios from "axios";
import { API } from "@/api";

export const getCompanyData = async (token) => {
  const headers = {
    "content-type": "application/json",
    Authorization: `Bearer ${token}`,
  };

  try {
    const response = await axios.get(API.company.details, { headers: headers });
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.log(error);
    return null;
  }
};
