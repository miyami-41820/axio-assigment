import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router";
import { BookingProvider } from "../src/context/GlobalContext";
import App from "./App";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <BookingProvider>
        <App />
      </BookingProvider>
    </BrowserRouter>
  </React.StrictMode>
);