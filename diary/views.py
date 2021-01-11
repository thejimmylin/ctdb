from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Diary


class DiaryListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('accounts:login')
    model = Diary
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().filter(created_by=self.request.user).order_by('date', 'id')
        return queryset


class DiaryCreateView(CreateView):
    model = Diary
    fields = ['date', 'todo', 'daily_record', 'daily_check', 'remark', 'created_by']
    success_url = reverse_lazy('diary:list')
