import json 
import cinema_service.settings as settings

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views import View
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, Page

from .models import Film
from .managers import FilmManager, FilmInfoManager
from .utils import is_number



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
    def get(self, request):

        resultset = FilmManager(request).get_filter().all()
        results = [ob.as_json() for ob in resultset]

        res_paginator, num_pages = self._pagination(request, results)
        data = {'films' : res_paginator.object_list}
        data['page_count'] = num_pages
        res_response = json.dumps(data)
        return HttpResponse(res_response, content_type="application/json")



    def _pagination(self, request, results_list : list) -> (Page, int):
        paginator = Paginator(results_list, settings.PAGE_SIZE)
        
        page = request.GET.get('page')
        try:
            res_paginator = paginator.page(page)
        except PageNotAnInteger:
            res_paginator = paginator.page(1)
        except EmptyPage:
            res_paginator = paginator.page(paginator.num_pages)

        return res_paginator, paginator.num_pages






class JsonViewPopularMovies(View):
    """
    Command to get N popular movies 
    (select N movies with the most views in the last 4 weeks, 
    N is passed to the command as a parameter, 4 weeks is set 
    in the configuration)

    number -> int 
    """
    def get(self, request):

        number_of_movies = self._parsing_parameters(request)

        resultset = FilmInfoManager(settings.NUMBER_OF_WEEKS, number_of_movies).get_filter()
        results = [ob.as_json() for ob in resultset]

        
        res_response = json.dumps(results)
        return HttpResponse(res_response, content_type="application/json")


    def _parsing_parameters(self, request) -> int:
        number_of_movies = request.GET.get('number')

        if number_of_movies == None or number_of_movies == '':
            if not is_number(number_of_movies):
                number_of_movies = settings.DEFAULT_NUMBER_OF_MOVIES

        return int(number_of_movies)
