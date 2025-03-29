from django.contrib import admin
from .models import Flight, ReserVation, Coupon, Fare


class FlightAdmin(admin.ModelAdmin):
    list_display = ['flight_id', 'airline', 'departure_location', \
        'destination_location', 'destination_time', 'departure_time', 'available_seats']
    search_fields = ['airline', 'departure_location', 'destination_location', 'departure_time', 'destination_time']
    list_filter = ['airline']


class ReserVationAdmin(admin.ModelAdmin):
    list_display = ['flight', 'passenger_name', 'seat_number', 'confirmed']
    search_fields = ['confirmed', 'flight']
    list_filter = ['confirmed']


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount_percentage', 'valid_until']
    search_fields = ['code', 'discount_percentage']
    list_filter = ['discount_percentage']


class FareAdmin(admin.ModelAdmin):
    list_display = ['fare', 'flight']
    search_fields = ['fare']


admin.site.register(Fare, FareAdmin)
admin.site.register(ReserVation, ReserVationAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Coupon, CouponAdmin)
