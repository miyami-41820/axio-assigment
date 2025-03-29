import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from airlineapp.models import Flight, ReserVation, Coupon, Fare

class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        self.populate_flights()
        self.populate_reservations()
        self.populate_coupons()
        self.populate_fares()
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with dummy data'))

    def populate_flights(self):
        airlines = ['Air India', 'IndiGo', 'SpiceJet', 'GoAir', 'Vistara']
        locations = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata']
        
        for _ in range(10):
            departure = random.choice(locations)
            destination = random.choice([loc for loc in locations if loc != departure])
            departure_time = datetime.now() + timedelta(days=random.randint(1, 30))
            destination_time = departure_time + timedelta(hours=random.randint(1, 5))

            Flight.objects.create(
                airline=random.choice(airlines),
                departure_location=departure,
                destination_location=destination,
                departure_time=departure_time,
                destination_time=destination_time,
                available_seats=random.randint(50, 200)
            )

    def populate_reservations(self):
        flights = list(Flight.objects.all())
        passenger_names = ['John Doe', 'Alice Brown', 'Bob Smith', 'Charlie Johnson']
        
        for _ in range(20):
            flight = random.choice(flights)
            ReserVation.objects.create(
                flight=flight,
                passenger_name=random.choice(passenger_names),
                seat_number=str(random.randint(1, 50)),
                confirmed=random.choice([True, False]),
                paid_price=random.randint(2000, 10000)
            )
    
    def populate_coupons(self):
        for _ in range(5):
            Coupon.objects.create(
                code=f'COUPON{random.randint(100, 999)}',
                discount_percentage=random.randint(5, 50),
                valid_until=datetime.now().date() + timedelta(days=random.randint(10, 60))
            )

    def populate_fares(self):
        flights = Flight.objects.all()
        for flight in flights:
            Fare.objects.create(
                fare=random.uniform(3000, 20000),
                flight=flight
            )
command = Command()
run = command.handle
run()