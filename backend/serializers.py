from backend.models import Furniture, Manager, Store
from rest_framework import serializers


class FurnitureSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Furniture
        fields = ['id', 'name', 'state', 'price', 'store', 'status']


class StoreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Store
        fields = ['id', 'name', 'address', 'manager', 'net_sales']


class ManagerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Manager
        fields = ['id', 'firstname', 'lastname']
