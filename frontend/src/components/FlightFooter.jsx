import { Box, Button, Typography, useTheme } from "@mui/material";
import { useNavigate } from "react-router";

const FlightFooter = ({ selectedFlight }) => {
  const theme = useTheme();
  const navigate = useNavigate();

  if (!selectedFlight) return null; // Don't show footer if no flight is selected

  return (
    <Box
      sx={{
        position: "fixed",
        bottom: 0,
        left: 0,
        width: "98%",
        backgroundColor: theme.palette.background.paper,
        boxShadow: "0 -2px 10px rgba(0,0,0,0.1)",
        padding: 2,
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
      }}
    >
      {/* Flight Details */}
      <Box>
        <Typography variant="subtitle1" fontWeight="bold">
          {selectedFlight.airline}
        </Typography>
        <Typography variant="body2">
          {selectedFlight.departure_location} → {selectedFlight.destination_location}
        </Typography>
        <Typography variant="body2">
          Departure: {new Date(selectedFlight.departure_time).toLocaleString()}
        </Typography>
      </Box>

      {/* Button to Proceed */}
      <Button
        variant="contained"
        color="primary"
        onClick={() => navigate(`/book-flight/${selectedFlight.flight_id}`, { state: { selectedFlight } })}
      >
        Continue Booking
      </Button>
    </Box>
  );
};

export default FlightFooter;
