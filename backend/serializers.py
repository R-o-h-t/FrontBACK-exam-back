from backend.models import User, Vehicle, Booking
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    bookings = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='booking-detail'
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'civil', 'firstname',
                  'lastname',  'password', 'role', 'bookings']
        extra_kwargs = {'password': {'write_only': True}}


class VehicleSerializer(serializers.HyperlinkedModelSerializer):

    bookings = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='booking-detail'
    )

    class Meta:
        model = Vehicle
        fields = ['id', 'brand', 'model', 'year',
                  'kilometers', 'daily_price', 'available', 'image', 'bookings']


class BookingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Booking
        fields = ['id', 'user', 'vehicle', 'date',
                  'days', 'kilometers', 'total_price']
        depth = 1
