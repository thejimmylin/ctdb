from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path, reverse_lazy

from .forms import EmailValidationOnForgotPasswordForm, LoginForm
from .views import profile_change, set_group, set_role, signup, signup_with_email

app_name = 'accounts'

# Built-in views from django.contrib.auth.urls with a little customization applied.
urlpatterns = [
    path('login/', LoginView.as_view(form_class=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(
        success_url=reverse_lazy('accounts:password_change_done')), name='password_change'
    ),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(
        form_class=EmailValidationOnForgotPasswordForm, success_url=reverse_lazy('accounts:password_reset_done')), name='password_reset'
    ),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'
    ),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# Custom views about signup.
urlpatterns += [
    path('signup/', signup, name='signup'),
    path(
        'signup/with-chief-email/',
        signup_with_email,
        kwargs={'email_endswith_strings': ['@chief.com.tw']},
        name='signup_with_chief_email'
    ),
]

# Custom views about user extending model - profile.
urlpatterns += [
    path('profile/', profile_change, name='profile_change'),
    path('set-group/<str:group_name>/', set_group, name='set_group'),
    path('set-role/<str:role_name>/', set_role, name='set_role'),
]
