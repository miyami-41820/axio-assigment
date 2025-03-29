from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from airlineapp.services.flight_service import FlightService
from airlineapp.services.reservation_service import ReservationService


class Flights(APIView):

    def get(self, request, *args, **kwargs):
        flight_service = FlightService()
        response = flight_service.get_flights()
        return Response(response,  status=response.get("code"))


class Reservation(APIView):

    def post(self, request, *args, **kwargs):
        reservation_service = ReservationService()
        response = reservation_service.create_reservation(data=request.data)
        return Response(response,  status=response.get("code"))

    def get(self, request, *args, **kwargs):
        reservation_service = ReservationService()
        response = reservation_service.get_reservations()
        return Response(response,  status=response.get("code"))


class FareDetail(APIView):

    def get(self, request, *args, **kwargs):
        flight_id = int(kwargs.get('flight_id'))
        coupon = request.query_params.get('coupon', None)
        flight_service = FlightService()
        response = flight_service.get_faire(flight_id, coupon=coupon)
        return Response(response,  status=response.get("code"))


class Coupon(APIView):

    def get(self, request, *args, **kwargs):
        flight_service = FlightService()
        response = flight_service.get_coupons()
        return Response(response,  status=response.get("code"))


class ReservationConfirmed(APIView):

    def get(self, request, *args, **kwargs):
        reservation_service = ReservationService()
        response = reservation_service.get_confirmed_reservation()
        return Response(response,  status=response.get("code"))

class Flight(APIView):

    def get(self, request, *args, **kwargs):
        flight_id = kwargs.get('flight_id')
        flight_service = FlightService()
        response = flight_service.get_flight_data(flight_id)
        return Response(response,  status=response.get("code"))
