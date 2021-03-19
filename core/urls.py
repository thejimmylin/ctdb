from django.urls import include, path
from django.views.generic import RedirectView

from .views import http404, news

urlpatterns = [
    path('news/', news, name='news'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', RedirectView.as_view(url='/news/'), name='index'),
    path('<path:path>', http404, name='http404'),
]
