import useAuthenticationStore from "@/stores/authentication";
import { logoutUserAPI, postData } from "@/services/apiService";

export const getAuthenticationStore = () => {
  const authenticationStore = useAuthenticationStore();
  return authenticationStore;
};

export const logoutUser = async (url) => {
  const authenticationStore = getAuthenticationStore();
  const token = authenticationStore.token;
  const logoutUserResponse = await logoutUserAPI(url, token);
  if (logoutUserResponse == 204) {
    authenticationStore.logout();
    return true;
  }
  return false;
};

export const loginUser = async (url, data) => {
  const authenticationStore = getAuthenticationStore();
  const loginResponse = await postData(url, data);
  if (loginResponse) {
    const token = loginResponse.auth_token;
    authenticationStore.setToken(token);
    authenticationStore.setUser(data.email);
    authenticationStore.getAccountPictures();
    authenticationStore.checkIfProfileComplete();
    return true;
  }
  return false;
};

export const signUpUser = async (url, data) => {
  const signUpResponse = await postData(url, data);
  if (signUpResponse) {
    console.log(signUpResponse);
    return true;
  }
  return false;
};
