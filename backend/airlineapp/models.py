from django.db import models

#flight model 
class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    airline = models.CharField(max_length=100)
    departure_location = models.CharField(max_length=100)
    destination_location = models.CharField(max_length=100)
    destination_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    available_seats = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.airline} ({self.departure_location} -> {self.destination_location})"

#reservation model 
class ReserVation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=5, null=True)
    confirmed = models.BooleanField(default=False)
    paid_price = models.FloatField(default=False)

    def __str__(self):
        return f"Reservation {self.id} - {self.passenger_name} - {self.flight}"

#coupon model 
class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percentage = models.IntegerField()
    valid_until = models.DateField()

    def __str__(self):
        return self.code

#fare model
class Fare(models.Model):
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.flight.airline} : {self.fare}'
