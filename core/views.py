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
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.mail import send_mail
from django.conf import settings

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
    parser_classes = [MultiPartParser, FormParser] #enables file upload

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#Report a found item(POST/GET)
class FoundItemListCreateView(generics.ListCreateAPIView):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser] #enables file upload

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#Delete a lost item(DELETE)
class LostItemDeleteView(generics.DestroyAPIView):
    queryset = LostItem.objects.all()
    serializer_class=LostItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

#Delete a found item(DELETE)
class FoundItemDeleteView(generics.DestroyAPIView):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

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
                    if lost.user and lost.user.email:
                        send_mail(
                        subject="Your lost item might be found!",
                        message=f"Your lost item '{lost.name}' might be found at {found.location}.",
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[lost.user.email],
                        fail_silently=False,
                    )
        return Response(matches)
    
class UserLostItemView(generics.ListAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
class UserFoundItemView(generics.ListAPIView):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
class NearbyLostItemsView(generics.ListAPIView):
    serializer_class = LostItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        location = self.request.query_params.get('location', None)
        if location:
            return LostItem.objects.filter(location__icontains=location)
        return LostItem.objects.all()
    
class NearbyFoundItemsView(generics.ListAPIView):
    serializer_class = FoundItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        location = self.request.query_params.get('location', None)
        if location:
            return FoundItem.objects.filter(location__icontains=location)
        return FoundItem.objects.all()