from django.shortcuts import render
from rest_framework import generics, filters
from .models import LostItem, FoundItem
from .serializers import UserSerializer, LostItemSerializer, FoundItemSerializer

#Report a lost item(POST)
class LostItemCreateView(generics.CreateAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer

#Report a found item(POST)
class FoundItemCreateView(generics.CreateAPIView):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer

#List all lost items(GET)
class LostItemListView(generics.ListAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer

#List all found items(GET)
class FoundItemListViewI(generics.ListAPIView):
    queryset=FoundItem.objects.all()
    serializer_class=FoundItemSerializer



#Delete a lost item(DELETE)
class LostItemDeleteView(generics.DestroyAPIView):
    queryset = LostItem.objects.all()
    serializer_class=LostItemSerializer

#Delete a found item(DELETE)
class FoundItemDeleteView(generics.DestroyAPIView):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer

