from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from core.decorators import permission_required

from .forms import DiaryModelForm
from .models import Diary


@login_required
@permission_required('diary.view_diary', raise_exception=True, exception=Http404)
def diary_list(request):
    model = Diary
    paginate_by = 5
    template_name = 'diary/diary_list.html'
    group = request.session.get('group', request.user.profile.get_default_group_name())
    is_supervisor = request.user.groups.filter(name='Supervisors').exists()
    if is_supervisor:
        qs = model.objects.filter(created_by__groups__name=group)
    else:
        qs = model.objects.filter(created_by=request.user)
    page_number = request.GET.get('page', '')
    paginator = Paginator(qs, paginate_by)
    page_obj = paginator.get_page(page_number)
    is_paginated = page_number.lower() != 'all' and page_obj.has_other_pages()
    context = {
        'model': model,
        'page_obj': page_obj,
        'object_list': page_obj if is_paginated else qs,
        'is_paginated': is_paginated,
        'is_supervisor': is_supervisor,
    }
    return render(request, template_name, context)


@login_required
@permission_required('diary.add_diary', raise_exception=True, exception=Http404)
def diary_create(request):
    model = Diary
    instance = model(created_by=request.user)
    form_class = DiaryModelForm
    success_url = reverse('diary:diary_list')
    form_buttons = ['create']
    template_name = 'diary/diary_form.html'
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
        context = {'model': model, 'form': form, 'form_buttons': form_buttons}
        return render(request, template_name, context)
    form = form_class()
    context = {'model': model, 'form': form, 'form_buttons': form_buttons}
    return render(request, template_name, context)


@login_required
@permission_required('diary.change_diary', raise_exception=True, exception=Http404)
def diary_update(request, pk):
    model = Diary
    instance = get_object_or_404(klass=model, pk=pk, created_by=request.user)
    form_class = DiaryModelForm
    success_url = reverse('diary:diary_list')
    form_buttons = ['update']
    template_name = 'diary/diary_form.html'
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
        context = {'model': model, 'form': form, 'form_buttons': form_buttons}
        return render(request, template_name, context)
    form = form_class(instance=instance)
    context = {'model': model, 'form': form, 'form_buttons': form_buttons}
    return render(request, template_name, context)


@login_required
@permission_required('diary.diary_archive', raise_exception=True, exception=Http404)
def diary_delete(request, pk):
    model = Diary
    instance = get_object_or_404(klass=model, pk=pk, created_by=request.user)
    success_url = reverse('diary:diary_list')
    template_name = 'diary/diary_confirm_delete.html'
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    context = {'model': model}
    return render(request, template_name, context)
