from rest_framework import generics, permissions
from .models import Session, Booking
from .serializers import SessionSerializer, BookingSerializer


# 🔓 Public: list all sessions
class SessionListView(generics.ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


# 🔒 Creator: create session
class SessionCreateView(generics.CreateAPIView):
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


# 🔒 User: book a session
class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 🔒 User: view own bookings
class UserBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
