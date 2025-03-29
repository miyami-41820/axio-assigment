import axios from "axios";

const API_BASE_URL = "https://api.example.com";

export const getFlights = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/flights`);
    return response.data;
  } catch (error) {
    console.error("Error fetching flights:", error);
    return [];
  }
};