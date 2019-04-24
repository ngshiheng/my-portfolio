from django.shortcuts import render


def profile(request):
    return render(request, 'portfolio/index.html', {'title': 'About Jerry'})
