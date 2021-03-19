from django.shortcuts import render


def news(request):
    return render(request, 'news.html')


def http404(request, path):
    context = {'path': path}
    return render(request, 'http404.html', context)
