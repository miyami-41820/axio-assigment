import { Routes, Route } from "react-router";
import Flights from "../src/components/Flights";
import NotFound from "../src/components//NotFound";
import BookingPage from "./components/BookingPage";
import Reservations from "./components/Reservations";
import Coupons from "./components/Coupons";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Flights />} />
      <Route path="/book-flight/:flightId" element={<BookingPage />} />
      <Route path="/bookings/" element={<Reservations />} />
      <Route path="/coupons/" element={<Coupons />} />
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}