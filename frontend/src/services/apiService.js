import axios from "axios";

export const setHeaders = (token) => {
  return {
    Authorization: `Bearer ${token}`,
  };
};

// ------------------ API CALLS ------------------//

//------------------ GET API CALLS ------------------//

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
    return response.data ? response.data : response.status;
  } catch (error) {
    console.log(error);
    return null;
  }
};

export const fetchDataWithTokenAndParams = async (url, token, params) => {
  const headers = setHeaders(token);
  try {
    const response = await axios.get(url, {
      headers: headers,
      params: params,
    });
    return response.data;
  } catch (error) {
    console.log(error);
    return null;
  }
};

export const fetchDataWithParams = async (url, params) => {
  try {
    const response = await axios.get(url, {
      params: params,
    });
    return response.data;
  } catch (error) {
    console.log(error);
    return null;
  }
};

//------------------ PUT API CALLS ------------------//

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

//------------------ PATCH API CALLS ------------------//

export const patchData = async (url) => {
  try {
    const response = await axios.patch(url);
    return response.data;
  } catch (error) {
    console.log(error);
    return null;
  }
};

export const patchDataWithToken = async (url, data, token) => {
  const headers = setHeaders(token);
  try {
    const response = await axios.patch(url, data, {
      headers: headers,
    });
    return response.data;
  } catch (error) {
    console.log(error);
    return null;
  }
};

// ------------------ POST API CALLS ------------------//

export const postDataWithToken = async (url, data, token) => {
  const headers = setHeaders(token);
  try {
    const response = await axios.post(url, data, {
      headers: headers,
    });
    return response.data;
  } catch (error) {
    console.log(error);
    return null;
  }
};

export const postData = async (url, data) => {
  try {
    const response = await axios.post(url, data);
    return response.data;
  } catch (error) {
    console.log(error);
    return null;
  }
};

export const logoutUserAPI = async (url, token) => {
  const headers = setHeaders(token);
  try {
    const response = await axios.post(url, token, {
      headers: headers,
    });
    return response.status;
  } catch (error) {
    console.log(error);
    return null;
  }
};

// ------------------ DELETE API CALLS ------------------//

export const deleteDataWithToken = async (url, token) => {
  const headers = setHeaders(token);
  try {
    const response = await axios.delete(url, {
      headers: headers,
    });
    return response.status;
  } catch (error) {
    console.log(error);
    return null;
  }
};

export const deleteDataWithTokenAndData = async (url, data, token) => {
  const headers = setHeaders(token);
  try {
    const response = await axios.delete(url, {
      headers: headers,
      data: data,
    });
    return response.status;
  } catch (error) {
    console.log(error);
    return null;
  }
};
