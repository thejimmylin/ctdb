from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from core.decorators import permission_required

from .forms import ArchiveModelForm
from .models import Archive


@login_required
@permission_required('archive.view_archive', raise_exception=True, exception=Http404)
def archive_list(request):
    model = Archive
    order_by = ['-pk']
    use_pagination = True
    paginate_by = 5
    template_name = 'archive/archive_list.html'
    dropdown_actions = ['update', 'delete']
    role = request.session.get('role', request.user.profile.get_default_role())
    is_supervisor = request.user.groups.filter(name='Supervisors').exists()
    if is_supervisor:
        qs = model.objects.filter(created_by__profile__department__name=role)
    else:
        qs = model.objects.filter(created_by=request.user)
    qs_ordered = qs.order_by(*order_by)
    paginator = Paginator(qs_ordered, paginate_by)
    page_number = request.GET.get('page')
    if str(page_number).lower() == 'all':
        is_paginated = False
    else:
        page_obj = paginator.get_page(page_number)
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


@login_required
@permission_required('archive.add_archive', raise_exception=True, exception=Http404)
def archive_create(request):
    model = Archive
    instance = model(created_by=request.user)
    form_class = ArchiveModelForm
    success_url = reverse('archive:archive_list')
    template_name = 'archive/archive_form.html'
    form_buttons = ['create']
    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
        context = {'model': model, 'form': form, 'form_buttons': form_buttons}
        return render(request, template_name, context)
    form = form_class()
    context = {'model': model, 'form': form, 'form_buttons': form_buttons}
    return render(request, template_name, context)


@login_required
@permission_required('archive.change_archive', raise_exception=True, exception=Http404)
def archive_update(request, pk):
    model = Archive
    instance = get_object_or_404(klass=model, pk=pk)
    form_class = ArchiveModelForm
    success_url = reverse('archive:archive_list')
    template_name = 'archive/archive_form.html'
    form_buttons = ['update']
    if instance.created_by != request.user:
        raise Http404
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
@permission_required('archive.delete_archive', raise_exception=True, exception=Http404)
def archive_delete(request, pk):
    model = Archive
    instance = get_object_or_404(klass=model, pk=pk)
    success_url = reverse('archive:archive_list')
    template_name = 'archive/archive_confirm_delete.html'
    if instance.created_by != request.user:
        raise Http404
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    context = {'model': model}
    return render(request, template_name, context)
