from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ProfileForm, SignUpWithEmailForm
from .models import Profile

User = get_user_model()


def signup(request):
    """
    A lobby view of signup.
    """
    return render(request, 'registration/signup.html')


# This view doesn't be used in urls.py.
def signup_with_account_and_password(request):
    """
    A standard signup view.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/signup_with_account_and_password.html', context)


def signup_with_email(request, email_endswith_strings=[], email_cant_endswith_strings=[]):
    """
    A signup view letting user sign up with Email.
    A user provides a Email and we generate a random uuid string as password,
    and then send a Email containing these info to the user.
    """
    if request.method == 'POST':
        form = SignUpWithEmailForm(
            data=request.POST,
            email_endswith_strings=email_endswith_strings,
            email_cant_endswith_strings=email_cant_endswith_strings,
        )
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:password_reset_done'))
    else:
        form = SignUpWithEmailForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/signup_with_email.html', context)


@login_required
def profile_change(request):
    """
    A profile change view.
    """
    model = Profile
    instance = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:profile_change'))
    else:
        form = ProfileForm(instance=instance)
    context = {
        'model': model,
        'form': form,
        'form_buttons': ('save_and_continue_editing', ),
    }
    return render(request, 'registration/profile_change.html', context)


@login_required
def role_change(request, pk):
    queryset = request.user.groups.filter(groupprofile__is_role=True, groupprofile__is_displayed=True)
    role = get_object_or_404(klass=queryset, pk=pk)
    request.user.profile.activated_role = role
    request.user.profile.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))
