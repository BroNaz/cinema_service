from django.db import models

# Create your models here.
class Person(models.Model):
    """Representation of an individual with the first and last name fields"""
    name = models.CharField('Name', max_length=255)
    last_name = models.CharField('Last name', max_length=255)

    class Meta:
        db_table = 'person'

class Film(models.Model):
    """information about the film"""
    name = models.CharField('Title', max_length=255)
    release_date = models.DateField('Release data')
    producer = models.ForeignKey(to='Person', verbose_name='Producer',
                                    on_delete=models.CASCADE, related_name='producer') # возможно придется менять to
    actors = models.ManyToManyField(to=Person, verbose_name='Actors', related_name='actors')

    class Meta:
        db_table = 'film'

class FilmInfo(models.Model):
    """information about watching movies"""
    date = models.DateField('Date')
    number_of_views = models.IntegerField('number of views')
    film = models.ForeignKey(to='Film', verbose_name='Film', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'film_info'
