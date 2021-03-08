from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from .models import Email, ContactTask


def email_list(request):
    model = Email
    use_pagination = True
    paginate_by = 5
    template_name = 'telecom/email_list.html'
    order_by = ('-id', )
    if not request.user.is_authenticated:
        return redirect(f'{reverse("accounts:login")}?next={request.path}')
    qs = model.objects.all()
    qs_ordered = qs.order_by(*order_by)
    paginator = Paginator(qs_ordered, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if str(page_number).lower() == 'all':
        is_paginated = False
    else:
        is_paginated = use_pagination and page_obj.has_other_pages()
    object_list = page_obj if is_paginated else qs_ordered
    context = {'page_obj': page_obj, 'object_list': object_list, 'is_paginated': is_paginated, }
    return render(request, template_name, context)


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
