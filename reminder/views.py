from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from accounts.models import get_role
from core.decorators import permission_required
from core.utils import remove_unnecessary_seperator

from .forms import ReminderModelForm
from .models import Reminder


def get_reminder_queryset(request):
    """
    The queryset of model `Reminder` with filter depending on user's role/identity/group.
    The views below will use this as a basic queryset. This ensures that users won't
    accidentally see or touch those they shouldn't.
    """
    model = Reminder
    queryset = model.objects.all()
    role = get_role(user=request.user, session=request.session)
    if not role:
        return queryset.filter(created_by=request.user)
    supervise_roles = role.groupprofile.supervise_roles.all()
    if not supervise_roles:
        return queryset.filter(created_by=request.user)
    return queryset.filter(created_by__groups__in=supervise_roles).distinct()


@login_required
@permission_required('reminder.view_reminder', raise_exception=True, exception=Http404)
def reminder_list(request):
    model = Reminder
    queryset = get_reminder_queryset(request)
    paginate_by = 5
    template_name = 'reminder/reminder_list.html'
    page_number = request.GET.get('page', '')
    paginator = Paginator(queryset, paginate_by)
    page_obj = paginator.get_page(page_number)
    is_paginated = page_number.lower() != 'all' and page_obj.has_other_pages()
    context = {
        'model': model,
        'page_obj': page_obj,
        'object_list': page_obj if is_paginated else queryset,
        'is_paginated': is_paginated,
    }
    return render(request, template_name, context)


@login_required
@permission_required('reminder.add_reminder', raise_exception=True, exception=Http404)
def reminder_create(request):
    model = Reminder
    instance = model(created_by=request.user)
    form_class = ReminderModelForm
    success_url = reverse('reminder:reminder_list')
    form_buttons = ['create']
    template_name = 'reminder/reminder_form.html'
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
@permission_required('reminder.change_reminder', raise_exception=True, exception=Http404)
def reminder_update(request, pk):
    model = Reminder
    queryset = get_reminder_queryset(request)
    instance = get_object_or_404(klass=queryset, pk=pk, created_by=request.user)
    form_class = ReminderModelForm
    success_url = reverse('reminder:reminder_list')
    form_buttons = ['update']
    template_name = 'reminder/reminder_form.html'
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
@permission_required('reminder.delete_reminder', raise_exception=True, exception=Http404)
def reminder_delete(request, pk):
    model = Reminder
    queryset = get_reminder_queryset(request)
    instance = get_object_or_404(klass=queryset, pk=pk, created_by=request.user)
    success_url = reverse('reminder:reminder_list')
    template_name = 'reminder/reminder_confirm_delete.html'
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    context = {'model': model}
    return render(request, template_name, context)


@login_required
@permission_required('reminder.change_reminder', raise_exception=True, exception=Http404)
def reminder_clone(request, pk):
    model = Reminder
    queryset = get_reminder_queryset(request)
    instance = get_object_or_404(klass=queryset, pk=pk, created_by=request.user)
    instance.pk = None
    form_class = ReminderModelForm
    success_url = reverse('reminder:reminder_list')
    form_buttons = ['create']
    template_name = 'reminder/reminder_form.html'
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
@permission_required('reminder.change_reminder', raise_exception=True, exception=Http404)
def reminder_send_email(request, pk):
    model = Reminder
    queryset = get_reminder_queryset(request)
    instance = get_object_or_404(klass=queryset, pk=pk, created_by=request.user)
    success_url = reverse('reminder:reminder_list')
    template_name = 'reminder/reminder_confirm_send_email.html'
    if request.method == 'POST':
        s = remove_unnecessary_seperator(instance.recipients, ';')
        recipient_list = list(map(str.strip, s.split(';')))
        send_mail(
            subject=instance.email_subject,
            message=instance.email_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        return redirect(success_url)
    context = {'model': model}
    return render(request, template_name, context)
