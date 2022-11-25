from django.shortcuts import render
from backend.serializers import UserSerializer, VehicleSerializer, BookingSerializer
from backend.models import User, Vehicle, Booking
from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters
from rest_framework.response import Response
from rest_framework import viewsets, views
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend, rest_filters.SearchFilter)
    filterset_fields = ('id', 'username', 'civil', 'firstname',
                        'lastname',  'password', 'role')
    search_fields = ('id', 'username', 'civil', 'firstname',
                     'lastname', 'password', 'role')


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = (filters.DjangoFilterBackend, rest_filters.SearchFilter)
    filterset_fields = ('id', 'brand', 'model', 'year',
                        'kilometers', 'daily_price', 'available', 'image')
    search_fields = ('id', 'brand', 'model', 'year',
                     'kilometers', 'daily_price', 'available', 'image')


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = (filters.DjangoFilterBackend, rest_filters.SearchFilter)
    filterset_fields = ('id', 'user', 'vehicle', 'date',
                        'days', 'kilometers', 'total_price')
    search_fields = ('id', 'user', 'vehicle', 'date',
                     'days', 'kilometers', 'total_price')
