from django.urls import path
from . import views
from .views import project,blog

urlpatterns = [
    path('', views.home),
    path('project/',project),
    path('blog/',blog),
    
    
]