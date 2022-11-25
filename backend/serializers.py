from backend.models import User, Vehicle, Booking
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'civil', 'firstname',
                  'lastname',  'password', 'role']


class VehicleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Vehicle
        fields = ['id', 'brand', 'model', 'year',
                  'kilometers', 'daily_price', 'available', 'image']


class BookingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Booking
        fields = ['id', 'user', 'vehicle', 'date',
                  'days', 'kilometers', 'total_price']
