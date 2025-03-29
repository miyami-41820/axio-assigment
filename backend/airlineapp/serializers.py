from rest_framework import serializers
from airlineapp.models import Flight, ReserVation, Coupon


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class ReservationSerializer(serializers.Serializer):
    flight_id = serializers.IntegerField()
    passenger_name =  serializers.CharField()
    paid_price = serializers.FloatField()
    coupon = serializers.CharField(required=False)


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


class GetReservationSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()
    class Meta:
        model = ReserVation
        fields = '__all__'
