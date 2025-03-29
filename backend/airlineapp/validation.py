from airlineapp.models import Flight, Coupon, Fare
from airlineapp.constants import NOT_VALID_DATA
from airlineapp.serializers import ReservationSerializer
from backend.base_service import BaseService
from decimal import Decimal

def validate_reservation(func):
    def wrapper(self, *args, **kwargs):
        import pdb; pdb.set_trace()
        try:
            reservation_serializer = ReservationSerializer(data=kwargs.get('data'))
            if not reservation_serializer.is_valid():
                raise Exception(NOT_VALID_DATA)
            data = reservation_serializer.data
            flight_id = data.get('flight_id')
            coupon = data.get('coupon')
            paid_price = data.get('paid_price')
            flight_obj = Flight.objects.filter(flight_id=int(flight_id)).last()
            if not flight_obj:
                raise Exception(NOT_VALID_DATA)
            discount_price_percentage = 0
            if coupon:
                coupon_obj = Coupon.objects.filter(code=coupon).last()
                if not coupon_obj:
                    raise Exception(NOT_VALID_DATA)
                discount_price_percentage = coupon_obj.discount_percentage/100
            fare_obj = Fare.objects.filter(flight=flight_obj).last()
            if Decimal(str(paid_price)) != fare_obj.fare- fare_obj.fare* Decimal(str(discount_price_percentage)):
                raise Exception(NOT_VALID_DATA)
            response = func(self, *args, **kwargs)
            return response
        except Exception as e:
            return BaseService().get_404_response(errors=NOT_VALID_DATA)
    return wrapper
