from django.shortcuts import render


def homepage(request):
    return render(request, 'index.html')


def handler404(request, exception):
    return render(request, 'errors/404.html', {'error': exception})
