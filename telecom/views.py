from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import (IspGroupModelForm, IspModelForm,
                    PrefixListUpdateTaskModelForm)
from .models import Isp, IspGroup, PrefixListUpdateTask


def isp_list(request):
    model = Isp
    use_pagination = True
    paginate_by = 5
    template_name = 'telecom/isp_list.html'
    order_by = ('-pk', )
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    qs = model.objects.all().order_by(*order_by)
    paginator = Paginator(qs, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if str(page_number).lower() == 'all':
        is_paginated = False
    else:
        is_paginated = use_pagination and page_obj.has_other_pages()
    object_list = page_obj if is_paginated else qs
    context = {'model': model, 'page_obj': page_obj, 'object_list': object_list, 'is_paginated': is_paginated, }
    return render(request, template_name, context)


def isp_create(request):
    model = Isp
    form_class = IspModelForm
    template_name = 'telecom/isp_form.html'
    success_url = reverse('telecom:isp_list')
    form_buttons = ['create']
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    if request.method == 'POST':
        instance = model(created_by=request.user)
        form = form_class(data=request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()
            return redirect(success_url)
        context = {'model': model, 'form': form, 'form_buttons': form_buttons}
        return render(request, template_name, context)
    form = form_class()
    context = {'model': model, 'form': form, 'form_buttons': form_buttons}
    return render(request, template_name, context)


def isp_update(request, pk):
    model = Isp
    form_class = IspModelForm
    template_name = 'telecom/isp_form.html'
    success_url = reverse('telecom:isp_list')
    form_buttons = ['update']
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
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


def isp_delete(request, pk):
    model = Isp
    template_name = 'telecom/isp_confirm_delete.html'
    success_url = reverse('telecom:isp_list')
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    instance = get_object_or_404(klass=model, pk=pk)
    if instance.created_by != request.user:
        return http404(request, path=request.path[1:])
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    context = {'model': model}
    return render(request, template_name, context)


def ispgroup_list(request):
    model = IspGroup
    use_pagination = True
    paginate_by = 5
    template_name = 'telecom/ispgroup_list.html'
    order_by = ('-pk', )
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    qs = model.objects.all().order_by(*order_by)
    paginator = Paginator(qs, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if str(page_number).lower() == 'all':
        is_paginated = False
    else:
        is_paginated = use_pagination and page_obj.has_other_pages()
    object_list = page_obj if is_paginated else qs
    context = {'model': model, 'page_obj': page_obj, 'object_list': object_list, 'is_paginated': is_paginated, }
    return render(request, template_name, context)


def ispgroup_create(request):
    model = IspGroup
    form_class = IspGroupModelForm
    template_name = 'telecom/ispgroup_form.html'
    success_url = reverse('telecom:ispgroup_list')
    form_buttons = ['create']
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    if request.method == 'POST':
        instance = model(created_by=request.user)
        form = form_class(data=request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()
            return redirect(success_url)
        context = {'model': model, 'form': form, 'form_buttons': form_buttons}
        return render(request, template_name, context)
    form = form_class()
    context = {'model': model, 'form': form, 'form_buttons': form_buttons}
    return render(request, template_name, context)


def ispgroup_update(request, pk):
    model = IspGroup
    form_class = IspGroupModelForm
    template_name = 'telecom/ispgroup_form.html'
    success_url = reverse('telecom:ispgroup_list')
    form_buttons = ['update']
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
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


def ispgroup_delete(request, pk):
    model = IspGroup
    template_name = 'telecom/ispgroup_confirm_delete.html'
    success_url = reverse('telecom:ispgroup_list')
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    instance = get_object_or_404(klass=model, pk=pk)
    if instance.created_by != request.user:
        return http404(request, path=request.path[1:])
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    context = {'model': model}
    return render(request, template_name, context)


def prefixlistupdatetask_list(request):
    model = PrefixListUpdateTask
    use_pagination = True
    paginate_by = 5
    template_name = 'telecom/prefixlistupdatetask_list.html'
    order_by = ('-pk', )
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    qs = model.objects.all().order_by(*order_by)
    paginator = Paginator(qs, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if str(page_number).lower() == 'all':
        is_paginated = False
    else:
        is_paginated = use_pagination and page_obj.has_other_pages()
    object_list = page_obj if is_paginated else qs
    context = {'model': model, 'page_obj': page_obj, 'object_list': object_list, 'is_paginated': is_paginated, }
    return render(request, template_name, context)


def prefixlistupdatetask_create(request):
    model = PrefixListUpdateTask
    form_class = PrefixListUpdateTaskModelForm
    template_name = 'telecom/prefixlistupdatetask_form.html'
    success_url = reverse('telecom:prefixlistupdatetask_list')
    form_buttons = ['create']
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    if request.method == 'POST':
        instance = model(created_by=request.user)
        form = form_class(data=request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()
            return redirect(success_url)
        context = {'model': model, 'form': form, 'form_buttons': form_buttons}
        return render(request, template_name, context)
    form = form_class()
    context = {'model': model, 'form': form, 'form_buttons': form_buttons}
    return render(request, template_name, context)


def prefixlistupdatetask_update(request, pk):
    model = PrefixListUpdateTask
    form_class = PrefixListUpdateTaskModelForm
    template_name = 'telecom/prefixlistupdatetask_form.html'
    success_url = reverse('telecom:prefixlistupdatetask_list')
    form_buttons = ['update']
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
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


def prefixlistupdatetask_delete(request, pk):
    model = PrefixListUpdateTask
    template_name = 'telecom/prefixlistupdatetask_confirm_delete.html'
    success_url = reverse('telecom:prefixlistupdatetask_list')
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    instance = get_object_or_404(klass=model, pk=pk)
    if instance.created_by != request.user:
        return http404(request, path=request.path[1:])
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    context = {'model': model}
    return render(request, template_name, context)
