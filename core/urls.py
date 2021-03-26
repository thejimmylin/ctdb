from django.urls import include, path

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]
