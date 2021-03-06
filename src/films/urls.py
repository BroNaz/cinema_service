
from django.urls import path, include, re_path

from . import views

urlpatterns = [
    re_path('$', views.JsonViewMovies.as_view()),
    path('popular', views.JsonViewPopularMovies.as_view())
]