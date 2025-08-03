from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing, Booking, Review
import random
from datetime import datetime, timedelta
import json

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with sample listings, bookings, and reviews'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        self.create_users()
        self.create_listings()
        self.create_bookings()
        self.create_reviews()
        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))

    def create_users(self):
        users = [
            {'email': 'host1@example.com', 'password': 'testpass123', 'first_name': 'John', 'last_name': 'Doe'},
            {'email': 'host2@example.com', 'password': 'testpass123', 'first_name': 'Jane', 'last_name': 'Smith'},
            {'email': 'guest1@example.com', 'password': 'testpass123', 'first_name': 'Alice', 'last_name': 'Johnson'},
            {'email': 'guest2@example.com', 'password': 'testpass123', 'first_name': 'Bob', 'last_name': 'Williams'},
        ]
        
        for user_data in users:
            user, created = User.objects.get_or_create(
                email=user_data['email'],
                defaults={
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name']
                }
            )
            if created:
                user.set_password(user_data['password'])
                user.save()
                self.stdout.write(f'Created user: {user.email}')

    def create_listings(self):
        amenities = [
            ["WiFi", "Kitchen", "Washer", "Air conditioning", "Heating"],
            ["Pool", "Free parking", "TV", "Gym", "Hot tub"],
            ["Fireplace", "BBQ grill", "Patio", "Garden", "Breakfast"],
        ]
        
        listings = [
            {
                'title': 'Cozy Apartment in Downtown',
                'property_type': 'apartment',
                'price_per_night': 120,
                'bedrooms': 2,
                'bathrooms': 1,
                'max_guests': 4,
                'city': 'New York',
                'country': 'USA'
            },
            {
                'title': 'Luxury Villa with Ocean View',
                'property_type': 'villa',
                'price_per_night': 350,
                'bedrooms': 4,
                'bathrooms': 3,
                'max_guests': 8,
                'city': 'Malibu',
                'country': 'USA'
            },
            {
                'title': 'Mountain Cabin Retreat',
                'property_type': 'cabin',
                'price_per_night': 180,
                'bedrooms': 3,
                'bathrooms': 2,
                'max_guests': 6,
                'city': 'Aspen',
                'country': 'USA'
            },
        ]
        
        hosts = User.objects.filter(email__in=['host1@example.com', 'host2@example.com'])
        
        for i, listing_data in enumerate(listings):
            listing, created = Listing.objects.get_or_create(
                title=listing_data['title'],
                defaults={
                    'host': hosts[i % len(hosts)],
                    'description': f"Beautiful {listing_data['property_type']} in {listing_data['city']}",
                    'property_type': listing_data['property_type'],
                    'price_per_night': listing_data['price_per_night'],
                    'bedrooms': listing_data['bedrooms'],
                    'bathrooms': listing_data['bathrooms'],
                    'max_guests': listing_data['max_guests'],
                    'address': f"{random.randint(1, 1000)} Main St",
                    'city': listing_data['city'],
                    'country': listing_data['country'],
                    'amenities': json.dumps(amenities[i % len(amenities)])
                }
            )
            if created:
                self.stdout.write(f'Created listing: {listing.title}')

    def create_bookings(self):
        listings = Listing.objects.all()
        guests = User.objects.filter(email__in=['guest1@example.com', 'guest2@example.com'])
        
        for i in range(10):
            listing = random.choice(listings)
            guest = random.choice(guests)
            
            start_date = datetime.now() + timedelta(days=random.randint(1, 30))
            end_date = start_date + timedelta(days=random.randint(1, 14))
            
            booking, created = Booking.objects.get_or_create(
                listing=listing,
                user=guest,
                start_date=start_date,
                end_date=end_date,
                defaults={
                    'status': random.choice(['pending', 'confirmed', 'completed']),
                    'total_price': listing.price_per_night * (end_date - start_date).days
                }
            )
            if created:
                self.stdout.write(f'Created booking for {listing.title}')

    def create_reviews(self):
        bookings = Booking.objects.filter(status='completed')
        
        for booking in bookings:
            review, created = Review.objects.get_or_create(
                listing=booking.listing,
                user=booking.user,
                defaults={
                    'rating': random.randint(3, 5),
                    'comment': f"Great stay at {booking.listing.title}! Would recommend."
                }
            )
            if created:
                self.stdout.write(f'Created review for {booking.listing.title}')
