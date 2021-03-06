from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic

from .models import Film

def get_a_list_of_movies(request):
    return JsonResponse({'success': True, 'name': 'get_a_list_of_movies'})

def get_popular_movies(request):
    return JsonResponse({'success': True, 'name': 'get_popular_movies'})


class FilmsView(generic.ListView):
    model = Film
    paginate_by = 10

    def get():
        return JsonResponse({'successGet': True})