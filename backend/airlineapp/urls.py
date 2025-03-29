from django.urls import path
from airlineapp.views import Flights, Reservation, FareDetail, Coupon, ReservationConfirmed, Flight

urlpatterns = [
    path('flights/', Flights.as_view(), name='flights'), #API to get all the available flights.
    path('flights/<int:flight_id>/', Flight.as_view(), name='single-flights'), #API to get all the available flights.
    path('reservation/', Reservation.as_view(), name='reservation'), #API to create reservation orders. + get bookings reservation
    path('confirmed-reservation/', ReservationConfirmed.as_view(), name='confirmed_reservation'), #get all confirmed reservation
    path('flights/<int:flight_id>/fare/', FareDetail.as_view(), name='fare_detail'), #API to get fare details.
    path('coupon/', Coupon.as_view(), name='coupon'), #API to get all available coupon.
]
