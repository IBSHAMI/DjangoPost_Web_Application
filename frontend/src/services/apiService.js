import axios from "axios";

export const setHeaders = (token) => {
  return {
    Authorization: `Bearer ${token}`,
  };
};

export const fetchData = async (url) => {
  try {
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.log(error);
    return null;
  }
};

export const fetchDataWithToken = async (url, token) => {
  const headers = setHeaders(token);
  try {
    const response = await axios.get(url, {
      headers: headers,
    });
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.log(error);
    return null;
  }
};

export const updateDataWithToken = async (url, data, token) => {
  const headers = setHeaders(token);
  try {
    const response = await axios.put(url, data, {
      headers: headers,
    });
    return response.status;
  } catch (error) {
    console.log(error);
    return null;
  }
};

export const uploadDataWithToken = async (url, data, token) => {
  const headers = setHeaders(token);
  try {
    const response = await axios.put(url, data, {
      headers: headers,
    });
    return response.data;
  } catch (error) {
    console.log(error);
    return null;
  }
};
