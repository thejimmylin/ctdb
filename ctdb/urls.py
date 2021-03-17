from django.contrib import admin
from django.urls import include, path

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
