from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse


from .forms import DiaryModelForm
from .models import Diary
from accounts.views import get_role


def diary_list(request):
    template_name = 'diary/diary_list.html'
    if not request.user.is_authenticated:
        return redirect(f'{reverse("accounts:login")}?next={request.path}')
    role = get_role(request)
    print(role)
    diaries = Diary.objects.filter(created_by=request.user).order_by('-date', '-id')
    paginator = Paginator(diaries, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'object_list': page_obj, 'is_paginated': True, }
    return render(request, template_name, context)


def diary_create(request):
    form_class = DiaryModelForm
    template_name = 'diary/diary_form.html'
    success_url = reverse('diary:list')
    action = 'create'
    if not request.user.is_authenticated:
        return redirect(f'{reverse("accounts:login")}?next={request.path}')
    if request.method == 'POST':
        instance = Diary(created_by=request.user)
        form = form_class(data=request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()
            return redirect(success_url)
        context = {'form': form, 'action': action}
        return render(request, template_name, context)
    form = form_class()
    context = {'form': form, 'action': action}
    return render(request, template_name, context)


def diary_update(request, pk):
    model = Diary
    form_class = DiaryModelForm
    template_name = 'diary/diary_form.html'
    success_url = reverse('diary:list')
    action = 'update'
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
        context = {'form': form, 'action': action}
        return render(request, template_name, context)
    form = form_class(instance=instance)
    context = {'form': form, 'action': action}
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
