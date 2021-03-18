from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from .static import static

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('diary/', include('diary.urls')),
    path('log/', include('log.urls')),
    path('telecom/', include('telecom.urls')),
    path('reminder/', include('reminder.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG or settings.USE_WHITENOISE:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
