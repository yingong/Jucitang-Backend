from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

# Create your views here.


class ItemView(viewsets.ModelViewSet):
    # reload functinos to achieve CRUD in one class
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
