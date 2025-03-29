import { useLocation, useParams } from "react-router";
import { useState, useEffect } from "react";
import { Card, Typography, TextField, Button, Box, CircularProgress } from "@mui/material";
import axios from "axios";
import { useNavigate } from "react-router";

export default function BookingPage() {
  const { flightId } = useParams();
  const location = useLocation();
  const navigate = useNavigate();

  const [flight, setFlight] = useState(null);
  const [price, setPrice] = useState(null);
  const [fullName, setFullName] = useState("");
  const [coupon, setCoupon] = useState("");
  const [loading, setLoading] = useState(true);
  const [couponValidating, setCouponValidating] = useState(false);
  const [couponValid, setCouponValid] = useState(null);
  const [error, setError] = useState(null);
  const [proceedLoading, setProceedLoading] = useState(null);

  useEffect(() => {
    async function fetchFlightData() {
      try {
        // Fetch flight data
        const { data } = await axios.get(`http://127.0.0.1:8000/flights/${flightId}/`);
        setFlight(data.data);

        // Fetch price
        const priceRes = await axios.get(`http://127.0.0.1:8000/flights/${flightId}/fare/`);
        setPrice(priceRes.data.data.fare);
      } catch (error) {
        console.error("Error fetching flight data:", error);
      } finally {
        setLoading(false);
      }
    }

    fetchFlightData();
  }, [flightId]);

  const applyCoupon = async () => {
    if (!coupon){
      return;
    }

    setCouponValidating(true);
    try {
      const priceRes = await axios.get(`http://127.0.0.1:8000/flights/${flightId}/fare/?coupon=${coupon}`);
      const data = priceRes.data.data;
      setCouponValid(data);
      setPrice(priceRes.data.data.fare);

    } catch (error) {
      console.error("Error validating coupon:", error);
      setCouponValid(error);
    } finally {
      setCouponValidating(false);
    }
  };

  const proceedToPayment = async () => {
    if (!fullName.length) {
      setError("Please enter Full Name");
      return;
    }
  
    setProceedLoading(true);
  
    const payload = {
      passenger_name: fullName,
      paid_price: price,
      flight_id: flightId,
    };

    if (coupon){
      payload['coupon'] = coupon;
    }
  
    try {
      const response = await axios.post("http://127.0.0.1:8000/reservation/", payload);

      setTimeout(() => {
        navigate("/bookings");
      }, 1000);
    } catch (error) {
      setError(error?.response?.data?.message || "Something went wrong. Please try again.");
    } finally {
      setProceedLoading(false);
    }
  };

  const onChangeCoupon = (e) => {
    setCouponValid(null);
    setCoupon(e.target.value);
  }

  if (loading) return <CircularProgress sx={{ display: "block", margin: "20px auto" }} />;

  return (
    <Box sx={{ padding: 3 }}>
      {/* Flight Details */}
      <Card sx={{ padding: 2, boxShadow: 3 }}>
        <Typography variant="h5">{flight?.airline}</Typography>
        <Typography>{flight?.departure_location} → {flight?.destination_location}</Typography>
        <Typography>Departure: {new Date(flight?.departure_time).toLocaleString()}</Typography>
        <Typography>Arrival: {new Date(flight.destination_time).toLocaleString()}</Typography>
      </Card>

      {/* User Details */}
      <Card sx={{ padding: 2, boxShadow: 3, marginTop: 2 }}>
        <TextField
          label="Full Name"
          variant="outlined"
          // fullWidth
          required
          value={fullName}
          onChange={(e) => setFullName(e.target.value)}
          sx={{ marginBottom: 2, width: '50%' }}
        />
      </Card>

      <Card sx={{ padding: 2, boxShadow: 3, marginTop: 2, display: 'flex', gap: 1, alignItems: 'center' }}>
        <TextField
          label="Apply Coupon"
          variant="outlined"
          // fullWidth
          value={coupon}
          onChange={(e) => onChangeCoupon(e)}
          sx={{ width: '50%' }}
        />
        <Box>
          <Button variant="contained" color="primary" onClick={applyCoupon} disabled={couponValidating || !coupon.length}>
            {couponValidating ? "Validating..." : "Apply Coupon"}
          </Button>
          {coupon.length && couponValid ?
          <Typography color={couponValid.coupon_validity ? 'success' : 'error'}>{couponValid.coupon_validity ? 'Coupon applied successfully!' : 'Invalid coupon'}</Typography> : ''
          }
        </Box>
      </Card>

      {/* Final Price & Proceed Button */}
      <Box sx={{ marginTop: 2 }}>
        <Typography variant="h6">Final Price: {price}</Typography>
        <Button variant="contained" color="primary" fullWidth sx={{ marginTop: 2 }} onClick={proceedToPayment} disabled={proceedLoading}>
          {proceedLoading ? <CircularProgress size={24} color="inherit" /> : "Proceed to Payment"}
        </Button>
        {error && 
          <Typography color="error">Error: {error}</Typography>
        }
      </Box>
    </Box>
  );
}
