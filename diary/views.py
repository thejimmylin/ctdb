from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import DiaryModelForm
from .models import Diary


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


def diary_update(request, pk):
    model = Diary
    form_class = DiaryModelForm
    template_name = 'diary/diary_form.html'
    success_url = reverse('diary:list')
    if not request.user.is_authenticated:
        return redirect(f'{reverse("accounts:login")}?next={request.path}')
    instance = get_object_or_404(klass=model, pk=pk)
    if instance.created_by != request.user:
        return HttpResponseNotFound('')
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    form = form_class(instance=instance)
    context = {'form': form}
    return render(request, template_name, context)


def diary_delete(request, pk):
    model = Diary
    template_name = 'diary/diary_confirm_delete.html'
    success_url = reverse('diary:list')
    if not request.user.is_authenticated:
        return redirect(f'{reverse("accounts:login")}?next={request.path}')
    instance = get_object_or_404(klass=model, pk=pk)
    if instance.created_by != request.user:
        return HttpResponseNotFound('')
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    return render(request, template_name)
