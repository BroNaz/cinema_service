from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json 
from django.views import generic
from django.core import serializers # вроде как его используют для сериализации, необходимо затестить
from django.views import View
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, Page

from .models import Film
from .managers import FilmManager


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
        resultset = FilmManager(request).get_filter().all()
        results = [ob.as_json() for ob in resultset]

        res_paginator, num_pages = self._pagination(request, results)

        data = {'films' : res_paginator.object_list}
        data['page_count'] = num_pages
        res_response = json.dumps(data)
        return HttpResponse(res_response, content_type="application/json")



    def _pagination(self, request, results_list : list) -> (Page, int):
        paginator = Paginator(results_list, self.YOUR_PAGE_SIZE)
        
        page = request.GET.get('pagination')
        try:
            res_paginator = paginator.page(page)
        except PageNotAnInteger:
            res_paginator = paginator.page(1)
        except EmptyPage:
            res_paginator = paginator.page(paginator.num_pages)

        return res_paginator, paginator.num_pages






class JsonViewPopularMovies(View):
    def get(self, request):
        return JsonResponse({'some': 'data'})


