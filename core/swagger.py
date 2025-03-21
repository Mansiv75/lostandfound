from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Lost and Found API",
        default_version='v1',
        description="API for managing lost and found items",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(name="Lost and Found Team", email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)