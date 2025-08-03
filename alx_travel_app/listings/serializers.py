from rest_framework import serializers
from .models import Listing, Booking, Review
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']

class ListingSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)
    
    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    listing = ListingSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['id', 'total_price', 'created_at', 'updated_at']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

class CreateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['listing', 'start_date', 'end_date']
        
    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("End date must be after start date")
        return data
