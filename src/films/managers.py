import datetime


from .models import Film, FilmInfo

class FilmManager():
    def __init__(self, request):
        self.params = request.GET

    def get_filter(self):
        films = Film.objects
        params = ['actor', 'producer', 'year']
        for param in params:
            for item in self.params.getlist(param):
                if param == 'actor':
                    item = person_preparation(item)
                    films = films\
                    .filter(actors__name__contains=item[0])
                    if item[1] != '':
                        films = films.filter(actors__last_name__contains=item[1])

                elif param == 'producer':
                    item = person_preparation(item)
                    films = films\
                    .filter(producer__name__contains=item[0])
                    if item[1] != '':
                        films = films.filter(producer__last_name__contains=item[1])

                elif param == 'year':
                    if data_check(item):
                        films = films.filter(release_date__year=item)

        return films

def data_check(date:str) -> bool:
    try:
        d = datetime.datetime.strptime(date, '%Y').date()
        res = d.year >= 1900
    except:
        return False
    return res 

def person_preparation(person:str) -> list():
    res = person.split(' ',2)
    if len(res) < 2: 
        res.append('')
    return res 


class FilmInfoManager():

    def __init__(self, number_of_weeks: int, default_number_of_movies: int ):
        self.delta = datetime.timedelta(days= 7 * number_of_weeks)
        self.default_number_of_movies = default_number_of_movies

    def get_filter(self):
        films_info = FilmInfo.objects.filter(date__gte=datetime.datetime.now() - self.delta,
                                                date__lte=datetime.datetime.now()) 

        films_info = films_info.order_by('-number_of_views')[0:self.default_number_of_movies]
        return films_info