from django.urls import path
from django.views.generic import RedirectView

from .views import about

urlpatterns = [
    path('about/', about, name='about'),
    path('', RedirectView.as_view(url='diary/diaries/'), name='index'),
]
