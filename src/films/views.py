from django.shortcuts import render
from django.http import JsonResponse

def get_a_list_of_movies(request):
    return JsonResponse({'success': True, 'name': 'get_a_list_of_movies'})

def get_popular_movies(request):
    return JsonResponse({'success': True, 'name': 'get_popular_movies'})