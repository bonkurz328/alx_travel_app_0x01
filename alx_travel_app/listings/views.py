from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Listing objects.
    Provides CRUD operations for listings.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Associate the listing with the authenticated user
        """
        serializer.save(owner=self.request.user)

class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Booking objects.
    Provides CRUD operations for bookings.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Associate the booking with the authenticated user
        """
        serializer.save(user=self.request.user)


