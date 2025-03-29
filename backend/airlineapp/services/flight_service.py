import logging

from backend.base_service import BaseService
from airlineapp.models import Flight, Fare, Coupon
from airlineapp.serializers import FlightSerializer, CouponSerializer
from airlineapp.constants import INVALID_DATA, FAILED_TO_PERFORM_OPERATION


logger = logging.getLogger('airlineapp')


class FlightService(BaseService):

    def get_flights(self):
        try:
            flights = Flight.objects.all()
            flight_serialized_obj = FlightSerializer(flights, many=True)
            data = flight_serialized_obj.data
            return self.set_response(data=data)
        except Exception as e:
            logger.error("AXIO_CAPITAL_BACKEND | FLIGHT_SERVICE | GET_FLIGHTS | ERROR: {e}")
            return self.get_400_response(errors=FAILED_TO_PERFORM_OPERATION)


    def get_faire(self, flight_id, coupon=None):
        try:
            fare_obj = Fare.objects.filter(flight__flight_id=flight_id).last()
            if not fare_obj:
                return self.get_404_response(errors=FAILED_TO_PERFORM_OPERATION)
            data = {'fare': fare_obj.fare}
            coupon_obj = Coupon.objects.filter(code=coupon).last()
            if coupon and coupon_obj:
                price_after_discount = fare_obj.fare - fare_obj.fare * coupon_obj.discount_percentage / 100
                data.update({'fare': price_after_discount})
                data.update({'coupon_validity': True}) 
            elif coupon:
                data.update({'coupon_validity': False}) 
            return self.set_response(data=data)
        except Exception as e:
            logger.error("AXIO_CAPITAL_BACKEND | FLIGHT_SERVICE | GET_FAIRE | ERROR: {e}")
            return self.get_400_response(errors=FAILED_TO_PERFORM_OPERATION)


    def get_coupons(self):
        try:
            coupons_obj = Coupon.objects.all()
            coupons_serializer = CouponSerializer(coupons_obj, many=True)
            data = coupons_serializer.data
            return self.set_response(data=data)
        except Exception as e:
            logger.error("AXIO_CAPITAL_BACKEND | FLIGHT_SERVICE | GET_COUPONS | ERROR: {e}")
            return self.get_400_response(errors=FAILED_TO_PERFORM_OPERATION)


    def get_flight_data(self, flight_id):
        try:
            flight = Flight.objects.filter(flight_id=flight_id).last()
            flight_serialized_obj = FlightSerializer(flight)
            data = flight_serialized_obj.data
            return self.set_response(data=data)
        except Exception as e:
            logger.error("AXIO_CAPITAL_BACKEND | FLIGHT_SERVICE | GET_FLIGHTS | ERROR: {e}")
            return self.get_400_response(errors=FAILED_TO_PERFORM_OPERATION)
