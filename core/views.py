from django.shortcuts import redirect, render
from django.urls import reverse


def news(request):
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    return render(request, 'news.html')
