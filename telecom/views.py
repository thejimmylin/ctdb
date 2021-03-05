from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.core.paginator import Paginator

from .forms import ContactTaskModelForm
from .models import ContactTask
from accounts.views import get_role


def diary_list(request):
    use_pagination = True
    paginate_by = 5
    template_name = 'telecom/contacttask_list.html'
    if not request.user.is_authenticated:
        return redirect(f'{reverse("accounts:login")}?next={request.path}')
    user = request.user
    role = get_role(request)  # NOQA, to be used
    is_supervisor = user.groups.filter(name='Supervisors').exists()
    if is_supervisor:
        diaries = Diary.objects.filter(created_by__profile__department__name__in=[role])
    else:
        diaries = Diary.objects.filter(created_by=user)
    diaries = diaries.distinct().order_by('-date', '-id')
    paginator = Paginator(diaries, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # temp solution for "all pages" view.
    if str(page_number).lower() == 'all':
        is_paginated = False
    else:
        is_paginated = use_pagination and page_obj.has_other_pages()
    object_list = page_obj if is_paginated else diaries
    context = {'page_obj': page_obj, 'object_list': object_list, 'is_paginated': is_paginated, 'is_supervisor': is_supervisor, }
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
