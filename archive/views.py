from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from accounts.views import get_role
from core.views import http404

from .forms import ArchiveModelForm
from .models import Archive


@login_required
@permission_required('archive.archive_view')
def archive_list(request):
    model = Archive
    use_pagination = True
    paginate_by = 5
    template_name = 'archive/archive_list.html'
    order_by = ('-pk', )
    required_perms = []
    dropdown_actions = ['update', 'delete']
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    for perm in required_perms:
        if not request.user.has_perm(perm):
            return http404(request, path=request.path[1:])
    role = get_role(request)
    is_supervisor = request.user.groups.filter(name='Supervisors').exists()
    if is_supervisor:
        qs = model.objects.filter(created_by__profile__department__name=role)
    else:
        qs = model.objects.filter(created_by=request.user)
    qs_ordered = qs.order_by(*order_by)
    paginator = Paginator(qs_ordered, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if str(page_number).lower() == 'all':
        is_paginated = False
    else:
        is_paginated = use_pagination and page_obj.has_other_pages()
    object_list = page_obj if is_paginated else qs_ordered
    context = {
        'model': model,
        'page_obj': page_obj,
        'object_list': object_list,
        'is_paginated': is_paginated,
        'is_supervisor': is_supervisor,
        'dropdown_actions': dropdown_actions,
    }
    return render(request, template_name, context)


def archive_create(request):
    model = Archive
    form_class = ArchiveModelForm
    template_name = 'archive/archive_form.html'
    success_url = reverse('archive:archive_list')
    form_buttons = ['create']
    required_perms = [
        f'{model._meta.app_label}.{model._meta.model_name}_add',
    ]
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    for perm in required_perms:
        if not request.user.has_perm(perm):
            return http404(request, path=request.path[1:])
    if request.method == 'POST':
        instance = model(created_by=request.user)
        form = form_class(data=request.POST, files=request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save()
            return redirect(success_url)
        context = {'model': model, 'form': form, 'form_buttons': form_buttons, 'required_perms': required_perms}
        return render(request, template_name, context)
    form = form_class()
    context = {'model': model, 'form': form, 'form_buttons': form_buttons, 'required_perms': required_perms}
    return render(request, template_name, context)


def archive_update(request, pk):
    model = Archive
    form_class = ArchiveModelForm
    template_name = 'archive/archive_form.html'
    success_url = reverse('archive:archive_list')
    form_buttons = ['update']
    required_perms = [
        f'{model._meta.app_label}.{model._meta.model_name}_change',
    ]
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    for perm in required_perms:
        if not request.user.has_perm(perm):
            return http404(request, path=request.path[1:])
    instance = get_object_or_404(klass=model, pk=pk)
    if instance.created_by != request.user:
        return http404(request, path=request.path[1:])
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


def archive_delete(request, pk):
    model = Archive
    template_name = 'archive/archive_confirm_delete.html'
    success_url = reverse('archive:archive_list')
    required_perms = [
        f'{model._meta.app_label}.{model._meta.model_name}_delete',
    ]
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    for perm in required_perms:
        if not request.user.has_perm(perm):
            return http404(request, path=request.path[1:])
    instance = get_object_or_404(klass=model, pk=pk)
    if instance.created_by != request.user:
        return http404(request, path=request.path[1:])
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    context = {'model': model}
    return render(request, template_name, context)
