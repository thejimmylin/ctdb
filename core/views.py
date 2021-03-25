from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from core.decorators import permission_required
from django.http.response import Http404
from django.urls import reverse

from .models import News
from .forms import NewsModelForm


@login_required
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


@login_required
@permission_required('news.add_news', raise_exception=True, exception=Http404)
def news_create(request):
    model = News
    instance = model(created_by=request.user)
    form_class = NewsModelForm
    success_url = reverse('news:news_list')
    form_buttons = ['create']
    template_name = 'news/news_form.html'
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
@permission_required('news.change_news', raise_exception=True, exception=Http404)
def news_update(request, pk):
    model = News
    instance = get_object_or_404(klass=model, pk=pk, created_by=request.user)
    form_class = NewsModelForm
    success_url = reverse('news:news_list')
    form_buttons = ['update']
    template_name = 'news/news_form.html'
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
@permission_required('news.news_archive', raise_exception=True, exception=Http404)
def news_delete(request, pk):
    model = News
    instance = get_object_or_404(klass=model, pk=pk, created_by=request.user)
    success_url = reverse('news:news_list')
    template_name = 'news/news_confirm_delete.html'
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    context = {'model': model}
    return render(request, template_name, context)
