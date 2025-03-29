import { useState, useEffect } from "react";
import {
  Card,
  Typography,
  CircularProgress,
  Box,
  Stack,
  Button,
} from "@mui/material";
import axios from "axios";

export default function Reservations() {
  const [reservations, setReservations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchReservations();
  }, []);

  const fetchReservations = async () => {
    try {
      const { data } = await axios.get("http://127.0.0.1:8000/reservation/");
      setReservations(data.data || []);
    } catch (error) {
      setError(error.errors || "Failed to load reservations.");
    } finally {
      setLoading(false);
    }
  };

  const fetchConfirmedBookings = async () => {
    try {
      const { data } = await axios.get(
        "http://127.0.0.1:8000/confirmed-reservation/"
      );
      setReservations(data.data || []);
    } catch (error) {
      setError(error.errors || "Failed to load reservations.");
    } finally {
      setLoading(false);
    }
  };

  if (loading)
    return <CircularProgress sx={{ display: "block", margin: "20px auto" }} />;
  if (error) return <Typography color="error">{error}</Typography>;

  return (
    <Box sx={{ padding: 3 }}>
      <Stack
        direction="row"
        spacing={2}
        sx={{ justifyContent: "space-between", marginX: 2, marginBottom: 3 }}
      >
        <Typography variant="h4" sx={{ marginBottom: 2 }} color="primary">
          Your Reservations
        </Typography>

        <Stack direction="row" spacing={2}>
          <Button variant="outlined" onClick={() => fetchConfirmedBookings()}>
            View Confirmed Bookings
          </Button>
          <Button variant="contained" onClick={() => fetchReservations()}>
            View All Bookings
          </Button>
        </Stack>
      </Stack>

      {reservations.length === 0 ? (
        <Typography>No reservations found.</Typography>
      ) : (
        reservations.map((reservation) => (
          <Card
            key={reservation.id}
            sx={{ padding: 2, marginBottom: 2, boxShadow: 3 }}
          >
            <Stack
              direction="row"
              spacing={2}
              sx={{ justifyContent: "space-between", marginX: 2 }}
            >
              <Stack direction="column" spacing={1}>
                <Typography variant="h6">
                  {reservation.flight.airline}
                </Typography>
                <Typography sx={{ fontWeight: "bold" }}>
                  {reservation.flight.departure_location} →{" "}
                  {reservation.flight.destination_location}
                </Typography>
                <Typography sx={{ fontWeight: "bold" }}>
                  Departure: {reservation.flight.departure_time}
                </Typography>
                <Typography sx={{ fontWeight: "bold" }}>
                  Arrival:{" "}
                  {new Date(
                    reservation.flight.destination_time
                  ).toLocaleString()}
                </Typography>
                <Typography>Passenger: {reservation.passenger_name}</Typography>
                <Typography>Price Paid: ₹{reservation.paid_price}</Typography>
                <Typography>Seat Number: {reservation.seat_number}</Typography>
              </Stack>
              <Typography
                variant="h6"
                color={reservation.confirmed ? "success" : "error"}
              >
                {reservation.confirmed ? "Confirmed" : "Pending Confirmation"}
              </Typography>
            </Stack>
          </Card>
        ))
      )}
    </Box>
  );
}
