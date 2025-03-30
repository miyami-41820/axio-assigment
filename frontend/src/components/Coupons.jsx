import { useState, useEffect } from "react";
import { Card, Typography, CircularProgress, Box, Stack } from "@mui/material";
import axios from "axios";

export default function Coupons() {
  const [coupons, setCoupons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchCoupons() {
      try {
        const { data } = await axios.get("http://127.0.0.1:8000/coupon/");
        setCoupons(data.data || []);
      } catch (error) {
        setError(error.errors || "Failed to load coupons.");
      } finally {
        setLoading(false);
      }
    }

    fetchCoupons();
  }, []);

  if (loading)
    return <CircularProgress sx={{ display: "block", margin: "20px auto" }} />;
  if (error) return <Typography color="error">Error: {error}</Typography>;

  return (
    <Box sx={{ padding: 3 }}>
      <Typography variant="h4" sx={{ marginBottom: 3 }} color="primary">
        Available Coupons
      </Typography>

      {coupons.length === 0 ? (
        <Typography>No coupons available.</Typography>
      ) : (
        coupons.map((coupon) => (
          <Card
            key={coupon.id}
            sx={{ padding: 2, marginBottom: 2, boxShadow: 3 }}
          >
            <Stack direction="row" spacing={2} sx={{justifyContent: 'space-between', marginX: 2, alignItems: 'center'}}>
            <Stack direction="column" spacing={2}>
                <Typography variant="h6">Coupon Name: {coupon.code}</Typography>
                <Typography>Discount: {coupon.discount_percentage}%</Typography>
            </Stack>
                {coupon.valid_until <= new Date().toISOString() ? (
                  <Typography color="error">Expired:  {coupon.valid_until}</Typography>
                ) : (
                  <Typography color="success.main">Expiry: {coupon.valid_until}</Typography>
                )}
            </Stack>
          </Card>
        ))
      )}
    </Box>
  );
}
