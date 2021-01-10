from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse('accounts:login'))
    return render(request, 'diary/index.html')
