from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from core.decorators import permission_required

from .forms import (IspGroupModelForm, IspModelForm,
                    PrefixListUpdateTaskModelForm)
from .models import Isp, IspGroup, PrefixListUpdateTask


@login_required
@permission_required('telecom.view_isp', raise_exception=True, exception=Http404)
def isp_list(request):
    model = Isp
    paginate_by = 5
    toolbar_actions = ['create']
    dropdown_actions = ['update', 'delete']
    template_name = 'telecom/isp_list.html'
    role = request.session.get('role', request.user.profile.get_default_role())
    is_supervisor = True
    qs = model.objects.filter(created_by__profile__department__name=role)
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
        'toolbar_actions': toolbar_actions,
        'dropdown_actions': dropdown_actions,
    }
    return render(request, template_name, context)


@login_required
@permission_required('telecom.add_isp', raise_exception=True, exception=Http404)
def isp_create(request):
    model = Isp
    instance = model(created_by=request.user)
    form_class = IspModelForm
    success_url = reverse('telecom:isp_list')
    form_buttons = ['create']
    template_name = 'telecom/isp_form.html'
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
@permission_required('telecom.change_isp', raise_exception=True, exception=Http404)
def isp_update(request, pk):
    model = Isp
    instance = get_object_or_404(klass=model, pk=pk)
    form_class = IspModelForm
    success_url = reverse('telecom:isp_list')
    form_buttons = ['update']
    template_name = 'telecom/isp_form.html'
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
@permission_required('telecom.delete_isp', raise_exception=True, exception=Http404)
def isp_delete(request, pk):
    model = Isp
    instance = get_object_or_404(klass=model, pk=pk)
    success_url = reverse('telecom:isp_list')
    template_name = 'telecom/isp_confirm_delete.html'
    if instance.created_by != request.user:
        raise Http404
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    context = {'model': model}
    return render(request, template_name, context)


@login_required
@permission_required('telecom.view_ispgroup', raise_exception=True, exception=Http404)
def ispgroup_list(request):
    model = IspGroup
    paginate_by = 5
    toolbar_actions = ['create']
    dropdown_actions = ['update', 'delete']
    template_name = 'telecom/ispgroup_list.html'
    role = request.session.get('role', request.user.profile.get_default_role())
    is_supervisor = True
    qs = model.objects.filter(created_by__profile__department__name=role)
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
        'toolbar_actions': toolbar_actions,
        'dropdown_actions': dropdown_actions,
    }
    return render(request, template_name, context)


@login_required
@permission_required('telecom.add_ispgroup', raise_exception=True, exception=Http404)
def ispgroup_create(request):
    model = IspGroup
    instance = model(created_by=request.user)
    form_class = IspGroupModelForm
    success_url = reverse('telecom:ispgroup_list')
    form_buttons = ['create']
    template_name = 'telecom/ispgroup_form.html'
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
@permission_required('telecom.change_ispgroup', raise_exception=True, exception=Http404)
def ispgroup_update(request, pk):
    model = IspGroup
    instance = get_object_or_404(klass=model, pk=pk)
    form_class = IspGroupModelForm
    success_url = reverse('telecom:ispgroup_list')
    form_buttons = ['update']
    template_name = 'telecom/ispgroup_form.html'
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
@permission_required('telecom.delete_ispgroup', raise_exception=True, exception=Http404)
def ispgroup_delete(request, pk):
    model = IspGroup
    instance = get_object_or_404(klass=model, pk=pk)
    success_url = reverse('telecom:ispgroup_list')
    template_name = 'telecom/ispgroup_confirm_delete.html'
    if instance.created_by != request.user:
        raise Http404
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    context = {'model': model}
    return render(request, template_name, context)


@login_required
@permission_required('telecom.view_prefixlistupdatetask', raise_exception=True, exception=Http404)
def prefixlistupdatetask_list(request):
    model = PrefixListUpdateTask
    paginate_by = 5
    toolbar_actions = ['create']
    dropdown_actions = ['update', 'delete']
    template_name = 'telecom/prefixlistupdatetask_list.html'
    role = request.session.get('role', request.user.profile.get_default_role())
    is_supervisor = True
    qs = model.objects.filter(created_by__profile__department__name=role)
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
        'toolbar_actions': toolbar_actions,
        'dropdown_actions': dropdown_actions,
    }
    return render(request, template_name, context)


@login_required
@permission_required('telecom.add_prefixlistupdatetask', raise_exception=True, exception=Http404)
def prefixlistupdatetask_create(request):
    model = PrefixListUpdateTask
    instance = model(created_by=request.user)
    form_class = PrefixListUpdateTaskModelForm
    success_url = reverse('telecom:prefixlistupdatetask_list')
    form_buttons = ['create']
    template_name = 'telecom/prefixlistupdatetask_form.html'
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
@permission_required('telecom.change_prefixlistupdatetask', raise_exception=True, exception=Http404)
def prefixlistupdatetask_update(request, pk):
    model = PrefixListUpdateTask
    instance = get_object_or_404(klass=model, pk=pk)
    form_class = PrefixListUpdateTaskModelForm
    success_url = reverse('telecom:prefixlistupdatetask_list')
    form_buttons = ['update']
    template_name = 'telecom/prefixlistupdatetask_form.html'
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
@permission_required('telecom.delete_prefixlistupdatetask', raise_exception=True, exception=Http404)
def prefixlistupdatetask_delete(request, pk):
    model = PrefixListUpdateTask
    instance = get_object_or_404(klass=model, pk=pk)
    success_url = reverse('telecom:prefixlistupdatetask_list')
    template_name = 'telecom/prefixlistupdatetask_confirm_delete.html'
    if instance.created_by != request.user:
        raise Http404
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    context = {'model': model}
    return render(request, template_name, context)
