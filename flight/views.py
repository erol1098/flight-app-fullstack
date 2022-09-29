from flight.serializers import FlightSerializer, ReservationSerializer
from .models import Flight, Passenger, Reservation
from rest_framework import viewsets
from flight.permissions import IsStaffOrReadOnly
# Create your views here.

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStaffOrReadOnly,)

class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer