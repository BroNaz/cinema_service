from django.db import models
from django.views import generic

# Create your models here.
class Person(models.Model):
    """Representation of an individual with the first and last name fields"""
    name = models.CharField('Name', max_length=255)
    last_name = models.CharField('Last name', max_length=255)

    def __str__(self):
        return f'{self.name} {self.last_name}'

    def as_json(self):
        return dict(
            name = self.name,
            last_name=self.last_name)

    class Meta:
        db_table = 'person'

class Film(models.Model):
    """information about the film"""
    name = models.CharField('Title', max_length=255)
    release_date = models.DateField('Release date')
    producer = models.ForeignKey(to='Person', verbose_name='Producer',
                                    on_delete=models.CASCADE, related_name='producer') # возможно придется менять to
    actors = models.ManyToManyField(to=Person, verbose_name='Actors', related_name='actors')

    def __str__(self):
        return f'{self.name}'

    def as_json(self):
        return dict(
            name = self.name,
            release_date=self.release_date.isoformat(), 
            producer=self.producer.as_json(),
            actors= [ob.as_json() for ob in self.actors.all()])


    class Meta:
        db_table = 'film'

class FilmInfo(models.Model):
    """information about watching movies"""
    date = models.DateField('Date')
    number_of_views = models.IntegerField('number of views')
    film = models.ForeignKey(to='Film', verbose_name='Film', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.film}'
    
    class Meta:
        db_table = 'film_info'

