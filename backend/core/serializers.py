from rest_framework import serializers
from .models import User, Session, Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "role", "avatar"]


class SessionSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Session
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    session = SessionSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = "__all__"
