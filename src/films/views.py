from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json 
from django.views import generic
from django.core import serializers # вроде как его используют для сериализации, необходимо затестить
from django.views import View
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    YOUR_PAGE_SIZE = 10
    def get(self, request):
        """v0 - вернем пока что все фильмы"""
        resultset = Film.objects.all()
        results = [ob.as_json() for ob in resultset]

        paginator = Paginator(results, self.YOUR_PAGE_SIZE)
        
        res_paginator = None
        page = request.GET.get('pagination')
        try:
            res_paginator = paginator.page(page)
        except PageNotAnInteger:
            res_paginator = paginator.page(1)
        except EmptyPage:
            res_paginator = paginator.page(paginator.num_pages)

        data = {'films' : res_paginator.object_list}
        data['page_count'] = paginator.num_pages
        res_response = json.dumps(data)
        return HttpResponse(res_response, content_type="application/json")


class JsonViewPopularMovies(View):
    def get(self, request):
        return JsonResponse({'some': 'data'})

