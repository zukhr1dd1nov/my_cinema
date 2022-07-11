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
        return ScheduleModel.objects.filter(movie_id=value.id)
    return None

register.filter('movie', movie)
register.filter('category', category)
register.filter('my_time', my_time)