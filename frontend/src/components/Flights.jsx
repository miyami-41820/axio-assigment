import { useEffect, useState } from "react";
import {
  Grid,
  Card,
  CardContent,
  Typography,
  Button,
  Box,
  TextField,
  CircularProgress,
  Stack
} from "@mui/material";

import FlightFooter from "./FlightFooter";
import axios from "axios";
import { useNavigate } from "react-router";

export default function Flights() {
  const [selectedFlight, setSelectedFlight] = useState(null);
  const [loading, setLoading] = useState(true);

  const [flights, setFlights] = useState([]);
  const [searchParams, setSearchParams] = useState({ from: "", to: "" });

  const navigate = useNavigate();

  useEffect(() => {
    async function fetchFlights() {
      try {
        const { data } = await axios.get(`http://127.0.0.1:8000/flights/`);
        setFlights(data.data);
      } catch (error) {
        console.error("Error fetching flight data:", error);
      } finally {
        setLoading(false);
      }
    }

    fetchFlights();
  }, []);

  const filteredFlights = flights.filter(
    (flight) =>
      (searchParams.from === "" ||
        flight?.departure_location
          .toLowerCase()
          .includes(searchParams.from.toLowerCase())) &&
      (searchParams.to === "" ||
        flight?.destination_location
          .toLowerCase()
          .includes(searchParams.to.toLowerCase()))
  );

  return (
    <>
      <Box sx={{ padding: 3 }}>
        <Stack direction="row" spacing={2} sx={{justifyContent: 'space-between', marginLeft: '8px', marginBottom: '1rem'}}>
          <Typography variant="h4" color="primary">Flights</Typography>
          <Stack direction="row" spacing={2} sx={{justifyContent: 'flex-end', marginBottom: '1rem'}}>

          <Button variant="contained" onClick={() => navigate('/coupons')}>View Coupons</Button>
          <Button variant="contained" onClick={() => navigate('/bookings')}>View Bookings</Button>
          </Stack>
        </Stack>

        {/* Search */}
        <Card
          sx={{
            minWidth: "100%",
            boxShadow: 3,
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <Grid container spacing={2} sx={{ margin: 3, width: "100%" }}>
            <Grid item size={6} sx={{ width: "30%" }}>
              <TextField
                label="From (Departure Location)"
                variant="outlined"
                fullWidth
                value={searchParams.from}
                onChange={(e) =>
                  setSearchParams({ ...searchParams, from: e.target.value })
                }
              />
            </Grid>
            <Grid item size={6} sx={{ width: "30%" }}>
              <TextField
                label="To (Destination Location)"
                variant="outlined"
                fullWidth
                value={searchParams.to}
                onChange={(e) =>
                  setSearchParams({ ...searchParams, to: e.target.value })
                }
              />
            </Grid>
          </Grid>
        </Card>

        {/* Flights */}
        <Grid container spacing={3} sx={{ margin: "16px" }}>
          {filteredFlights.length > 0 && !loading ? (
            filteredFlights.map((flight) => (
              <Grid item xs={12} sm={6} md={4} key={flight.flight_id}>
                <Card sx={{ minWidth: 275, boxShadow: 3 }}>
                  <CardContent>
                    <Typography variant="h6" gutterBottom>
                      {flight.airline}
                    </Typography>
                    <Typography variant="body1">
                      <strong>From:</strong> {flight.departure_location} →{" "}
                      <strong>To:</strong> {flight.destination_location}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Departure: {new Date(flight.departure_time).toLocaleString()}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Arrival:{" "}
                      {new Date(flight.destination_time).toLocaleString()}
                    </Typography>
                    <Typography variant="body2">
                      Available Seats: <strong>{flight.available_seats}</strong>
                    </Typography>
                    <Button
                      variant="contained"
                      color="primary"
                      sx={{ mt: 2 }}
                      fullWidth
                      onClick={() => setSelectedFlight(flight)}
                    >
                      Book Now
                    </Button>
                  </CardContent>
                </Card>
              </Grid>
            ))
          ) : loading ? (
            <CircularProgress />
          ) : (
            <Typography
              variant="h6"
              color="text.secondary"
              sx={{ textAlign: "center", width: "100%", marginTop: 3 }}
            >
              No flights found
            </Typography>
          )}
        </Grid>

        {selectedFlight && <FlightFooter selectedFlight={selectedFlight} />}
      </Box>
    </>
  );
}
