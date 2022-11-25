from django.shortcuts import render
from backend.serializers import UserSerializer, VehicleSerializer, BookingSerializer
from backend.models import User, Vehicle, Booking
from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters
from rest_framework.response import Response
from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.decorators import action

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend, rest_filters.SearchFilter)
    filterset_fields = ('id', 'username', 'civil', 'firstname',
                        'lastname',  'password', 'role')
    search_fields = ('id', 'username', 'civil', 'firstname',
                     'lastname', 'password', 'role')

    def get_permissions(self):
        # Your logic should be all here
        if self.request.method == 'POST':
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated, ]

        return super(UserViewSet, self).get_permissions()

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # register User
            user = get_user_model().objects.create_user(
                username=serializer.data['username'],
                password=serializer.data['password'],
            )
            serializer.date["password"] = user.password
            return Response(serializer.data)
        return Response(serializer.errors)


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = (filters.DjangoFilterBackend, rest_filters.SearchFilter)
    filterset_fields = ('id', 'brand', 'model', 'year',
                        'kilometers', 'daily_price', 'available', 'image')
    search_fields = ('id', 'brand', 'model', 'year',
                     'kilometers', 'daily_price', 'available', 'image')
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = (filters.DjangoFilterBackend, rest_filters.SearchFilter)
    filterset_fields = ('id', 'user', 'vehicle', 'date',
                        'days', 'kilometers', 'total_price')
    search_fields = ('id', 'user', 'vehicle', 'date',
                     'days', 'kilometers', 'total_price')
    permission_classes = [IsAuthenticated]


class RegisterView(views.APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.create_user(
            username=serializer.data['username'],
            password=serializer.data['password'],
        )
        return Response(serializer.data)
