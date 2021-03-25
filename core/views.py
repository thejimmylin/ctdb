from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.decorators import permission_required
from django.http.response import Http404


@login_required
@permission_required('new.view_new', raise_exception=True, exception=Http404)
def news_list(request):
    return render(request, 'news.html')
