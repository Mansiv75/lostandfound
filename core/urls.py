from django.urls import path
from .views import LostItemListCreateView, LostItemDeleteView, FoundItemListCreateView,  FoundItemDeleteView, MatchItemsView

urlpatterns = [
    path('lost-items/', LostItemListCreateView.as_view(), name='lost-item-create'),
    path('lost-items/<int:pk>/', LostItemDeleteView.as_view(), name='lost-item-delete'),
    path('found-items/', FoundItemListCreateView.as_view(), name='found-item-create'),
    path('found-items/<int:pk>/', FoundItemDeleteView.as_view(), name='found-item-delete'),
    path('match-items/', MatchItemsView.as_view(), name='match-items'),
]