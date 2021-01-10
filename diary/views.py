from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse('accounts:login'))
    return render(request, 'diary/index.html')


from django.utils import timezone
from django.views.generic.list import ListView

from .models import Diary

class DiaryListView(ListView):

    model = Diary
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context