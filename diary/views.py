from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import DiaryModelForm
from .models import Diary
from django.utils import timezone


def today():
    return timezone.localtime(timezone.now()).date()


class DiaryListView(LoginRequiredMixin, ListView):
    model = Diary
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().filter(created_by=self.request.user).order_by('-date', '-id')
        return queryset


class DiaryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'diary/diary_form.html'
    form_class = DiaryModelForm
    success_url = reverse_lazy('diary:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = Diary(created_by=self.request.user, date=today())
        return kwargs


class DiaryUpdateView(LoginRequiredMixin, UpdateView):
    model = Diary
    form_class = DiaryModelForm
    success_url = reverse_lazy('diary:list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DiaryDeleteView(LoginRequiredMixin, DeleteView):
    model = Diary
    success_url = reverse_lazy('diary:list')
