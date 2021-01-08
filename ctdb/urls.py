from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.conf import settings
from accounts.forms import LoginForm

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('accounts.urls')),
    path('', LoginView.as_view(form_class=LoginForm, template_name='index.html'), name='index'),
]

if settings.DEBUG:
    urlpatterns += [
        path('admin/', admin.site.urls),
    ]
