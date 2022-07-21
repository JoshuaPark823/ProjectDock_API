from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users_api import urls as users_api_urls
from rest_framework import routers
from projects_api.views import ProjectConfigViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="ProjectDock API",
        default_version='v1',
        description="ProjectDock v1.0.0 Django API documentation. Contact Josh Park for more details.",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

project_config_router = routers.DefaultRouter()
project_config_router.register(r'', ProjectConfigViewSet)

urlpatterns = [
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('admin/', admin.site.urls),
    path('auth/', include('auth_api.urls')),
    path('project-configs/', include(project_config_router.urls)),
    path('users/', include(users_api_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)