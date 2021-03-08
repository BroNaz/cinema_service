from .models import Film

class FilmManager():
    def __init__(self, request):
        self.params = request.GET
        self.filter_parametrs = dict()

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
        films = Film.objects
        params = ['actor', 'director', 'year']
        for param in params:
            for item in self.params.getlist(param):
                if param == 'actor':
                    # if check good params
                    films = films
                    .filter(desc__contains=filter, actors__name__contains="Foo")
                    .filter(desc__contains=filter, actors__last_name__contains="Foo")
                    .order_by("desc")

                elif param == 'director':
                    # if check good params
                    films = films
                    .filter(desc__contains=filter, producer__name__contains="Foo")
                    .filter(desc__contains=filter, producer__last_name__contains="Foo")
                    .order_by("desc")

                elif param == 'year':
                    films = films.filter(release_date__year='2012')

        return films


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




"""


"""