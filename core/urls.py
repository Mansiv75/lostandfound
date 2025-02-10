from django.urls import path
from .views import LostItemCreateView, LostItemListView, LostItemDeleteView, FoundItemCreateView, FoundItemListViewI, FoundItemDeleteView

url_patterns = [
    path('lost/', LostItemCreateView.as_view(), name='lost-item-create'),
    path('lost/', LostItemListView.as_view(), name='lost-item-list'),
    path('lost/delete/<int:pk>/', LostItemDeleteView.as_view(), name='lost-item-delete'),
    path('found/', FoundItemCreateView.as_view(), name='found-item-create'),
    path('found/', FoundItemListViewI.as_view(), name='found-item-list'),
    path('found/delete/<int:pk>/', FoundItemDeleteView.as_view(), name='found-item-delete'),
]