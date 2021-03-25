from django.urls import include, path
from django.views.generic import RedirectView

from .views import news_list

urlpatterns = [
    path('news/', news_list, name='news_list'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', RedirectView.as_view(url='/news/'), name='index'),
]
