from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http.response import Http404
from django.shortcuts import render

from core.decorators import permission_required

from .models import Log

User = get_user_model()


@login_required
@permission_required('log.view_log', raise_exception=True, exception=Http404)
def diary_log_list(request):
    model = Log
    paginate_by = 5
    toolbar_actions = ['create']
    dropdown_actions = ['update', 'delete']
    template_name = 'log/diary_log_list.html'
    group = request.session.get('group', request.user.profile.get_default_group_name())
    is_supervisor = request.user.groups.filter(name='Supervisors').exists()
    if is_supervisor:
        qs = model.objects.filter(created_by__groups__name=group)
    else:
        qs = model.objects.filter(created_by=request.user)
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
