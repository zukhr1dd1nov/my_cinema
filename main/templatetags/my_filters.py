import datetime

from django import template
from main.models import MovieModel, ScheduleModel

register = template.Library()

def my_time(value):
    return f'{value.split(":")[0]} ч. {value.split(":")[1]} мин.'

def category(value):
    if MovieModel.objects.filter(category__name=value,is_active=True).count() != 0:
        return MovieModel.objects.filter(category__name=value,is_active=True)
    return None

def movie(value):
    if ScheduleModel.objects.filter(movie_id=value.id).count() != 0:
        return ScheduleModel.objects.filter(movie_id=value.id).order_by('date','time')
    return None

def is_searched(value , is_searched):
    if not is_searched:
       return ScheduleModel.objects.filter(movie__is_active=True,date__gte=datetime.datetime.today()).order_by('date','time')
    return value

register.filter('is_searched', is_searched)
register.filter('movie', movie)
register.filter('category', category)
register.filter('my_time', my_time)