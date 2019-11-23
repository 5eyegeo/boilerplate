from django.shortcuts import render


def handler404(request, *args, **kwargs):
    return render(request, 'error-pages/404.html', status=404)


def index(request):
    return render(request, 'index.html', {})
