# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('git-history', views.get_git_history, name='view_git_history'),
]
