from django.shortcuts import render
from backend.serializers import FurnitureSerializer, StoreSerializer, ManagerSerializer
from backend.models import Manager, Store, Furniture
from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters
from rest_framework.response import Response
from rest_framework import viewsets, views
# Create your views here.


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       rest_filters.SearchFilter, rest_filters.OrderingFilter)
    filterset_fields = ('firstname', 'lastname')
    ordering_fields = ('firstname', 'lastname')
    search_fields = ('^firstname', '^lastname')


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       rest_filters.SearchFilter, rest_filters.OrderingFilter)
    filterset_fields = ('name', 'address', 'manager', 'net_sales')
    ordering_fields = ('name', 'address', 'manager', 'net_sales')
    search_fields = ('^name', '^address', '^manager', '^net_sales')


class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       rest_filters.SearchFilter, rest_filters.OrderingFilter)
    filterset_fields = ('name', 'state', 'price', 'store', 'status')
    ordering_fields = ('name', 'state', 'price', 'store', 'status')
    search_fields = ('^name', '^state', '^price', '^store', '^status')


class FurnitureAPIViewPostStatus(views.APIView):
    queryset = Furniture.objects.all()

    # post on /api/furnitures/status/{id}
    def post(self, request, pk):
        furniture = Furniture.objects.get(pk=pk)
        if (request.data['status'] == 'sold'):
            furniture.status = 'sold'
            furniture.store.net_sales += furniture.price
            furniture.store.save()
        furniture.status = request.data['status']
        furniture.save()
        return Response({'status': 'ok'})
