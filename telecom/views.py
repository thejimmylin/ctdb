from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.core.paginator import Paginator

from .models import Email, ContactTask
from .forms import EmailModelForm


def email_list(request):
    model = Email
    use_pagination = True
    paginate_by = 5
    template_name = 'telecom/email_list.html'
    order_by = ('-id', )
    if not request.user.is_authenticated:
        return redirect(f'{reverse("accounts:login")}?next={request.path}')
    qs = model.objects.all().order_by(*order_by)
    paginator = Paginator(qs, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if str(page_number).lower() == 'all':
        is_paginated = False
    else:
        is_paginated = use_pagination and page_obj.has_other_pages()
    object_list = page_obj if is_paginated else qs
    context = {'page_obj': page_obj, 'object_list': object_list, 'is_paginated': is_paginated, }
    return render(request, template_name, context)


def email_create(request):
    form_class = EmailModelForm
    template_name = 'telecom/email_form.html'
    success_url = reverse('telecom:email_list')
    action = 'create'
    if not request.user.is_authenticated:
        return redirect(f'{reverse("accounts:login")}?next={request.path}')
    if request.method == 'POST':
        instance = Email(created_by=request.user)
        form = form_class(data=request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()
            return redirect(success_url)
        context = {'form': form, 'action': action}
        return render(request, template_name, context)
    form = form_class()
    context = {'form': form, 'action': action}
    return render(request, template_name, context)


def email_update(request, pk):
    model = Email
    form_class = EmailModelForm
    template_name = 'telecom/email_form.html'
    success_url = reverse('telecom:email_list')
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


def email_delete(request, pk):
    model = Email
    template_name = 'telecom/email_confirm_delete.html'
    success_url = reverse('telecom:email_list')
    if not request.user.is_authenticated:
        return redirect(f'{reverse("accounts:login")}?next={request.path}')
    instance = get_object_or_404(klass=model, pk=pk)
    if instance.created_by != request.user:
        return HttpResponseNotFound('')
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    return render(request, template_name)


def contacttask_list(request):
    use_pagination = True
    paginate_by = 5
    template_name = 'telecom/contacttask_list.html'
    if not request.user.is_authenticated:
        return redirect(f'{reverse("accounts:login")}?next={request.path}')
    role = get_role(request)  # NOQA, to be used
    contacttasks = ContactTask.objects.all()
    paginator = Paginator(contacttasks, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # temp solution for "all pages" view.
    if str(page_number).lower() == 'all':
        is_paginated = False
    else:
        is_paginated = use_pagination and page_obj.has_other_pages()
    object_list = page_obj if is_paginated else contacttasks
    context = {'page_obj': page_obj, 'object_list': object_list, 'is_paginated': is_paginated}
    return render(request, template_name, context)
