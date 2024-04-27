import axiosInstance from "@/api/axiosInstance";

export const getPrediction = async (url, data) => {
  try {
    const response = await axiosInstance.post(url, data);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
