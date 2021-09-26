from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

from AlmabaseTask import settings

schema_view = get_schema_view(
   openapi.Info(
      title="Almabase Task API's",
      default_version='v1',
      description="This documents contains all the api's used in Almabase project.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # API docs
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # App urls
    path('wish/', include('wish.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
