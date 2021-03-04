from django.urls import path
from .views import about
from django.views.generic import RedirectView

urlpatterns = [
    path('about/', about, name='about'),
    path('', RedirectView.as_view(url='diary/diaries/'), name='index'),
]
