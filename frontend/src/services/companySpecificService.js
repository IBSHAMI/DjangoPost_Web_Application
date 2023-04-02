import axios from "axios";
import { API } from "@/api";

const setHeaders = (token) => {
  return {
    Authorization: `Bearer ${token}`,
  };
};
