
from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('popular/', views.JsonViewPopularMovies.as_view()),
    path('', views.JsonViewMovies.as_view())
]