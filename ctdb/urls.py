from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('accounts.urls')),
    path('diary/', include('diary.urls')),
    path('', RedirectView.as_view(url='diary/diaries/'), name='index'),
    path('admin/', admin.site.urls),
]
