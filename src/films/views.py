from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json 
from django.views import generic
from django.core import serializers # вроде как его используют для сериализации, необходимо затестить
from django.views import View
from django.core import serializers

from .models import Film


class JsonViewMovies(View):
    """
    command for getting a list of movies with the possibility of pagination 
    and filters by actor, director, year.
    Pagination and filtering occurs by variables from the url, 
    namely "pagination" and " filter"

    pagination -> int 

    filter -> [actor, director, year]
    actor -> str 
    director -> str 
    year -> str (YYYY-MM-DD)
    """
    def get(self, request):
        """v0 - вернем пока что все фильмы"""
        resultset = Film.objects.all()
        results = [ob.as_json() for ob in resultset]
        return HttpResponse(json.dumps(results), content_type="application/json")


class JsonViewPopularMovies(View):
    def get(self, request):
        return JsonResponse({'some': 'data'})

