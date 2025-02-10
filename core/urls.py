from django.urls import path
from .views import LostItemCreateView, LostItemListView, LostItemDeleteView, FoundItemCreateView, FoundItemListViewI, FoundItemDeleteView

url_patterns = [
    path('lost-item/', LostItemCreateView.as_view(), name='lost-item-create'),
    path('lost-item/', LostItemListView.as_view(), name='lost-item-list'),
    path('lost-item/<int:pk>/', LostItemDeleteView.as_view(), name='lost-item-delete'),
    path('found-item/', FoundItemCreateView.as_view(), name='found-item-create'),
    path('found-item/', FoundItemListViewI.as_view(), name='found-item-list'),
    path('found-item/<int:pk>/', FoundItemDeleteView.as_view(), name='found-item-delete'),
]