from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from storage.views import StorageAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('vacancies/', include('vacancies.urls')),
    path('storage', StorageAPI.as_view(), name='storage'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )