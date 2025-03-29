import logging

from backend.base_service import BaseService
from airlineapp.models import ReserVation, Flight
from airlineapp.validation import validate_reservation
from airlineapp.constants import TOTAL_SEATS, INVALID_DATA
from airlineapp.serializers import ReservationSerializer, GetReservationSerializer


logger = logging.getLogger('airlineapp')


class ReservationService(BaseService):


    @validate_reservation
    def create_reservation(self, *args, **kwargs):
        try:
            data = kwargs.get('data')
            flight_id = data.get('flight_id')
            paid_price = data.get('paid_price')
            passenger_name = data.get('passenger_name')
            flight_obj = Flight.objects.filter(flight_id=flight_id).last()
            seat_number = f'{flight_id}-{TOTAL_SEATS-flight_obj.available_seats}'
            reservation_obj = ReserVation.objects.create(flight=flight_obj, passenger_name=passenger_name, seat_number=seat_number, confirmed=True, paid_price=paid_price)
            flight_obj.available_seats = flight_obj.available_seats - 1
            flight_obj.save()
            return self.get_201_response({'status': "Book Successfully"})
        except Exception as e:
            logger.error("AXIO_CAPITAL_BACKEND | RESERVATION_SERVICE | CREATE_RESERVATION | ERROR: {e}")
            return self.get_baked_412_response(errors=INVALID_DATA)


    def get_reservations(self):
        try:
            reservations = ReserVation.objects.all().select_related()
            reservations_serialized = GetReservationSerializer(reservations, many=True)
            return self.set_response(data=reservations_serialized.data)
        except Exception as e:
            logger.error("AXIO_CAPITAL_BACKEND | RESERVATION_SERVICE | GET_RESERVATION | ERROR: {e}")
            return self.get_baked_412_response(errors=INVALID_DATA)


    def get_confirmed_reservation(self):
        try:
            reservations = ReserVation.objects.filter(confirmed=True).select_related()
            reservations_serialized = GetReservationSerializer(reservations, many=True)
            return self.set_response(data=reservations_serialized.data)
        except Exception as e:
            logger.error("AXIO_CAPITAL_BACKEND | RESERVATION_SERVICE | GET_CONFIRMED_RESERVATION | ERROR: {e}")
            return self.get_baked_412_response(errors=INVALID_DATA)
