import json
from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.paginator import Paginator

from .models import Log
from accounts.views import get_role
from django.contrib.auth import get_user_model


User = get_user_model()


def filter_jsonfield(qs, jsonfield_name, *args, **kwargs):
    """
    Filtering..
    """
    return qs


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
    qs = model.objects.all().order_by(*order_by).values()
    """
    To be refactored.
    """
    object_list = []
    if is_supervisor:
        for instance in qs:
            data_as_dict = json.loads(instance['data'])
            try:
                created_by = User.objects.get(id=data_as_dict.get('created_by'))
            except User.DoesNotExist as e:
                print(e)
            else:
                dep_names = [dep.name for dep in created_by.profile.department.all()]
                if role in dep_names:
                    object_list.append(instance)
    else:
        for instance in qs:
            data_as_dict = json.loads(instance['data'])
            if data_as_dict.get('created_by') == request.user.id:
                object_list.append(instance)
    map(lambda obj: instance.update({'data_as_dict': json.loads(obj['data'])}), object_list)
    """
    To be refactored.
    """
    paginator = Paginator(object_list, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # temp solution for "all pages" view.
    if str(page_number).lower() == 'all':
        is_paginated = False
    else:
        is_paginated = use_pagination and page_obj.has_other_pages()
    object_list = page_obj if is_paginated else object_list
    context = {'page_obj': page_obj, 'object_list': object_list, 'is_paginated': is_paginated, 'is_supervisor': is_supervisor, }
    return render(request, template_name, context)
