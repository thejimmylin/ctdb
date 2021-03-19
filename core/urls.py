from django.urls import path, include
from django.views.generic import RedirectView

from .views import news, http404

urlpatterns = [
    path('news/', news, name='news'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', RedirectView.as_view(url='/news/'), name='index'),
    path('<path:path>', http404, name='http404'),
]
