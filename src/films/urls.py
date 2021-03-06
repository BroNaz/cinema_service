
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.FilmsView.as_view(), name='films'),
    path('popular', views.get_popular_movies)
]