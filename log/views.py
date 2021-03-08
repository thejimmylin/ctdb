import json
from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.paginator import Paginator

from .models import Log
from accounts.views import get_role
from django.contrib.auth import get_user_model


User = get_user_model()


def diary_log_list(request):
    model = Log
    use_pagination = True
    paginate_by = 5
    template_name = 'log/diary_log_list.html'
    order_by = ('-id', )
    if not request.user.is_authenticated:
        return redirect(f'{reverse("accounts:login")}?next={request.path}')
    role = get_role(request)  # NOQA, to be used
    is_supervisor = request.user.groups.filter(name='Supervisors').exists()
    qs = model.objects.all()
    qs_ordered = qs.order_by(*order_by)
    """
    To be refactored.
    """
    diary_logs = qs_ordered.values()
    available_diary_logs = []
    if is_supervisor:
        for diary_log in diary_logs:
            data_as_dict = json.loads(diary_log['data'])
            try:
                created_by = User.objects.get(id=data_as_dict.get('created_by'))
            except User.DoesNotExist as e:
                print(e)
            else:
                dep_names = [dep.name for dep in created_by.profile.department.all()]
                if role in dep_names:
                    available_diary_logs.append(diary_log)
    else:
        for diary_log in diary_logs:
            data_as_dict = json.loads(diary_log['data'])
            if data_as_dict.get('created_by') == request.user.id:
                available_diary_logs.append(diary_log)
    for diary_log in available_diary_logs:
        data_as_dict = json.loads(diary_log['data'])
        diary_log['data_as_dict'] = data_as_dict
    """
    To be refactored.
    """
    paginator = Paginator(available_diary_logs, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # temp solution for "all pages" view.
    if str(page_number).lower() == 'all':
        is_paginated = False
    else:
        is_paginated = use_pagination and page_obj.has_other_pages()
    object_list = page_obj if is_paginated else available_diary_logs
    context = {'page_obj': page_obj, 'object_list': object_list, 'is_paginated': is_paginated, 'is_supervisor': is_supervisor, }
    return render(request, template_name, context)
