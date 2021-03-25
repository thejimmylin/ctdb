from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator
from core.decorators import permission_required
from django.http.response import Http404

from .models import News


@login_required
@permission_required('new.view_new', raise_exception=True, exception=Http404)
def news_list(request):
    model = News
    paginate_by = 5
    template_name = 'news_list.html'
    is_supervisor = True
    qs = News.objects.all()
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
    }
    return render(request, template_name, context)
