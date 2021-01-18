from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import DiaryModelForm
# from django.shortcuts import render, redirect
from .models import Diary


class DiaryListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('accounts:login')
    model = Diary
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().filter(created_by=self.request.user).order_by('-date', '-id')
        return queryset


class DiaryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'diary/diary_form.html'
    form_class = DiaryModelForm
    success_url = reverse_lazy('diary:list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


# def diary_create(request):
#     template = 'diary/diary_form.html'
#     form_class = DiaryModelForm
#     success_url = reverse_lazy('diary:list')
#     if not request.user.is_authenticated:
#         return redirect('accounts:login')
#     if request.method == 'POST':
#         diary = Diary(created_by=request.user)
#         form = form_class(request.POST, instance=diary)
#         if form.is_valid():
#             form.save()
#             return redirect(success_url)
#     form = form_class()
#     context = {
#         'form': form
#     }
#     return render(request, template, context)


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
