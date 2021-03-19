from django.shortcuts import render, redirect
from django.urls import reverse


def news(request):
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    return render(request, 'news.html')


def http404(request, path):
    context = {'path': path}
    return render(request, 'http404.html', context)
