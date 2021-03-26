from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from .static import static

# Apps
urlpatterns = [
    path('', include('core.urls')),
    path('', include('diary.urls')),
    path('', include('reminder.urls')),
    path('', include('telecom.urls')),
    path('', include('archive.urls')),
    path('', include('news.urls')),
    path('log/', include('log.urls')),
    path('auth/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/news/'), name='index'),
]

# Media things (active only when DEBUG=True or USE_WHITENOISE=True)
if settings.DEBUG or settings.USE_WHITENOISE:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
