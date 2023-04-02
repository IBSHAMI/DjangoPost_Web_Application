import useAuthenticationStore from "@/stores/authentication";

export const getAuthenticationStore = () => {
  const authenticationStore = useAuthenticationStore();
  return authenticationStore;
};
