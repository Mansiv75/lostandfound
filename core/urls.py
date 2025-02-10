from django.urls import path, re_path
from .views import LostItemListCreateView, LostItemDeleteView, FoundItemListCreateView,  FoundItemDeleteView, MatchItemsView, UserRegisterView
from .views import UserLoginView, UserLostItemView, UserFoundItemView, NearbyLostItemsView, NearbyFoundItemsView
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from .swagger import schema_view

urlpatterns = [
    path('users/register/', UserRegisterView.as_view(), name='register'),
    path('token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/login/', UserLoginView.as_view(), name='login'),
    path('lost-items/', LostItemListCreateView.as_view(), name='lost-items'),
    path('lost-items/<int:pk>/', LostItemDeleteView.as_view(), name='lost-item-delete'),
    path('found-items/', FoundItemListCreateView.as_view(), name='found-items'),
    path('found-items/<int:pk>/', FoundItemDeleteView.as_view(), name='found-item-delete'),
    path('match-items/', MatchItemsView.as_view(), name='match-items'),
    path('lost-items/history/', UserLostItemView.as_view(), name='lost-item-history'),
    path('found-items/history/', UserFoundItemView.as_view(), name='found-item-history'),
    path('nearby-lost-items/', NearbyLostItemsView.as_view(), name='nearmost-lost-items'),
    path('nearby-found-items/', NearbyFoundItemsView.as_view(), name='nearmost-found-items'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)