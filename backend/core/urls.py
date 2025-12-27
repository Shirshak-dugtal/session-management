from django.urls import path
from .views import (
    SessionListView,
    SessionCreateView,
    BookingCreateView,
    UserBookingsView,
)

urlpatterns = [
    path("sessions/", SessionListView.as_view()),
    path("sessions/create/", SessionCreateView.as_view()),
    path("bookings/create/", BookingCreateView.as_view()),
    path("bookings/my/", UserBookingsView.as_view()),
]
