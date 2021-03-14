from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from django.urls import reverse
from .models import Reminder
from .forms import ReminderModelForm
from django.core.paginator import Paginator
from accounts.views import get_role
from django.core.mail import send_mail


def reminder_list(request):
    model = Reminder
    use_pagination = True
    paginate_by = 5
    template_name = 'reminder/reminder_list.html'
    order_by = ('-pk', )
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    role = get_role(request)
    qs = model.objects.filter(created_by__profile__department__name=role)
    qs_ordered = qs.order_by(*order_by)
    paginator = Paginator(qs_ordered, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if str(page_number).lower() == 'all':
        is_paginated = False
    else:
        is_paginated = use_pagination and page_obj.has_other_pages()
    object_list = page_obj if is_paginated else qs_ordered
    context = {'model': model, 'page_obj': page_obj, 'object_list': object_list, 'is_paginated': is_paginated}
    return render(request, template_name, context)


def reminder_create(request):
    model = Reminder
    form_class = ReminderModelForm
    template_name = 'reminder/reminder_form.html'
    success_url = reverse('reminder:reminder_list')
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


def reminder_update(request, pk):
    model = Reminder
    form_class = ReminderModelForm
    template_name = 'reminder/reminder_form.html'
    success_url = reverse('reminder:reminder_list')
    form_buttons = ['update']
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    instance = get_object_or_404(klass=model, pk=pk)
    if instance.created_by != request.user:
        return HttpResponseNotFound('')
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


def reminder_delete(request, pk):
    model = Reminder
    template_name = 'reminder/reminder_confirm_delete.html'
    success_url = reverse('reminder:reminder_list')
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    instance = get_object_or_404(klass=model, pk=pk)
    if instance.created_by != request.user:
        return HttpResponseNotFound('')
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    context = {'model': model}
    return render(request, template_name, context)


def reminder_send_email(request, pk):
    model = Reminder
    template_name = 'reminder/reminder_confirm_send_email.html'
    success_url = reverse('reminder:reminder_list')
    if not request.user.is_authenticated:
        return redirect(reverse("accounts:login") + '?next=' + request.get_full_path())
    instance = get_object_or_404(klass=model, pk=pk)
    if instance.created_by != request.user:
        return HttpResponseNotFound('')
    if request.method == 'POST':
        recipients = instance.recipients
        recipients = recipients[:-1] if recipients[-1:] == ';' else recipients
        recipient_list = list(map(str.strip, recipients.split(';')))
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
