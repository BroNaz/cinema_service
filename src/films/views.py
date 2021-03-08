from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json 
from django.views import generic
from django.core import serializers # вроде как его используют для сериализации, необходимо затестить
from django.views import View
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, Page
from datetime import date, datetime

from .models import Film


class JsonViewMovies(View):
    """
    command for getting a list of movies with the possibility of pagination 
    and filters by actor, director, year.
    Pagination and filtering occurs by variables from the url, 
    namely "pagination" and " filter"

    pagination -> int 

    actor -> str 
    director -> str 
    year -> str (YYYY) or (YYYY)to(YYYY)
    """
    YOUR_PAGE_SIZE = 10
    def get(self, request):
        """v0 - вернем пока что все фильмы"""
        resultset = Film.objects.all()
        results = [ob.as_json() for ob in resultset]

        filter = Filters(Film, request)

        print(filter)

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



class Filters():
    def __init__(self, type_model, request):
        self.request = request
        self.type_model = type_model 
        self.filter_parametrs = dict()
        self._filter_parser()

    def _filter_parser(self):
        temp = self.request.GET.get('actor')
        if temp != None and temp != '':
            self.filter_parametrs['actor'] = temp
            
        temp = self.request.GET.get('director') 
        if temp != None and temp != '':
            self.filter_parametrs['director'] = temp

        temp = self.request.GET.get('year')
        if temp != None and temp != '':
            if 'to' not in temp:
                if data_check(temp):
                    self.filter_parametrs['date'] = temp
            else :
                temp = temp.split('to',2)[0:2]
                if data_check_range(temp):
                    self.filter_parametrs['date_range'] = temp

    def get_filter(self):
        films = self.type_model.objects.all()
        for param in self.filter_parametrs.keys:
            films.filter


    def __str__(self):
        return str(self.filter_parametrs)

# проверка даты по нашим правилам
def data_check(date:str) -> bool:
    d = datetime.strptime(date, '%Y').date()
    return d.year >= 1900

def data_check_range(dates:list) -> bool:
    if len(dates) > 2:
        return False
    d1 = datetime.strptime(dates[0], '%Y').date()
    d2 = datetime.strptime(dates[1], '%Y').date()
    
    return d1.year >= 1900 and d1 <= d2