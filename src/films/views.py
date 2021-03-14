from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json 
from django.views import generic
from django.core import serializers
from django.views import View
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, Page

from .models import Film
from .managers import FilmManager, FilmInfoManager


class JsonViewMovies(View):
    """
    command for getting a list of movies with the possibility of pagination 
    and filters by actor, producer, year.
    Pagination and filtering occurs by variables from the url, 
    namely "pagination" and " filter"

    pagination -> int 

    actor -> str 
    producer -> str 
    year -> str (YYYY)
    """
    YOUR_PAGE_SIZE = 10
    def get(self, request):
        """v0 - вернем пока что все фильмы"""
        print('JsonViewMovies')
        resultset = FilmManager(request).get_filter().all()
        results = [ob.as_json() for ob in resultset]

        res_paginator, num_pages = self._pagination(request, results)
        data = {'films' : res_paginator.object_list}
        data['page_count'] = num_pages
        res_response = json.dumps(data)
        return HttpResponse(res_response, content_type="application/json")



    def _pagination(self, request, results_list : list) -> (Page, int):
        paginator = Paginator(results_list, self.YOUR_PAGE_SIZE)
        
        page = request.GET.get('page')
        try:
            res_paginator = paginator.page(page)
        except PageNotAnInteger:
            res_paginator = paginator.page(1)
        except EmptyPage:
            res_paginator = paginator.page(paginator.num_pages)

        return res_paginator, paginator.num_pages






class JsonViewPopularMovies(View):
    NUMBER_OF_WEEKS = 4 
    DEFAULT_NUMBER_OF_MOVIES = 10
    def get(self, request):
        print('JsonViewPopularMovies')

        number_of_movies = self._parsing_parameters(request)

        resultset = FilmInfoManager(self.NUMBER_OF_WEEKS, number_of_movies).get_filter()
        results = [ob.as_json() for ob in resultset]

        
        res_response = json.dumps(results)
        return HttpResponse(res_response, content_type="application/json")


    def _parsing_parameters(self, request) -> int:
        number_of_movies = request.GET.get('number')

        if number_of_movies == None or number_of_movies == '':
            if not is_number(number_of_movies):
                number_of_movies = self.DEFAULT_NUMBER_OF_MOVIES

        return int(number_of_movies)


def is_number(var):
    try:
        if var == int(var):
            return True
    except Exception:
        return False