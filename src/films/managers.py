from datetime import date, datetime

from .models import Film

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
        d = datetime.strptime(date, '%Y').date()
        res = d.year >= 1900
    except:
        return False
    return res 

def person_preparation(person:str) -> list():
    res = person.split(' ',2)
    if len(res) < 2: 
        res.append('')
    return res 
