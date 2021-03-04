from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('accounts.urls')),
    path('diary/', include('diary.urls')),
    path('log/', include('log.urls')),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
