from django.shortcuts import render
from django.views.generic import ListView
from .models import Project


def profile(request):
    return render(request, 'portfolio/index.html', {'title': 'Jerry\'s Portfolio'})


class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/index.html'
    context_object_name = 'projects'


