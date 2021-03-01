
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_a_list_of_movies),
    path('popular', views.get_popular_movies)
]