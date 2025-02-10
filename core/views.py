from django.shortcuts import render
from rest_framework import generics, filters
from .models import LostItem, FoundItem
from .serializers import UserSerializer, LostItemSerializer, FoundItemSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q


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
class FoundItemListView(generics.ListAPIView):
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

#Match Items

class MatchItemsView(APIView):
    def get(self, request):
        matches=[]

        lost_items = LostItem.objects.all()
        found_items = FoundItem.objects.all()

        for lost in lost_items:
            for found in found_items:
                if(
                    lost.name.lower() == found.name.lower() and
                    lost.location.lower() == found.location.lower() and
                    (found.date-lost.date).days<=7
                ):
                    matches.append({
                        'lost_item':LostItemSerializer(lost).data,
                        'found_item':FoundItemSerializer(found).data,
                    })
        return Response(matches)