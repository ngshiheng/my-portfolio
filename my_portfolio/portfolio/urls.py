from django.urls import path
from . import views
from .views import ProjectListView

urlpatterns = [
    path('', ProjectListView.as_view(), name='portfolio-index'),
]