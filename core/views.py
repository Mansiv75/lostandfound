from django.shortcuts import render
from rest_framework import generics, filters
from .models import LostItem, FoundItem
from .serializers import UserSerializer, LostItemSerializer, FoundItemSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

#User registration
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserLoginView(TokenObtainPairView):
    permission_classes = [AllowAny]

#Report a lost item(POST/GET)
class LostItemListCreateView(generics.ListCreateAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer
    permission_classes = [IsAuthenticated]

#Report a found item(POST/GET)
class FoundItemListCreateView(generics.ListCreateAPIView):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer
    permission_classes = [IsAuthenticated]

#Delete a lost item(DELETE)
class LostItemDeleteView(generics.DestroyAPIView):
    queryset = LostItem.objects.all()
    serializer_class=LostItemSerializer
    permission_classes = [IsAuthenticated]

#Delete a found item(DELETE)
class FoundItemDeleteView(generics.DestroyAPIView):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer
    permission_classes = [IsAuthenticated]

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