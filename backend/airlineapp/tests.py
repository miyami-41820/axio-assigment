from django.test import TestCase, Client
from django.urls import reverse
from airlineapp.models import Flight, ReserVation, Coupon, Fare
from rest_framework import status
import datetime
from django.utils import timezone

class FlightTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.flight = Flight.objects.create(
            airline="IndiGo",
            departure_location="Delhi",
            destination_location="Mumbai",
            destination_time=timezone.make_aware(datetime.datetime.now()),  # ✅ Fixed
            departure_time=datetime.date.today(),
            available_seats=50
        )

    def test_get_all_flights(self):
        response = self.client.get(reverse('flights'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('data', response.json())

    def test_get_single_flight(self):
        response = self.client.get(reverse('single-flights', args=[self.flight.flight_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['data']['flight_id'], self.flight.flight_id)


class FareTests(TestCase):
    def setUp(self):
        self.flight = Flight.objects.create(
            airline="AirIndia",
            departure_location="Delhi",
            destination_location="Mumbai",
            destination_time=timezone.make_aware(datetime.datetime.now()),  # ✅ Fixed
            departure_time=datetime.date.today(),
            available_seats=100
        )

        self.fare = Fare.objects.create(
            flight=self.flight,
            fare='5000.00'
        )

        self.coupon = Coupon.objects.create(
                code="DISCOUNT50", 
                discount_percentage=50,
                valid_until=datetime.date.today())

    def test_get_fare(self):
        url = reverse('fare_detail', args=[self.flight.flight_id])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.json()['data']['fare']), "5000.0")

        response = self.client.get(url, {'coupon':  self.coupon.code})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_fare = '2500.0'
        self.assertEqual(str(response.json()['data']['fare']), expected_fare)


class CouponTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.coupon = Coupon.objects.create(code="COUPON52",
                discount_percentage=30,
                valid_until=datetime.date.today())

    def test_get_all_coupons(self):
        response = self.client.get(reverse('coupon'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('data', response.json())


class ReservationTests(TestCase):
    def setUp(self):
        self.flight = Flight.objects.create(
            airline="Vistara",
            departure_location="Vellore",
            destination_location="Lucknow",
            destination_time=timezone.make_aware(datetime.datetime.now()),  # ✅ Fixed
            departure_time=datetime.date.today(),
            available_seats=90
        )

        self.fare = Fare.objects.create(
            flight=self.flight,
            fare='5000.00'
        )

        self.reservation_data = {
            "flight_id": self.flight.flight_id,
            "passenger_name": "John Doe",
            "paid_price":'5000.00',
        }

    def test_create_reservation(self):
        url = reverse('reservation')
        response = self.client.post(url, self.reservation_data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_reservation(self):
        url = reverse('reservation')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('data', response.json())


class ConfirmedReservation(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_all_confirmed_reservation(self):
        response = self.client.get(reverse('confirmed_reservation'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('data', response.json())
