from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from .forms import SignUpWithEmailForm, ProfileForm

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


def profile_change(request):
    """
    A profile change view.
    """
    if not request.user.is_authenticated:
        return redirect(reverse('accounts:login'))
    instance = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            # messages.success(request, _('Changed successfully.'))  The template is not ready (message div covered.)
            return redirect(reverse('accounts:profile_change'))
    else:
        form = ProfileForm(instance=instance)
    context = {
        'form': form,
    }
    return render(request, 'registration/profile_change.html', context)


def set_role(request, role):
    """
    A set role view.
    """
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    if role not in [dep.name for dep in request.user.profile.department.all()]:
        messages.add_message(request, messages.ERROR, _('You have no access to this role.'))
        return redirect(reverse('index'))
    request.session['role'] = role
    return redirect(reverse('index'))


def get_role(request):
    """
    Not a view. This function get the role for a given request.
    It detects the role set in session of the request. If there's not one,
    use the first result of profile-department of user.
    """
    user = request.user
    departments = user.profile.department.all()
    default_role = departments.first().name if departments.exists() else ''
    role = request.session.get('role', default_role)
    return role
