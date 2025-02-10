from django.urls import path
from .views import LostItemCreateView, LostItemListView, LostItemDeleteView, FoundItemCreateView, FoundItemListView, FoundItemDeleteView, MatchItemsView

urlpatterns = [
    path('lost-item/', LostItemCreateView.as_view(), name='lost-item-create'),
    path('lost-item/', LostItemListView.as_view(), name='lost-item-list'),
    path('lost-item/<int:pk>/', LostItemDeleteView.as_view(), name='lost-item-delete'),
    path('found-item/', FoundItemCreateView.as_view(), name='found-item-create'),
    path('found-item/', FoundItemListView.as_view(), name='found-item-list'),
    path('found-item/<int:pk>/', FoundItemDeleteView.as_view(), name='found-item-delete'),
    path('match-items/', MatchItemsView.as_view(), name='match-items'),
]