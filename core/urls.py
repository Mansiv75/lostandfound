from django.urls import path
from .views import LostItemListCreateView, LostItemDeleteView, FoundItemListCreateView,  FoundItemDeleteView, MatchItemsView, UserRegisterView
from .views import UserLoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('users/register/', UserRegisterView.as_view(), name='register'),
    path('token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/login/', UserLoginView.as_view(), name='login'),
    path('lost-items/', LostItemListCreateView.as_view(), name='lost-item-create'),
    path('lost-items/<int:pk>/', LostItemDeleteView.as_view(), name='lost-item-delete'),
    path('found-items/', FoundItemListCreateView.as_view(), name='found-item-create'),
    path('found-items/<int:pk>/', FoundItemDeleteView.as_view(), name='found-item-delete'),
    path('match-items/', MatchItemsView.as_view(), name='match-items'),
]