from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import dogSerializer
from .serializers import FoodSerializer
from .models import dog, Food


class dogList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = dog.objects.all().order_by('id')
    serializer_class = dogSerializer  # tell django what serializer to use


class dogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = dog.objects.all().order_by('id')
    serializer_class = dogSerializer


class FoodList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = Food.objects.all().order_by('id')
    serializer_class = FoodSerializer  # tell django what serializer to use


class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all().order_by('id')
    serializer_class = FoodSerializer
